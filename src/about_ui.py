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
