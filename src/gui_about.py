# Copyright (c) 2024-2025 Daniel Seichter
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

import wx

import helper
import icons


class dialogAbout(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            title="About VATValidation",
            size=(240, 200),
        )

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bitmapLogo = wx.StaticBitmap(self)
        bSizer2.Add(self.bitmapLogo, 0, wx.ALL, 5)

        self.SetIcon(icons.select_check_box_48dp_097e23_fill1_wght400_grad0_opsz48.GetIcon())
        self.bitmapLogo.SetBitmap(icons.select_check_box_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())

        self.staticTextName = wx.StaticText(
            self,
            wx.ID_ANY,
            helper.NAME + " " + helper.VERSION,
        )
        bSizer2.Add(self.staticTextName, 0, wx.ALL, 5)

        self.staticTextLicence = wx.StaticText(
            self,
            wx.ID_ANY,
            "Licenced under " + helper.LICENCE,
        )
        bSizer2.Add(self.staticTextLicence, 0, wx.ALL, 5)

        self.staticTextGithub = wx.StaticText(
            self,
            wx.ID_ANY,
            "More on GitHub",
        )
        self.staticTextGithub.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                True,
            )
        )
        self.staticTextGithub.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.staticTextGithub.SetToolTip("Visit GitHub repository for further information.")
        bSizer2.Add(self.staticTextGithub, 0, wx.ALL, 5)

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer2.Add(m_sdbSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.staticTextGithub.Bind(wx.EVT_LEFT_DOWN, self.openGithub)

    def __del__(self):
        pass

    # Virtual event handlers, see about_ui.py
    def openGithub(self, event):
        event.Skip()
