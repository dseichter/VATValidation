# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

ID_CLOSE = 6000
ID_GITHUB = 6001
ID_ABOUT = 6002

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"VATValidation"), pos = wx.DefaultPosition, size = wx.Size( 642,552 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.panelSingle = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.AddGrowableCol( 1 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.staticText_ownvat = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Own VAT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_ownvat.Wrap( -1 )

        fgSizer2.Add( self.staticText_ownvat, 0, wx.ALL, 5 )

        self.textOwnvat = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textOwnvat, 0, wx.ALL, 5 )

        self.buttonClear = wx.Button( self.panelSingle, wx.ID_ANY, _(u"Clear"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonClear.SetToolTip( _(u"Clear all entries except your own VAT (if saved).") )

        fgSizer2.Add( self.buttonClear, 0, wx.ALIGN_CENTER, 5 )

        self.staticText_foreignvat = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Foreign VAT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_foreignvat.Wrap( -1 )

        fgSizer2.Add( self.staticText_foreignvat, 0, wx.ALL, 5 )

        self.textForeignvat = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textForeignvat, 0, wx.ALL, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticText_company = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Company"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_company.Wrap( -1 )

        fgSizer2.Add( self.staticText_company, 0, wx.ALL, 5 )

        self.textCompany = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textCompany, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticText_street = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Street"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_street.Wrap( -1 )

        fgSizer2.Add( self.staticText_street, 0, wx.ALL, 5 )

        self.textStreet = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textStreet, 0, wx.ALL|wx.EXPAND, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticText_zip = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"ZIP"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_zip.Wrap( -1 )

        fgSizer2.Add( self.staticText_zip, 0, wx.ALL, 5 )

        self.textZip = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textZip, 0, wx.ALL, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticText_town = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Town"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_town.Wrap( -1 )

        fgSizer2.Add( self.staticText_town, 0, wx.ALL, 5 )

        self.textTown = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textTown, 0, wx.ALL|wx.EXPAND, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.buttonValidateSingle = wx.Button( self.panelSingle, wx.ID_ANY, _(u"Validate your entries"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonValidateSingle.SetToolTip( _(u"Start validating your entries.") )

        fgSizer2.Add( self.buttonValidateSingle, 0, wx.ALIGN_CENTER, 5 )


        bSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticline5 = wx.StaticLine( self.panelSingle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer6.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )


        bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )

        fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer5.AddGrowableCol( 1 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText_ValidationResult = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Validation Result"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ValidationResult.Wrap( -1 )

        self.m_staticText_ValidationResult.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        fgSizer5.Add( self.m_staticText_ValidationResult, 0, wx.ALL, 5 )

        self.staticText_result = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Result"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_result.Wrap( -1 )

        fgSizer5.Add( self.staticText_result, 0, wx.ALL, 5 )

        self.textResultCode = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.textResultCode, 0, wx.ALL, 5 )

        self.staticText_isvalid = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Valid"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_isvalid.Wrap( -1 )

        fgSizer5.Add( self.staticText_isvalid, 0, wx.ALL, 5 )

        self.textResultIsValid = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.textResultIsValid, 0, wx.ALL, 5 )

        self.staticText_details = wx.StaticText( self.panelSingle, wx.ID_ANY, _(u"Details"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_details.Wrap( -1 )

        fgSizer5.Add( self.staticText_details, 0, wx.ALL, 5 )

        self.textResultDetails = wx.TextCtrl( self.panelSingle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.textResultDetails.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.textResultDetails.SetMinSize( wx.Size( -1,100 ) )

        fgSizer5.Add( self.textResultDetails, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )


        self.panelSingle.SetSizer( bSizer3 )
        self.panelSingle.Layout()
        bSizer3.Fit( self.panelSingle )
        self.m_notebook3.AddPage( self.panelSingle, _(u"Single"), True )
        self.panelBatch = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.AddGrowableCol( 1 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.staticText_Inputfile = wx.StaticText( self.panelBatch, wx.ID_ANY, _(u"Input file"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_Inputfile.Wrap( -1 )

        fgSizer3.Add( self.staticText_Inputfile, 0, wx.ALL, 5 )

        self.filepickerInput = wx.FilePickerCtrl( self.panelBatch, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        self.filepickerInput.SetToolTip( _(u"Select your input file (JSON, XML, CSV) for processing.") )

        fgSizer3.Add( self.filepickerInput, 1, wx.ALL|wx.EXPAND, 5 )

        self.staticText_Outputfile = wx.StaticText( self.panelBatch, wx.ID_ANY, _(u"Output file"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_Outputfile.Wrap( -1 )

        fgSizer3.Add( self.staticText_Outputfile, 0, wx.ALL, 5 )

        self.filepickerOutput = wx.FilePickerCtrl( self.panelBatch, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        self.filepickerOutput.SetToolTip( _(u"Select your output file to store the validation results to.") )

        fgSizer3.Add( self.filepickerOutput, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.buttonValidateBatch = wx.Button( self.panelBatch, wx.ID_ANY, _(u"Start processing file"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonValidateBatch.SetToolTip( _(u"Start processing your input file. This can take a while and the UI can stop for some seconds to work.") )

        fgSizer3.Add( self.buttonValidateBatch, 0, wx.ALIGN_LEFT, 5 )


        bSizer9.Add( fgSizer3, 0, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticline10 = wx.StaticLine( self.panelBatch, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer12.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )


        bSizer9.Add( bSizer12, 0, wx.EXPAND, 5 )

        fgSizer51 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer51.SetFlexibleDirection( wx.BOTH )
        fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.staticText_RecordsFound = wx.StaticText( self.panelBatch, wx.ID_ANY, _(u"Records found"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_RecordsFound.Wrap( -1 )

        fgSizer51.Add( self.staticText_RecordsFound, 0, wx.ALL, 5 )

        self.textRecordsFound = wx.TextCtrl( self.panelBatch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer51.Add( self.textRecordsFound, 0, wx.ALL, 5 )

        self.staticText_Progress = wx.StaticText( self.panelBatch, wx.ID_ANY, _(u"Progress"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_Progress.Wrap( -1 )

        fgSizer51.Add( self.staticText_Progress, 0, wx.ALL, 5 )

        self.progressProcessing = wx.Gauge( self.panelBatch, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.progressProcessing.SetValue( 0 )
        fgSizer51.Add( self.progressProcessing, 0, wx.ALL, 5 )


        fgSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticText_ProcessingXofY = wx.StaticText( self.panelBatch, wx.ID_ANY, _(u"0/0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_ProcessingXofY.Wrap( -1 )

        fgSizer51.Add( self.staticText_ProcessingXofY, 0, wx.ALL, 5 )


        bSizer9.Add( fgSizer51, 1, wx.EXPAND, 5 )


        self.panelBatch.SetSizer( bSizer9 )
        self.panelBatch.Layout()
        bSizer9.Fit( self.panelBatch )
        self.m_notebook3.AddPage( self.panelBatch, _(u"Batch"), False )
        self.panelConfig = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer31 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer31.AddGrowableCol( 1 )
        fgSizer31.SetFlexibleDirection( wx.BOTH )
        fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.staticTextConfigOwnVat = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"Own VAT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigOwnVat.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigOwnVat, 0, wx.ALL, 5 )

        self.textCtrlConfigOwnVat = wx.TextCtrl( self.panelConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer31.Add( self.textCtrlConfigOwnVat, 0, wx.ALL, 5 )


        fgSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticTextConfigInterface = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"Interface"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigInterface.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigInterface, 0, wx.ALL, 5 )

        comboBoxConfigInterfaceChoices = [ _(u"vies"), _(u"bzst") ]
        self.comboBoxConfigInterface = wx.ComboBox( self.panelConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxConfigInterfaceChoices, 0 )
        self.comboBoxConfigInterface.SetSelection( 0 )
        fgSizer31.Add( self.comboBoxConfigInterface, 0, wx.ALL, 5 )


        fgSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticTextConfigLanguage = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"Language"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigLanguage.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigLanguage, 0, wx.ALL, 5 )

        comboBoxConfigLanguageChoices = [ _(u"en"), _(u"de") ]
        self.comboBoxConfigLanguage = wx.ComboBox( self.panelConfig, wx.ID_ANY, _(u"Combo!"), wx.DefaultPosition, wx.DefaultSize, comboBoxConfigLanguageChoices, 0 )
        self.comboBoxConfigLanguage.SetSelection( 0 )
        fgSizer31.Add( self.comboBoxConfigLanguage, 0, wx.ALL, 5 )


        fgSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticTextConfigCSVDelimiter = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"CSV delimiter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigCSVDelimiter.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigCSVDelimiter, 0, wx.ALL, 5 )

        self.textConfigCSVdelimiter = wx.TextCtrl( self.panelConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textConfigCSVdelimiter.SetMaxLength( 1 )
        self.textConfigCSVdelimiter.SetMinSize( wx.Size( 20,-1 ) )

        fgSizer31.Add( self.textConfigCSVdelimiter, 0, wx.ALL, 5 )


        fgSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.staticTextConfigLogfile = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"Logfile"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigLogfile.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigLogfile, 0, wx.ALL, 5 )

        self.textCtrlConfigLogfile = wx.TextCtrl( self.panelConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textCtrlConfigLogfile.SetMinSize( wx.Size( 400,-1 ) )

        fgSizer31.Add( self.textCtrlConfigLogfile, 1, wx.ALL|wx.EXPAND, 5 )

        self.buttonConfigLogfile = wx.Button( self.panelConfig, wx.ID_ANY, _(u"Logfile"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer31.Add( self.buttonConfigLogfile, 0, wx.ALL, 5 )

        self.staticTextConfigLogLevel = wx.StaticText( self.panelConfig, wx.ID_ANY, _(u"Loglevel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextConfigLogLevel.Wrap( -1 )

        fgSizer31.Add( self.staticTextConfigLogLevel, 0, wx.ALL, 5 )

        comboBoxConfigLoglevelChoices = [ _(u"DEBUG"), _(u"ERROR") ]
        self.comboBoxConfigLoglevel = wx.ComboBox( self.panelConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxConfigLoglevelChoices, 0 )
        self.comboBoxConfigLoglevel.SetSelection( 1 )
        fgSizer31.Add( self.comboBoxConfigLoglevel, 0, wx.ALL, 5 )


        fgSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.buttonSaveConfig = wx.Button( self.panelConfig, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer31.Add( self.buttonSaveConfig, 0, wx.ALL, 5 )


        self.panelConfig.SetSizer( fgSizer31 )
        self.panelConfig.Layout()
        fgSizer31.Fit( self.panelConfig )
        self.m_notebook3.AddPage( self.panelConfig, _(u"Configuration"), False )

        bSizer4.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 0 )


        bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.mainmenu = wx.MenuBar( 0 )
        self.file = wx.Menu()
        self.menuitemFileClose = wx.MenuItem( self.file, ID_CLOSE, _(u"Close"), _(u"Close VATValidation"), wx.ITEM_NORMAL )
        self.menuitemFileClose.SetBitmap( wx.NullBitmap )
        self.file.Append( self.menuitemFileClose )

        self.mainmenu.Append( self.file, _(u"File") )

        self.help = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem( self.help, ID_GITHUB, _(u"Support..."), _(u"Go to GitHub Repository"), wx.ITEM_NORMAL )
        self.help.Append( self.menuitemHelpSupport )

        self.menuitemHelpUpdate = wx.MenuItem( self.help, wx.ID_ANY, _(u"Check for updates"), wx.EmptyString, wx.ITEM_NORMAL )
        self.help.Append( self.menuitemHelpUpdate )

        self.menuitemHelpAbout = wx.MenuItem( self.help, ID_ABOUT, _(u"About..."), _(u"About VATValidation"), wx.ITEM_NORMAL )
        self.help.Append( self.menuitemHelpAbout )

        self.mainmenu.Append( self.help, _(u"Help") )

        self.SetMenuBar( self.mainmenu )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.loadConfig )
        self.buttonClear.Bind( wx.EVT_BUTTON, self.clearFields )
        self.buttonValidateSingle.Bind( wx.EVT_BUTTON, self.validateSingle )
        self.buttonValidateBatch.Bind( wx.EVT_BUTTON, self.validateBatch )
        self.buttonConfigLogfile.Bind( wx.EVT_BUTTON, self.openLogfile )
        self.buttonSaveConfig.Bind( wx.EVT_BUTTON, self.saveConfig )
        self.Bind( wx.EVT_MENU, self.vatvalidationClose, id = self.menuitemFileClose.GetId() )
        self.Bind( wx.EVT_MENU, self.vatvalidationGitHub, id = self.menuitemHelpSupport.GetId() )
        self.Bind( wx.EVT_MENU, self.checkForUpdates, id = self.menuitemHelpUpdate.GetId() )
        self.Bind( wx.EVT_MENU, self.vatvalidationAbout, id = self.menuitemHelpAbout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def loadConfig( self, event ):
        event.Skip()

    def clearFields( self, event ):
        event.Skip()

    def validateSingle( self, event ):
        event.Skip()

    def validateBatch( self, event ):
        event.Skip()

    def openLogfile( self, event ):
        event.Skip()

    def saveConfig( self, event ):
        event.Skip()

    def vatvalidationClose( self, event ):
        event.Skip()

    def vatvalidationGitHub( self, event ):
        event.Skip()

    def checkForUpdates( self, event ):
        event.Skip()

    def vatvalidationAbout( self, event ):
        event.Skip()


###########################################################################
## Class dialogAbout
###########################################################################

class dialogAbout ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"About VATValidation"), pos = wx.DefaultPosition, size = wx.Size( 240,300 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.bitmapLogo = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.bitmapLogo, 0, wx.ALL, 5 )

        self.staticTextName = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextName.Wrap( -1 )

        bSizer2.Add( self.staticTextName, 0, wx.ALL, 5 )

        self.staticTextLicence = wx.StaticText( self, wx.ID_ANY, _(u"Licenced under"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextLicence.Wrap( -1 )

        bSizer2.Add( self.staticTextLicence, 0, wx.ALL, 5 )

        self.staticTextGithub = wx.StaticText( self, wx.ID_ANY, _(u"More on GitHub"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextGithub.Wrap( -1 )

        self.staticTextGithub.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
        self.staticTextGithub.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.staticTextGithub.SetToolTip( _(u"Visit GitHub repository for further information.") )

        bSizer2.Add( self.staticTextGithub, 0, wx.ALL, 5 )

        self.staticTextIcon8 = wx.StaticText( self, wx.ID_ANY, _(u"Icons by Icons8.com"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextIcon8.Wrap( -1 )

        self.staticTextIcon8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.staticTextIcon8.SetToolTip( _(u"All icons within VATValidation are taken from Icons8") )

        bSizer2.Add( self.staticTextIcon8, 0, wx.ALL, 5 )

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
        self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
        m_sdbSizer2.Realize()

        bSizer2.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.staticTextGithub.Bind( wx.EVT_LEFT_DOWN, self.openGithub )
        self.staticTextIcon8.Bind( wx.EVT_LEFT_DOWN, self.openIcons8 )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def openGithub( self, event ):
        event.Skip()

    def openIcons8( self, event ):
        event.Skip()


