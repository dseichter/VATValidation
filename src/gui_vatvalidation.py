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
import wx.xrc

import icons
import helper

ID_CLOSE = 6000
ID_GITHUB = 6001
ID_ABOUT = 6002


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=helper.NAME + " " + helper.VERSION,
            pos=wx.DefaultPosition,
            size=wx.Size(642, 552),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetIcon(icons.select_check_box_24dp_097e23_fill1_wght400_grad0_opsz24.GetIcon())

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook3 = wx.Notebook(
            self,
            wx.ID_ANY,
        )

        self.panelSingle = wx.Panel(
            self.m_notebook3,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.staticText_ownvat = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Own VAT",
        )
        self.staticText_ownvat.Wrap(-1)

        fgSizer2.Add(self.staticText_ownvat, 0, wx.ALL, 5)

        self.textOwnvat = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textOwnvat, 0, wx.ALL, 5)

        self.buttonClear = wx.Button(
            self.panelSingle,
            wx.ID_ANY,
            "Clear",
        )
        self.buttonClear.SetBitmap(icons.restart_alt_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.buttonClear.SetToolTip("Clear all entries except your own VAT (if saved).")

        fgSizer2.Add(self.buttonClear, 0, wx.ALIGN_CENTER, 5)

        self.staticText_foreignvat = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Foreign VAT",
        )
        self.staticText_foreignvat.Wrap(-1)

        fgSizer2.Add(self.staticText_foreignvat, 0, wx.ALL, 5)

        self.textForeignvat = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textForeignvat, 0, wx.ALL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticText_company = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Company",
        )
        self.staticText_company.Wrap(-1)

        fgSizer2.Add(self.staticText_company, 0, wx.ALL, 5)

        self.textCompany = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textCompany, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticText_street = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Street",
        )
        self.staticText_street.Wrap(-1)

        fgSizer2.Add(self.staticText_street, 0, wx.ALL, 5)

        self.textStreet = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textStreet, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticText_zip = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "ZIP",
        )
        self.staticText_zip.Wrap(-1)

        fgSizer2.Add(self.staticText_zip, 0, wx.ALL, 5)

        self.textZip = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textZip, 0, wx.ALL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticText_town = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Town",
        )
        self.staticText_town.Wrap(-1)

        fgSizer2.Add(self.staticText_town, 0, wx.ALL, 5)

        self.textTown = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer2.Add(self.textTown, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonValidateSingle = wx.Button(
            self.panelSingle,
            wx.ID_ANY,
            "Validate your entries",
        )
        self.buttonValidateSingle.SetBitmap(icons.playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.buttonValidateSingle.SetToolTip("Start validating your entries.")

        fgSizer2.Add(self.buttonValidateSingle, 0, wx.ALIGN_CENTER, 5)

        bSizer3.Add(fgSizer2, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline5 = wx.StaticLine(
            self.panelSingle,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LI_HORIZONTAL,
        )
        bSizer6.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer3.Add(bSizer6, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer5.AddGrowableCol(1)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText_ValidationResult = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Validation Result",
        )
        self.m_staticText_ValidationResult.Wrap(-1)

        self.m_staticText_ValidationResult.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                wx.EmptyString,
            )
        )

        fgSizer5.Add(self.m_staticText_ValidationResult, 0, wx.ALL, 5)

        self.staticText_result = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Result",
        )
        self.staticText_result.Wrap(-1)

        fgSizer5.Add(self.staticText_result, 0, wx.ALL, 5)

        self.textResultCode = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer5.Add(self.textResultCode, 0, wx.ALL, 5)

        self.staticText_isvalid = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Valid",
        )
        self.staticText_isvalid.Wrap(-1)

        fgSizer5.Add(self.staticText_isvalid, 0, wx.ALL, 5)

        self.textResultIsValid = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer5.Add(self.textResultIsValid, 0, wx.ALL, 5)

        self.staticText_details = wx.StaticText(
            self.panelSingle,
            wx.ID_ANY,
            "Details",
        )
        self.staticText_details.Wrap(-1)

        fgSizer5.Add(self.staticText_details, 0, wx.ALL, 5)

        self.textResultDetails = wx.TextCtrl(
            self.panelSingle,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE,
        )
        self.textResultDetails.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_SCRIPT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )
        self.textResultDetails.SetMinSize(wx.Size(-1, 100))

        fgSizer5.Add(self.textResultDetails, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.panelSingle.SetSizer(bSizer3)
        self.panelSingle.Layout()
        bSizer3.Fit(self.panelSingle)
        self.m_notebook3.AddPage(self.panelSingle, "Single", True)
        self.panelBatch = wx.Panel(
            self.m_notebook3,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.AddGrowableCol(1)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # INPUT FILE
        self.staticText_Inputfile = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "Input file",
        )
        self.staticText_Inputfile.Wrap(-1)

        fgSizer3.Add(self.staticText_Inputfile, 0, wx.ALL, 5)

        self.filepickerInput = wx.FilePickerCtrl(
            self.panelBatch,
            wx.ID_ANY,
            wx.EmptyString,
            "Select a file",
            "CSV files (*.csv)|*.csv|Excel files (*.xlsx)|*.xlsx|JSON files (*.json)|*.json|All files (*.*)|*.*",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.FLP_USE_TEXTCTRL | wx.FLP_OPEN | wx.FLP_FILE_MUST_EXIST | wx.FLP_SMALL,
        )
        self.filepickerInput.SetToolTip("Select your input file (JSON, XSLX, CSV) for processing.")

        fgSizer3.Add(self.filepickerInput, 1, wx.ALL | wx.EXPAND, 5)

        # OUTPUT FILE
        self.staticText_Outputfile = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "Output file",
        )
        self.staticText_Outputfile.Wrap(-1)

        fgSizer3.Add(self.staticText_Outputfile, 0, wx.ALL, 5)

        self.filepickerOutput = wx.FilePickerCtrl(
            self.panelBatch,
            wx.ID_ANY,
            wx.EmptyString,
            "Select a file",
            "CSV files (*.csv)|*.csv|Excel files (*.xlsx)|*.xlsx|JSON files (*.json)|*.json|All files (*.*)|*.*",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT | wx.FLP_SMALL,
        )

        self.filepickerOutput.SetToolTip("Select your output file to store the validation results to.")

        fgSizer3.Add(self.filepickerOutput, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonValidateBatch = wx.Button(
            self.panelBatch,
            wx.ID_ANY,
            "Start processing file",
        )
        self.buttonValidateBatch.SetBitmap(icons.playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.buttonValidateBatch.SetToolTip("Start processing your input file. This can take a while and the UI can stop for some seconds to work.")

        fgSizer3.Add(self.buttonValidateBatch, 0, wx.ALIGN_LEFT, 5)

        bSizer9.Add(fgSizer3, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline10 = wx.StaticLine(
            self.panelBatch,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LI_HORIZONTAL,
        )
        bSizer12.Add(self.m_staticline10, 0, wx.EXPAND | wx.ALL, 5)

        bSizer9.Add(bSizer12, 0, wx.EXPAND, 5)

        fgSizer51 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer51.SetFlexibleDirection(wx.BOTH)
        fgSizer51.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.staticText_RecordsFound = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "Records found",
        )
        self.staticText_RecordsFound.Wrap(-1)

        fgSizer51.Add(self.staticText_RecordsFound, 0, wx.ALL, 5)

        self.staticText_RecordsFound = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "0",
        )
        self.staticText_RecordsFound.Wrap(-1)

        fgSizer51.Add(self.staticText_RecordsFound, 0, wx.ALL, 5)

        self.staticText_Progress = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "Progress",
        )
        self.staticText_Progress.Wrap(-1)

        fgSizer51.Add(self.staticText_Progress, 0, wx.ALL, 5)

        self.progressProcessing = wx.Gauge(
            self.panelBatch,
            wx.ID_ANY,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.GA_HORIZONTAL,
        )
        self.progressProcessing.SetValue(0)
        fgSizer51.Add(self.progressProcessing, 0, wx.ALL, 5)

        fgSizer51.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticText_ProcessingXofY = wx.StaticText(
            self.panelBatch,
            wx.ID_ANY,
            "0/0",
        )
        self.staticText_ProcessingXofY.Wrap(-1)

        fgSizer51.Add(self.staticText_ProcessingXofY, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer51, 1, wx.EXPAND, 5)

        self.panelBatch.SetSizer(bSizer9)
        self.panelBatch.Layout()
        bSizer9.Fit(self.panelBatch)
        self.m_notebook3.AddPage(self.panelBatch, "Batch", False)
        self.panelConfig = wx.Panel(
            self.m_notebook3,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        fgSizer31 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.staticTextConfigOwnVat = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "Own VAT",
        )
        self.staticTextConfigOwnVat.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigOwnVat, 0, wx.ALL, 5)

        self.textCtrlConfigOwnVat = wx.TextCtrl(
            self.panelConfig,
            wx.ID_ANY,
            wx.EmptyString,
        )
        fgSizer31.Add(self.textCtrlConfigOwnVat, 0, wx.ALL, 5)

        fgSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticTextConfigInterface = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "Interface",
        )
        self.staticTextConfigInterface.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigInterface, 0, wx.ALL, 5)

        comboBoxConfigInterfaceChoices = ["vies", "bzst"]
        self.comboBoxConfigInterface = wx.ComboBox(
            self.panelConfig,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            comboBoxConfigInterfaceChoices,
            0,
        )
        self.comboBoxConfigInterface.SetSelection(0)
        fgSizer31.Add(self.comboBoxConfigInterface, 0, wx.ALL, 5)

        fgSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticTextConfigLanguage = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "Language",
        )
        self.staticTextConfigLanguage.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigLanguage, 0, wx.ALL, 5)

        comboBoxConfigLanguageChoices = ["en", "de"]
        self.comboBoxConfigLanguage = wx.ComboBox(
            self.panelConfig,
            wx.ID_ANY,
            "Combo!",
            wx.DefaultPosition,
            wx.DefaultSize,
            comboBoxConfigLanguageChoices,
            0,
        )
        self.comboBoxConfigLanguage.SetSelection(0)
        fgSizer31.Add(self.comboBoxConfigLanguage, 0, wx.ALL, 5)

        fgSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticTextConfigCSVDelimiter = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "CSV delimiter",
        )
        self.staticTextConfigCSVDelimiter.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigCSVDelimiter, 0, wx.ALL, 5)

        self.textConfigCSVdelimiter = wx.TextCtrl(
            self.panelConfig,
            wx.ID_ANY,
            wx.EmptyString,
        )
        self.textConfigCSVdelimiter.SetMaxLength(1)
        self.textConfigCSVdelimiter.SetMinSize(wx.Size(20, -1))

        fgSizer31.Add(self.textConfigCSVdelimiter, 0, wx.ALL, 5)

        fgSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.staticTextConfigLogfile = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "Logfile",
        )
        self.staticTextConfigLogfile.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigLogfile, 0, wx.ALL, 5)

        self.textCtrlConfigLogfile = wx.TextCtrl(
            self.panelConfig,
            wx.ID_ANY,
            wx.EmptyString,
        )
        self.textCtrlConfigLogfile.SetMinSize(wx.Size(400, -1))

        fgSizer31.Add(self.textCtrlConfigLogfile, 1, wx.ALL | wx.EXPAND, 5)

        self.buttonConfigLogfile = wx.Button(
            self.panelConfig,
            wx.ID_ANY,
            "Logfile",
        )
        self.buttonConfigLogfile.SetBitmap(icons.overview_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        fgSizer31.Add(self.buttonConfigLogfile, 0, wx.ALL, 5)

        self.staticTextConfigLogLevel = wx.StaticText(
            self.panelConfig,
            wx.ID_ANY,
            "Loglevel",
        )
        self.staticTextConfigLogLevel.Wrap(-1)

        fgSizer31.Add(self.staticTextConfigLogLevel, 0, wx.ALL, 5)

        comboBoxConfigLoglevelChoices = ["DEBUG", "ERROR"]
        self.comboBoxConfigLoglevel = wx.ComboBox(
            self.panelConfig,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            comboBoxConfigLoglevelChoices,
            0,
        )
        self.comboBoxConfigLoglevel.SetSelection(1)
        fgSizer31.Add(self.comboBoxConfigLoglevel, 0, wx.ALL, 5)

        fgSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonSaveConfig = wx.Button(
            self.panelConfig,
            wx.ID_ANY,
            "Save",
        )
        self.buttonSaveConfig.SetBitmap(icons.save_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        fgSizer31.Add(self.buttonSaveConfig, 0, wx.ALL, 5)

        self.panelConfig.SetSizer(fgSizer31)
        self.panelConfig.Layout()
        fgSizer31.Fit(self.panelConfig)
        self.m_notebook3.AddPage(self.panelConfig, "Configuration", False)

        # create image list
        self.imageList = wx.ImageList(24, 24)
        # add the icons
        self.imageList.Add(icons.task_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.imageList.Add(icons.playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.imageList.Add(icons.settings_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        # set the image list
        self.m_notebook3.AssignImageList(self.imageList)
        # set the icons
        self.m_notebook3.SetPageImage(0, 0)
        self.m_notebook3.SetPageImage(1, 1)
        self.m_notebook3.SetPageImage(2, 2)

        # always start with first page (no need to remember, like last used page)
        self.m_notebook3.SetSelection(0)

        bSizer4.Add(self.m_notebook3, 1, wx.EXPAND | wx.ALL, 0)

        bSizer2.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.mainmenu = wx.MenuBar(0)
        self.file = wx.Menu()
        self.menuitemFileClose = wx.MenuItem(self.file, ID_CLOSE, "Close", "Close VATValidation", wx.ITEM_NORMAL)
        self.menuitemFileClose.SetBitmap(icons.exit_to_app_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.file.Append(self.menuitemFileClose)

        self.mainmenu.Append(self.file, "File")

        self.help = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem(
            self.help,
            ID_GITHUB,
            "Support...",
            "Go to GitHub repository.",
            wx.ITEM_NORMAL,
        )
        self.menuitemHelpSupport.SetBitmap(icons.contact_support_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.help.Append(self.menuitemHelpSupport)

        self.menuitemHelpWebsite = wx.MenuItem(
            self.help,
            wx.ID_ANY,
            "Open Website",
            "Open website for further information.",
            wx.ITEM_NORMAL,
        )
        self.menuitemHelpWebsite.SetBitmap(icons.globe_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.help.Append(self.menuitemHelpWebsite)

        self.menuitemHelpUpdate = wx.MenuItem(
            self.help,
            wx.ID_ANY,
            "Check for updates",
            "Check, if there is an update available.",
            wx.ITEM_NORMAL,
        )
        self.menuitemHelpUpdate.SetBitmap(icons.restart_alt_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.help.Append(self.menuitemHelpUpdate)

        self.menuitemHelpAbout = wx.MenuItem(self.help, ID_ABOUT, "About...", "About VATValidation", wx.ITEM_NORMAL)
        self.menuitemHelpAbout.SetBitmap(icons.info_24dp_097e23_fill1_wght400_grad0_opsz24.GetBitmap())
        self.help.Append(self.menuitemHelpAbout)

        self.mainmenu.Append(self.help, "Help")

        self.SetMenuBar(self.mainmenu)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SHOW, self.loadConfig)
        self.buttonClear.Bind(wx.EVT_BUTTON, self.clearFields)
        self.buttonValidateSingle.Bind(wx.EVT_BUTTON, self.validateSingle)
        self.buttonValidateBatch.Bind(wx.EVT_BUTTON, self.validateBatch)
        self.buttonConfigLogfile.Bind(wx.EVT_BUTTON, self.openLogfile)
        self.buttonSaveConfig.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.Bind(wx.EVT_MENU, self.vatvalidationClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.openGitHubRepo, id=self.menuitemHelpSupport.GetId())
        self.Bind(wx.EVT_MENU, self.openWebsite, id=self.menuitemHelpWebsite.GetId())
        self.Bind(wx.EVT_MENU, self.checkForUpdates, id=self.menuitemHelpUpdate.GetId())
        self.Bind(wx.EVT_MENU, self.vatvalidationAbout, id=self.menuitemHelpAbout.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, see vatvalidation.py
    def loadConfig(self, event):
        event.Skip()

    def clearFields(self, event):
        event.Skip()

    def validateSingle(self, event):
        event.Skip()

    def validateBatch(self, event):
        event.Skip()

    def openLogfile(self, event):
        event.Skip()

    def saveConfig(self, event):
        event.Skip()

    def vatvalidationClose(self, event):
        event.Skip()

    def openGitHubRepo(self, event):
        event.Skip()

    def openWebsite(self, event):
        event.Skip()

    def checkForUpdates(self, event):
        event.Skip()

    def vatvalidationAbout(self, event):
        event.Skip()
