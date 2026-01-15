# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide6.QtCore import QTimer

import theme_manager

# Import the newly created GUI file
import gui_vatvalidation

# Import the VATValidation library
import single
import batch
import helper
import settings
import about_ui

# Import common libraries
import webbrowser
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

BATCH_STATUS_FILE = "batchstatus.json"


class VATValidationFrame(gui_vatvalidation.MainFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Connect signals
        self.buttonClear.clicked.connect(self.clearFields)
        self.buttonValidateSingle.clicked.connect(self.validateSingle)
        self.buttonValidateBatch.clicked.connect(self.validateBatch)
        self.buttonInputFile.clicked.connect(self.selectInputFile)
        self.buttonOutputFile.clicked.connect(self.selectOutputFile)
        self.buttonConfigLogfile.clicked.connect(self.openLogfile)
        self.buttonSaveConfig.clicked.connect(self.saveConfig)
        self.comboBoxConfigTheme.currentTextChanged.connect(self.themeChanged)
        
        # Load config after a short delay to ensure UI is ready
        QTimer.singleShot(100, self.loadConfig)
        
        # Setup watchdog
        QTimer.singleShot(200, self.addWatchdog)
    
    def closeEvent(self, event):
        """Handle window close event"""
        if hasattr(self, 'observer'):
            self.observer.stop()
            self.observer.join()
        if os.path.exists(BATCH_STATUS_FILE):
            os.remove(BATCH_STATUS_FILE)
        event.accept()
    
    def addWatchdog(self):
        """Setup file system watcher for batch status"""
        path = os.path.abspath(".")
        self.observer = Observer()
        event_handler = Handler(self)
        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()
    
    def onWatchdog(self, event):
        """Handle watchdog events for batch status updates"""
        if event.event_type in ["modified", "created"] and BATCH_STATUS_FILE in event.src_path:
            try:
                with open(BATCH_STATUS_FILE, "r") as f:
                    data = json.load(f)
                # Update the current status
                self.staticText_RecordsFoundValue.setText(str(data["total"]))
                self.staticText_ProcessingXofY.setText(f"{data['current']}/{data['total']}")
                self.progressProcessing.setMaximum(data["total"])
                self.progressProcessing.setValue(data["current"])
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                pass
        if event.event_type in ["deleted"] and BATCH_STATUS_FILE in event.src_path:
            self.staticText_RecordsFoundValue.setText("0")
            self.staticText_ProcessingXofY.setText("0/0")
            self.progressProcessing.setMaximum(0)
            self.progressProcessing.setValue(0)
    
    def loadConfig(self):
        """Load configuration from file"""
        settings.create_config()
        try:
            own_vat = settings.load_value_from_json_file("ownvat")
            self.textCtrlConfigOwnVat.setText(own_vat or "")
            self.textOwnvat.setText(own_vat or "")
        except TypeError:
            QMessageBox.warning(
                self,
                "Own VAT",
                "Your own VAT is not set. Please provide your own VAT within the configuration."
            )
        
        if not settings.load_value_from_json_file("ownvat"):
            QMessageBox.warning(
                self,
                "Own VAT", 
                "Your own VAT is not set. Please provide your own VAT within the configuration."
            )
        
        # Load visible configuration values
        self.comboBoxConfigLanguage.setCurrentText(settings.load_value_from_json_file("language") or "en")
        self.textConfigCSVdelimiter.setText(settings.load_value_from_json_file("delimiter") or ",")
        self.textCtrlConfigLogfile.setText(settings.load_value_from_json_file("logfilename") or "")
        self.comboBoxConfigLoglevel.setCurrentText(settings.load_value_from_json_file("loglevel") or "ERROR")
        self.comboBoxConfigTheme.setCurrentText(settings.load_value_from_json_file("theme") or "system")
        
        # Apply current theme
        theme_manager.ThemeManager.apply_theme(settings.load_value_from_json_file("theme") or "system")
    
    def saveConfig(self):
        """Save configuration to file"""
        settings.save_config("ownvat", self.textCtrlConfigOwnVat.text())
        settings.save_config("language", self.comboBoxConfigLanguage.currentText())
        settings.save_config("delimiter", self.textConfigCSVdelimiter.text())
        settings.save_config("logfilename", self.textCtrlConfigLogfile.text())
        settings.save_config("loglevel", self.comboBoxConfigLoglevel.currentText())
        settings.save_config("theme", self.comboBoxConfigTheme.currentText())
        self.textOwnvat.setText(settings.load_value_from_json_file("ownvat"))
        
        # Apply new theme
        theme_manager.ThemeManager.apply_theme(self.comboBoxConfigTheme.currentText())
        QMessageBox.information(
            self,
            "Configuration saved",
            "Your changes of your configuration have been saved."
        )
    
    def clearFields(self):
        """Clear form fields"""
        own_vat = settings.load_value_from_json_file("ownvat") or ""
        self.textCtrlConfigOwnVat.setText(own_vat)
        self.textOwnvat.setText(own_vat)
        self.textForeignvat.setText("")
        self.textCompany.setText("")
        self.textStreet.setText("")
        self.textZip.setText("")
        self.textTown.setText("")
        self.m_staticText_ValidationResult.setText("Validation Result")
        self.textResultIsValid.setText("")
        self.textResultCode.setText("")
        self.textResultDetails.setText("")
    
    def selectInputFile(self):
        """Select input file for batch processing"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "CSV files (*.csv);;Excel files (*.xlsx);;JSON files (*.json);;All files (*.*)"
        )
        if file_path:
            self.textInputFile.setText(file_path)
    
    def selectOutputFile(self):
        """Select output file for batch processing"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Select Output File", 
            "",
            "CSV files (*.csv);;Excel files (*.xlsx);;JSON files (*.json);;All files (*.*)"
        )
        if file_path:
            self.textOutputFile.setText(file_path)
    
    def openLogfile(self):
        """Open logfile in browser"""
        webbrowser.open_new_tab(self.textCtrlConfigLogfile.text())
    
    def vatvalidationClose(self):
        """Close application"""
        self.close()
    
    def validateSingle(self):
        """Validate single VAT entry"""
        QMessageBox.information(
            self,
            "Single Validation",
            "Start the single validation."
        )
        
        message = single.validatesingle(
            ownvat=self.textOwnvat.text(),
            foreignvat=self.textForeignvat.text(),
            company=self.textCompany.text(),
            street=self.textStreet.text(),
            zip=self.textZip.text(),
            town=self.textTown.text(),
            lang=settings.load_value_from_json_file("language"),
        )
        
        self.textResultIsValid.setText("Yes" if message["valid"] else "No")
        self.textResultCode.setText(message["errorcode"])
        self.textResultDetails.setText(message.get("errorcode_description", ""))
        self.m_staticText_ValidationResult.setText(f"Validation Result: (Interface: {message['type']})")
        
        # In case of empty errorcode_description, load company details
        if not message.get("errorcode_description", ""):
            details = f"Company: {message['company']}\nAddress: {message['address']}\nTown: {message['town']}\nZip: {message['zip']}\nStreet: {message['street']}"
            self.textResultDetails.setText(details)
    
    def validateBatch(self):
        """Validate batch of VAT entries"""
        reply = QMessageBox.question(
            self,
            "Batch Validation",
            "Are you sure you want to start the batch validation?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.No:
            return
        
        if not self.textOutputFile.text():
            QMessageBox.critical(self, "No output file", "Please select an output file.")
            return
        
        if not self.textInputFile.text():
            QMessageBox.critical(self, "No input file", "Please select an input file.")
            return
        
        # Check file formats
        input_ext = self.textInputFile.text().split(".")[-1].lower()
        if input_ext not in ["xlsx", "csv", "json"]:
            QMessageBox.critical(self, "Unsupported file format", "Unsupported input file format.")
            return
        
        output_ext = self.textOutputFile.text().split(".")[-1].lower()
        if output_ext not in ["xlsx", "csv", "json"]:
            QMessageBox.critical(self, "Unsupported file format", "Unsupported output file format.")
            return
        
        # Reset progress
        self.staticText_RecordsFoundValue.setText("0")
        self.staticText_ProcessingXofY.setText("0/0")
        self.progressProcessing.setMaximum(0)
        self.progressProcessing.setValue(0)
        
        # Start batch validation in thread
        download_thread = threading.Thread(
            target=batch.validatebatch,
            kwargs={
                "inputfile": self.textInputFile.text(),
                "outputfile": self.textOutputFile.text(),
                "type": "vies",
                "lang": settings.load_value_from_json_file("language"),
                "statusupdate": True,
            },
        )
        download_thread.start()
        
        # Wait for completion (this blocks the UI, matching original behavior)
        while download_thread.is_alive():
            QApplication.processEvents()
            threading.Event().wait(0.1)
        
        QMessageBox.information(self, "Batch Validation", "Batch validation done.")
    
    def openGitHubRepo(self):
        """Open GitHub repository"""
        webbrowser.open_new_tab("https://github.com/dseichter/VATValidation")
    
    def openWebsite(self):
        """Open project website"""
        webbrowser.open_new_tab("https://dseichter.github.io/VATValidation/")
    
    def checkForUpdates(self):
        """Check for application updates"""
        if helper.check_for_new_release():
            reply = QMessageBox.question(
                self,
                "Update available",
                "A new release is available.\nWould you like to open the download page?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            QMessageBox.information(self, "No update", "No new release available.")
    
    def vatvalidationAbout(self):
        """Show about dialog"""
        dlg = about_ui.DialogAbout(self)
        dlg.exec()
    
    def themeChanged(self, theme_name):
        """Apply theme immediately when changed"""
        theme_manager.ThemeManager.apply_theme(theme_name)


class Handler(FileSystemEventHandler):
    def __init__(self, parent):
        self.parent = parent
    
    def on_any_event(self, event):
        """Handle file system events"""
        # Use QTimer to ensure GUI updates happen in main thread
        QTimer.singleShot(0, lambda: self.parent.onWatchdog(event))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Apply initial theme from settings
    import settings
    settings.create_config()
    theme = settings.load_value_from_json_file("theme") or "system"
    theme_manager.ThemeManager.apply_theme(theme)
    
    frame = VATValidationFrame()
    frame.show()
    sys.exit(app.exec())