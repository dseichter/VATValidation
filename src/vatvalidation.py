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
        self.textCtrlOwnVat.SetValue(settings.load_value_from_json_file("ownvat"))
        # visible values of configuration
        self.textOwnvat.SetValue(settings.load_value_from_json_file("ownvat"))
        self.comboBoxInterface.SetValue(settings.load_value_from_json_file("interface"))
        self.comboBoxLanguage.SetValue(settings.load_value_from_json_file("language"))
        self.textCSVdelimiter.SetValue(settings.load_value_from_json_file("delimiter"))

    # save the config file
    def saveConfig(self, event):
        # open the file
        with open("config.json", "w") as f:
            # write the data
            f.write(
                json.dumps(
                    {
                        "ownvat": self.textCtrlOwnVat.GetValue(),
                        "interface": self.comboBoxInterface.GetValue(),
                        "language": self.comboBoxLanguage.GetValue(),
                        "delimiter": self.textCSVdelimiter.GetValue(),
                    },
                    indent=2,
                )
            )

        self.textOwnvat.SetValue(settings.load_value_from_json_file("ownvat"))

    # put a blank string in text when 'Clear' is clicked
    def clearFunc(self, event):
        self.textCtrlOwnVat.SetValue(settings.load_value_from_json_file("ownvat"))
        self.textForeignvat.SetValue(str(""))
        self.textCompany.SetValue(str(""))
        self.textStreet.SetValue(str(""))
        self.textZip.SetValue(str(""))
        self.textTown.SetValue(str(""))
        self.textResultIsValid.SetValue(str(""))
        self.textResultCode.SetValue(str(""))
        self.textResultDetails.SetValue(str(""))

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
            lang=settings.load_value_from_json_file("language"),
            iscli=False,
        )
        self.textResultIsValid.SetValue("Yes" if message["valid"] else "No")
        self.textResultCode.SetValue(message["errorcode"])
        self.textResultDetails.SetValue(message.get("errorcode_description", ""))

        # In case of empty errorcode_description, load the company, address twon, zip and street into textResultDetails
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

        if self.m_filePickerOutput.GetPath() == "":
            wx.MessageBox(
                "Please select an output file.", "No output file", wx.OK | wx.ICON_ERROR
            )
            return

        batch.validatebatch(
            inputfile=self.filePickerInput.GetPath(),
            outputfile=self.m_filePickerOutput.GetPath(),
            type=settings.load_value_from_json_file("interface"),
            lang=settings.load_value_from_json_file("language"),
        )

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
