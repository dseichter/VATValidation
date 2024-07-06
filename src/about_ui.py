# import the newly created GUI file
import gui

# import VATValidation specific libraries
import helper
import webbrowser
import icons


class DialogAbout(gui.dialogAbout):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogAbout.__init__(self, parent)

        self.staticTextName.SetLabelText(helper.NAME + ' ' + helper.VERSION)
        self.staticTextLicence.SetLabelText(self.staticTextLicence.GetLabelText() + ' ' + helper.LICENCE)

        # specify all the icons
        gui.dialogAbout.SetIcon(self, icons.info.GetIcon())
        self.bitmapLogo.SetBitmap(icons.tick_box.GetBitmap())
        self.Fit()

    def openGithub(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/VATValidation')  # Add the URL of the GitHub repository

    def openIcons8(self, event):
        webbrowser.open_new_tab('https://icons8.com/')
