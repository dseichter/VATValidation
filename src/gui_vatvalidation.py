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

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QTabWidget, QLabel, QLineEdit, QPushButton, 
                               QTextEdit, QComboBox, QProgressBar,
                               QGridLayout, QFrame, QStatusBar)
from PySide6.QtGui import QAction

import icons
import helper

ID_CLOSE = 6000
ID_GITHUB = 6001
ID_ABOUT = 6002


class MainFrame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")
        self.resize(642, 552)
        self.setWindowIcon(icons.get_icon('select_check_box_24dp_097e23_fill1_wght400_grad0_opsz24'))
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # Create tabs
        self.create_single_tab()
        self.create_batch_tab()
        self.create_config_tab()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Center window
        self.move_to_center()
    
    def create_single_tab(self):
        """Create the Single validation tab"""
        single_widget = QWidget()
        layout = QVBoxLayout(single_widget)
        
        # Form layout
        form_layout = QGridLayout()
        
        # Own VAT
        form_layout.addWidget(QLabel("Own VAT"), 0, 0)
        self.textOwnvat = QLineEdit()
        self.textOwnvat.setFixedWidth(150)
        form_layout.addWidget(self.textOwnvat, 0, 1)
        
        self.buttonClear = QPushButton("Clear")
        self.buttonClear.setIcon(icons.get_icon('restart_alt_24dp_097e23_fill1_wght400_grad0_opsz24'))
        self.buttonClear.setToolTip("Clear all entries except your own VAT (if saved).")
        form_layout.addWidget(self.buttonClear, 0, 2)
        
        # Foreign VAT
        form_layout.addWidget(QLabel("Foreign VAT"), 1, 0)
        self.textForeignvat = QLineEdit()
        self.textForeignvat.setFixedWidth(150)
        form_layout.addWidget(self.textForeignvat, 1, 1)
        
        # Company
        form_layout.addWidget(QLabel("Company"), 2, 0)
        self.textCompany = QLineEdit()
        form_layout.addWidget(self.textCompany, 2, 1, 1, 2)
        
        # Street
        form_layout.addWidget(QLabel("Street"), 3, 0)
        self.textStreet = QLineEdit()
        form_layout.addWidget(self.textStreet, 3, 1, 1, 2)
        
        # ZIP
        form_layout.addWidget(QLabel("ZIP"), 4, 0)
        self.textZip = QLineEdit()
        form_layout.addWidget(self.textZip, 4, 1)
        
        # Town
        form_layout.addWidget(QLabel("Town"), 5, 0)
        self.textTown = QLineEdit()
        form_layout.addWidget(self.textTown, 5, 1, 1, 2)
        
        # Validate button
        self.buttonValidateSingle = QPushButton("Validate your entries")
        self.buttonValidateSingle.setIcon(icons.get_icon('playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24'))
        self.buttonValidateSingle.setToolTip("Start validating your entries.")
        form_layout.addWidget(self.buttonValidateSingle, 6, 1)
        
        layout.addLayout(form_layout)
        
        # Separator line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        
        # Results section
        results_layout = QGridLayout()
        
        self.m_staticText_ValidationResult = QLabel("Validation Result")
        results_layout.addWidget(self.m_staticText_ValidationResult, 0, 0, 1, 2)
        
        results_layout.addWidget(QLabel("Result"), 1, 0)
        self.textResultCode = QLineEdit()
        results_layout.addWidget(self.textResultCode, 1, 1)
        
        results_layout.addWidget(QLabel("Valid"), 2, 0)
        self.textResultIsValid = QLineEdit()
        results_layout.addWidget(self.textResultIsValid, 2, 1)
        
        results_layout.addWidget(QLabel("Details"), 3, 0)
        self.textResultDetails = QTextEdit()
        self.textResultDetails.setMinimumHeight(100)
        results_layout.addWidget(self.textResultDetails, 3, 1)
        
        layout.addLayout(results_layout)
        
        self.tab_widget.addTab(single_widget, icons.get_icon('task_24dp_097e23_fill1_wght400_grad0_opsz24'), "Single")
    
    def create_batch_tab(self):
        """Create the Batch processing tab"""
        batch_widget = QWidget()
        layout = QVBoxLayout(batch_widget)
        
        # File selection layout
        file_layout = QGridLayout()
        
        # Input file
        file_layout.addWidget(QLabel("Input file"), 0, 0)
        input_layout = QHBoxLayout()
        self.textInputFile = QLineEdit()
        self.buttonInputFile = QPushButton("Browse...")
        input_layout.addWidget(self.textInputFile)
        input_layout.addWidget(self.buttonInputFile)
        file_layout.addLayout(input_layout, 0, 1)
        
        # Output file
        file_layout.addWidget(QLabel("Output file"), 1, 0)
        output_layout = QHBoxLayout()
        self.textOutputFile = QLineEdit()
        self.buttonOutputFile = QPushButton("Browse...")
        output_layout.addWidget(self.textOutputFile)
        output_layout.addWidget(self.buttonOutputFile)
        file_layout.addLayout(output_layout, 1, 1)
        
        # Validate button
        self.buttonValidateBatch = QPushButton("Start processing file")
        self.buttonValidateBatch.setIcon(icons.get_icon('playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24'))
        self.buttonValidateBatch.setToolTip("Start processing your input file. This can take a while and the UI can stop for some seconds to work.")
        file_layout.addWidget(self.buttonValidateBatch, 2, 1)
        
        layout.addLayout(file_layout)
        
        # Separator line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        
        # Progress section
        progress_layout = QGridLayout()
        
        progress_layout.addWidget(QLabel("Records found"), 0, 0)
        self.staticText_RecordsFoundValue = QLabel("0")
        progress_layout.addWidget(self.staticText_RecordsFoundValue, 0, 1)
        
        progress_layout.addWidget(QLabel("Progress"), 1, 0)
        self.progressProcessing = QProgressBar()
        progress_layout.addWidget(self.progressProcessing, 1, 1)
        
        self.staticText_ProcessingXofY = QLabel("0/0")
        progress_layout.addWidget(self.staticText_ProcessingXofY, 2, 1)
        
        layout.addLayout(progress_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(batch_widget, icons.get_icon('playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24'), "Batch")
    
    def create_config_tab(self):
        """Create the Configuration tab"""
        config_widget = QWidget()
        layout = QVBoxLayout(config_widget)
        
        config_layout = QGridLayout()
        
        # Own VAT
        config_layout.addWidget(QLabel("Own VAT"), 0, 0)
        self.textCtrlConfigOwnVat = QLineEdit()
        self.textCtrlConfigOwnVat.setFixedWidth(150)
        config_layout.addWidget(self.textCtrlConfigOwnVat, 0, 1)
        
        # Interface
        config_layout.addWidget(QLabel("Interface"), 1, 0)
        interface_layout = QHBoxLayout()
        self.comboBoxConfigInterface = QComboBox()
        self.comboBoxConfigInterface.addItems(["vies", "bzst"])
        interface_layout.addWidget(self.comboBoxConfigInterface)
        interface_note = QLabel("(HMRC will be detected automatically)")
        interface_note.setStyleSheet("color: gray; font-size: 10px;")
        interface_layout.addWidget(interface_note)
        config_layout.addLayout(interface_layout, 1, 1)
        
        # Language
        config_layout.addWidget(QLabel("Language"), 2, 0)
        self.comboBoxConfigLanguage = QComboBox()
        self.comboBoxConfigLanguage.addItems(["en", "de"])
        config_layout.addWidget(self.comboBoxConfigLanguage, 2, 1)
        
        # CSV delimiter
        config_layout.addWidget(QLabel("CSV delimiter"), 3, 0)
        self.textConfigCSVdelimiter = QLineEdit()
        self.textConfigCSVdelimiter.setMaxLength(1)
        self.textConfigCSVdelimiter.setFixedWidth(20)
        config_layout.addWidget(self.textConfigCSVdelimiter, 3, 1)
        
        # Logfile
        config_layout.addWidget(QLabel("Logfile"), 4, 0)
        logfile_layout = QHBoxLayout()
        self.textCtrlConfigLogfile = QLineEdit()
        self.textCtrlConfigLogfile.setMinimumWidth(400)
        self.buttonConfigLogfile = QPushButton("Logfile")
        self.buttonConfigLogfile.setIcon(icons.get_icon('overview_24dp_097e23_fill1_wght400_grad0_opsz24'))
        logfile_layout.addWidget(self.textCtrlConfigLogfile)
        logfile_layout.addWidget(self.buttonConfigLogfile)
        config_layout.addLayout(logfile_layout, 4, 1, 1, 2)
        
        # Loglevel
        config_layout.addWidget(QLabel("Loglevel"), 5, 0)
        self.comboBoxConfigLoglevel = QComboBox()
        self.comboBoxConfigLoglevel.addItems(["DEBUG", "ERROR"])
        self.comboBoxConfigLoglevel.setCurrentIndex(1)
        config_layout.addWidget(self.comboBoxConfigLoglevel, 5, 1)
        
        # Theme
        config_layout.addWidget(QLabel("Theme"), 6, 0)
        self.comboBoxConfigTheme = QComboBox()
        self.comboBoxConfigTheme.addItems(["system", "light", "dark"])
        config_layout.addWidget(self.comboBoxConfigTheme, 6, 1)
        
        # Save button
        self.buttonSaveConfig = QPushButton("Save")
        self.buttonSaveConfig.setIcon(icons.get_icon('save_24dp_097e23_fill1_wght400_grad0_opsz24'))
        config_layout.addWidget(self.buttonSaveConfig, 7, 0)
        
        layout.addLayout(config_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(config_widget, icons.get_icon('settings_24dp_097e23_fill1_wght400_grad0_opsz24'), "Configuration")
    
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        close_action = QAction("Close", self)
        close_action.setIcon(icons.get_icon('exit_to_app_24dp_097e23_fill1_wght400_grad0_opsz24'))
        close_action.setStatusTip("Close VATValidation")
        close_action.triggered.connect(self.vatvalidationClose)
        file_menu.addAction(close_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        support_action = QAction("Support...", self)
        support_action.setIcon(icons.get_icon('contact_support_24dp_097e23_fill1_wght400_grad0_opsz24'))
        support_action.setStatusTip("Go to GitHub repository.")
        support_action.triggered.connect(self.openGitHubRepo)
        help_menu.addAction(support_action)
        
        website_action = QAction("Open Website", self)
        website_action.setIcon(icons.get_icon('globe_24dp_097e23_fill1_wght400_grad0_opsz24'))
        website_action.setStatusTip("Open website for further information.")
        website_action.triggered.connect(self.openWebsite)
        help_menu.addAction(website_action)
        
        update_action = QAction("Check for updates", self)
        update_action.setIcon(icons.get_icon('restart_alt_24dp_097e23_fill1_wght400_grad0_opsz24'))
        update_action.setStatusTip("Check, if there is an update available.")
        update_action.triggered.connect(self.checkForUpdates)
        help_menu.addAction(update_action)
        
        about_action = QAction("About...", self)
        about_action.setIcon(icons.get_icon('info_24dp_097e23_fill1_wght400_grad0_opsz24'))
        about_action.setStatusTip("About VATValidation")
        about_action.triggered.connect(self.vatvalidationAbout)
        help_menu.addAction(about_action)
    
    def move_to_center(self):
        """Center the window on the screen"""
        screen_rect = self.screen().geometry()
        window_rect = self.frameGeometry()
        x = (screen_rect.width() - window_rect.width()) // 2
        y = (screen_rect.height() - window_rect.height()) // 2
        self.move(max(x, 0), max(y, 0))
    
    # Virtual event handlers - to be implemented in subclass
    def loadConfig(self):
        pass
    
    def clearFields(self):
        pass
    
    def validateSingle(self):
        pass
    
    def validateBatch(self):
        pass
    
    def openLogfile(self):
        pass
    
    def saveConfig(self):
        pass
    
    def vatvalidationClose(self):
        pass
    
    def openGitHubRepo(self):
        pass
    
    def openWebsite(self):
        pass
    
    def checkForUpdates(self):
        pass
    
    def vatvalidationAbout(self):
        pass