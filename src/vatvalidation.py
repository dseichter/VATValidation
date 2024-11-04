# Copyright (c) 2024 Daniel Seichter
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

# importing wx files
import wx

# import the newly created GUI file
import gui

# Import the VATValidation library
import single
import batch
import helper
import settings
import about_ui
import icons

# import common libraries
import webbrowser
import json

import logging_config  # Setup the logging
import logging

logger = logging.getLogger(__name__)


# inherit from the MainFrame created in wxFowmBuilder and create VATValidationFrame
class VATValidationFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)

        # add the version to the label
        self.SetTitle(helper.NAME + " " + helper.VERSION)

        # specify all the icons
        gui.MainFrame.SetIcon(self, icons.tick_box.GetIcon())
        self.menuitemFileClose.SetBitmap(
            icons.cancel.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap()
        )
        self.menuitemHelpSupport.SetBitmap(
            icons.get_help.GetBitmap()
            .ConvertToImage()
            .Rescale(16, 16)
            .ConvertToBitmap()
        )
        self.menuitemHelpUpdate.SetBitmap(
            icons.restart.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap()
        )
        self.menuitemHelpAbout.SetBitmap(
            icons.info.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap()
        )
        self.buttonValidateSingle.SetBitmap(icons.fry.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.buttonValidateSingle.SetSize(self.buttonValidateSingle.GetBestSize())

        self.buttonValidateBatch.SetBitmap(icons.fry.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.buttonValidateBatch.SetSize(self.buttonValidateBatch.GetBestSize())

        self.buttonClear.SetBitmap(icons.broom.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.buttonClear.SetSize(self.buttonClear.GetBestSize())

        self.m_notebook3.SetSelection(0)
        # create image list
        self.imageList = wx.ImageList(16, 16)
        # add the icons
        self.imageList.Add(
            icons.document.GetBitmap()
            .ConvertToImage()
            .Rescale(16, 16)
            .ConvertToBitmap()
        )
        self.imageList.Add(
            icons.microsoft_excel.GetBitmap()
            .ConvertToImage()
            .Rescale(16, 16)
            .ConvertToBitmap()
        )
        self.imageList.Add(
            icons.settings.GetBitmap()
            .ConvertToImage()
            .Rescale(16, 16)
            .ConvertToBitmap()
        )
        # set the image list
        self.m_notebook3.AssignImageList(self.imageList)
        # set the icons
        self.m_notebook3.SetPageImage(0, 0)
        self.m_notebook3.SetPageImage(1, 1)
        self.m_notebook3.SetPageImage(2, 2)

    # load the config file
    def loadConfig(self, event):
        settings.create_config()
        self.textCtrlConfigOwnVat.SetValue(settings.load_value_from_json_file("ownvat"))
        # visible values of configuration
        self.textOwnvat.SetValue(settings.load_value_from_json_file("ownvat"))
        self.comboBoxConfigInterface.SetValue(settings.load_value_from_json_file("interface"))
        self.comboBoxConfigLanguage.SetValue(settings.load_value_from_json_file("language"))
        self.textConfigCSVdelimiter.SetValue(settings.load_value_from_json_file("delimiter"))
        self.textCtrlConfigLogfile.SetValue(settings.load_value_from_json_file("logfilename"))
        self.comboBoxConfigLoglevel.SetValue(settings.load_value_from_json_file("loglevel"))

    # save the config file
    def saveConfig(self, event):
        # open the file
        settings.save_config("ownvat", self.textCtrlConfigOwnVat.GetValue())
        settings.save_config("interface", self.comboBoxConfigInterface.GetValue())
        settings.save_config("language", self.comboBoxConfigLanguage.GetValue())
        settings.save_config("delimiter", self.textConfigCSVdelimiter.GetValue())
        settings.save_config("logfilename", self.textCtrlConfigLogfile.GetValue())
        settings.save_config("loglevel", self.comboBoxConfigLoglevel.GetValue())
        self.textOwnvat.SetValue(settings.load_value_from_json_file("ownvat"))

    # put a blank string in text when 'Clear' is clicked
    def clearFields(self, event):
        self.textCtrlConfigOwnVat.SetValue(settings.load_value_from_json_file("ownvat"))
        self.textForeignvat.SetValue(str(""))
        self.textCompany.SetValue(str(""))
        self.textStreet.SetValue(str(""))
        self.textZip.SetValue(str(""))
        self.textTown.SetValue(str(""))
        self.textResultIsValid.SetValue(str(""))
        self.textResultCode.SetValue(str(""))
        self.textResultDetails.SetValue(str(""))
        
    def openLogfile(self, event):
        webbrowser.open_new_tab(self.textCtrlConfigLogfile.GetValue())        

    def vatvalidationClose(self, event):
        self.Close()

    def vatvalidationGitHub(self, event):
        webbrowser.open_new_tab("https://github.com/dseichter/VATValidation")

    def validateSingle(self, event):
        wx.MessageBox(
            "Start the single validation.",
            "Single Validation",
            wx.OK | wx.ICON_INFORMATION,
        )
        message = single.validatesingle(
            ownvat=self.textOwnvat.GetValue(),
            foreignvat=self.textForeignvat.GetValue(),
            company=self.textCompany.GetValue(),
            street=self.textStreet.GetValue(),
            zip=self.textZip.GetValue(),
            town=self.textTown.GetValue(),
            type=settings.load_value_from_json_file("interface"),
            lang=settings.load_value_from_json_file("language")
        )
        self.textResultIsValid.SetValue("Yes" if message["valid"] else "No")
        self.textResultCode.SetValue(message["errorcode"])
        self.textResultDetails.SetValue(message.get("errorcode_description", ""))

        # In case of empty errorcode_description, load the company, address town, zip and street into textResultDetails
        if message.get("errorcode_description", "") == "":
            self.textResultDetails.SetValue(
                f"Company: {message['company']}\nAddress: {message['address']}\nTown: {message['town']}\nZip: {message['zip']}\nStreet: {message['street']}"
            )

    def validateBatch(self, event):
        if (
            wx.MessageBox(
                "Are you sure you want to start the batch validation?",
                "Batch Validation",
                wx.YES_NO | wx.ICON_QUESTION,
            )
            == wx.NO
        ):
            return

        if self.filepickerOutput.GetPath() == "":
            wx.MessageBox(
                "Please select an output file.", "No output file", wx.OK | wx.ICON_ERROR
            )
            return

        # check if given file exists
        if not self.filepickerInput.GetPath():
            wx.MessageBox(
                "Please select an input file.", "No input file", wx.OK | wx.ICON_ERROR
            )
            return

        resultcode = batch.validatebatch(
            inputfile=self.filepickerInput.GetPath(),
            outputfile=self.filepickerOutput.GetPath(),
            type=settings.load_value_from_json_file("interface"),
            lang=settings.load_value_from_json_file("language")
        )

        if resultcode == 127:
            wx.MessageBox(
                "Unsupported file format.", "Unsupported file format", wx.OK | wx.ICON_ERROR
            )
            return

        # if done, show a message box
        wx.MessageBox(
            "Batch validation done.", "Batch Validation", wx.OK | wx.ICON_INFORMATION
        )

    def checkForUpdates(self, event):
        if helper.check_for_new_release():
            result = wx.MessageBox(
                "A new release is available.\nWould you like to open the download page?",
                "Update available",
                wx.YES_NO | wx.ICON_INFORMATION,
            )
            if result == wx.YES:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            wx.MessageBox(
                "No new release available.", "No update", wx.OK | wx.ICON_INFORMATION
            )

    def vatvalidationAbout(self, event):
        # open the about dialog
        dlg = about_ui.DialogAbout(self)
        dlg.ShowModal()
        dlg.Destroy()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of VATValidationFrame
frame = VATValidationFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
