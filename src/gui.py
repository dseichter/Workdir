# -*- coding: utf-8 -*-

# #########################################################################
# # Python code generated with wxFormBuilder (version 4.1.0-69d57cd9)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
# #########################################################################

import wx
import wx.xrc

ID_CLOSE = 1000
ID_CONFIGURATION = 1001
ID_GET_HELP = 1002
ID_CHECK_FOR_UPDATES = 1003
ID_ABOUT = 1004


# #########################################################################
# # Class MainFrame
# #########################################################################


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Workdir", pos=wx.DefaultPosition, size=wx.Size(660, 387), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.menuitemFile = wx.Menu()
        self.menuitemFileClose = wx.MenuItem(self.menuitemFile, ID_CLOSE, u"Close", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemFile.Append(self.menuitemFileClose)

        self.m_menubar1.Append(self.menuitemFile, u"File")

        self.menuItemExtras = wx.Menu()
        self.menuitemExtrasConfiguration = wx.MenuItem(self.menuItemExtras, ID_CONFIGURATION, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuItemExtras.Append(self.menuitemExtrasConfiguration)

        self.m_menubar1.Append(self.menuItemExtras, u"Extras")

        self.menuitemHelp = wx.Menu()
        self.menuitemHelpSupport = wx.MenuItem(self.menuitemHelp, ID_GET_HELP, u"Support...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpSupport)

        self.menuitemHelpUpdate = wx.MenuItem(self.menuitemHelp, ID_CHECK_FOR_UPDATES, u"Check for updates", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpUpdate)

        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About...", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.workdirClose)
        self.Bind(wx.EVT_SHOW, self.workdirShow)
        self.Bind(wx.EVT_MENU, self.miFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.miExtrasConfiguration, id=self.menuitemExtrasConfiguration.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpSupport, id=self.menuitemHelpSupport.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpUpdate, id=self.menuitemHelpUpdate.GetId())
        self.Bind(wx.EVT_MENU, self.miHelpAbout, id=self.menuitemHelpAbout.GetId())

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def workdirClose(self, event):
        event.Skip()

    def workdirShow(self, event):
        event.Skip()

    def miFileClose(self, event):
        event.Skip()

    def miExtrasConfiguration(self, event):
        event.Skip()

    def miHelpSupport(self, event):
        event.Skip()

    def miHelpUpdate(self, event):
        event.Skip()

    def miHelpAbout(self, event):
        event.Skip()

# #########################################################################
# # Class dialogConfiguration
# #########################################################################


class dialogConfiguration(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Configuration", pos=wx.DefaultPosition, size=wx.Size(901, 546), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer6 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)


        fgSizer6.Add((0, 0), 1, wx.EXPAND, 5)
        self.staticTextLabel = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextLabel.Wrap(-1)

        fgSizer6.Add(self.staticTextLabel, 0, wx.ALL, 5)
        self.staticTextCommand = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCommand.Wrap(-1)

        fgSizer6.Add(self.staticTextCommand, 0, wx.ALL, 5)
        self.staticTextParameter = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Parameter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextParameter.Wrap(-1)

        fgSizer6.Add(self.staticTextParameter, 0, wx.ALL, 5)
        self.staticTextConfirmation = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Confirmation?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextConfirmation.Wrap(-1)

        fgSizer6.Add(self.staticTextConfirmation, 0, wx.ALL, 5)
        self.staticTextEnvVar = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Env Var?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextEnvVar.Wrap(-1)

        fgSizer6.Add(self.staticTextEnvVar, 0, wx.ALL, 5)
        self.staticTextFontColor = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Font color", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextFontColor.Wrap(-1)

        fgSizer6.Add(self.staticTextFontColor, 0, wx.ALL, 5)
        self.staticTextCMD1 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD1.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD1, 0, wx.ALL, 5)
        self.textCtrlLabelCMD1 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD1, 0, wx.ALL, 5)
        self.textCtrlCommandCMD1 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD1, 0, wx.ALL, 5)
        self.textCtrlParameterCMD1 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD1, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD1 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD1, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD1 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD1, 0, wx.ALL, 5)
        self.colourPickerCMD1 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD1, 0, wx.ALL, 5)
        self.staticTextCMD2 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD2.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD2, 0, wx.ALL, 5)
        self.textCtrlLabelCMD2 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD2, 0, wx.ALL, 5)
        self.textCtrlCommandCMD2 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD2, 0, wx.ALL, 5)
        self.textCtrlParameterCMD2 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD2, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD2 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD2, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD2 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD2, 0, wx.ALL, 5)
        self.colourPickerCMD2 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD2, 0, wx.ALL, 5)
        self.staticTextCMD3 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD3.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD3, 0, wx.ALL, 5)
        self.textCtrlLabelCMD3 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD3, 0, wx.ALL, 5)
        self.textCtrlCommandCMD3 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD3, 0, wx.ALL, 5)
        self.textCtrlParameterCMD3 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD3, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD3 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD3, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD3 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD3, 0, wx.ALL, 5)
        self.colourPickerCMD3 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD3, 0, wx.ALL, 5)
        self.staticTextCMD4 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD4.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD4, 0, wx.ALL, 5)
        self.textCtrlLabelCMD4 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD4, 0, wx.ALL, 5)
        self.textCtrlCommandCMD4 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD4, 0, wx.ALL, 5)
        self.textCtrlParameterCMD4 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD4, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD4 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD4, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD4 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD4, 0, wx.ALL, 5)
        self.colourPickerCMD4 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD4, 0, wx.ALL, 5)
        self.staticTextCMD5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD5.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD5, 0, wx.ALL, 5)
        self.textCtrlLabelCMD5 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD5, 0, wx.ALL, 5)
        self.textCtrlCommandCMD5 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD5, 0, wx.ALL, 5)
        self.textCtrlParameterCMD5 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD5, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD5 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD5, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD5 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD5, 0, wx.ALL, 5)
        self.colourPickerCMD5 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD5, 0, wx.ALL, 5)
        self.staticTextCMD6 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"CMD6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCMD6.Wrap(-1)

        fgSizer6.Add(self.staticTextCMD6, 0, wx.ALL, 5)
        self.textCtrlLabelCMD6 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlLabelCMD6, 0, wx.ALL, 5)
        self.textCtrlCommandCMD6 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlCommandCMD6, 0, wx.ALL, 5)
        self.textCtrlParameterCMD6 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.textCtrlParameterCMD6, 0, wx.ALL, 5)
        self.checkBoxConfirmCMD6 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxConfirmCMD6, 0, wx.ALL, 5)
        self.checkBoxEnvVarCMD6 = wx.CheckBox(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.checkBoxEnvVarCMD6, 0, wx.ALL, 5)
        self.colourPickerCMD6 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.colourPickerCMD6, 0, wx.ALL, 5)
        self.m_panel5.SetSizer(fgSizer6)
        self.m_panel5.Layout()
        fgSizer6.Fit(self.m_panel5)
        bSizer1.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(0)
        fgSizer2.AddGrowableRow(1)
        fgSizer2.SetFlexibleDirection(wx.VERTICAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.staticTextDirectories = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Directories", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextDirectories.Wrap(-1)

        fgSizer2.Add(self.staticTextDirectories, 1, wx.ALL | wx.EXPAND, 5)
        self.staticTextEnvVar1 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Environment Variables", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextEnvVar1.Wrap(-1)

        fgSizer2.Add(self.staticTextEnvVar1, 1, wx.ALL | wx.EXPAND, 5)
        self.textCtrlDirectories = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        fgSizer2.Add(self.textCtrlDirectories, 1, wx.ALL | wx.EXPAND, 5)
        self.textCtrlEnvVars = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        fgSizer2.Add(self.textCtrlEnvVars, 1, wx.ALL | wx.EXPAND, 5)
        self.staticTextDirectoriesNotes = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Add one directory each line. If a directory is not available, no commands will be enabled.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextDirectoriesNotes.Wrap(-1)

        fgSizer2.Add(self.staticTextDirectoriesNotes, 1, wx.ALL | wx.EXPAND, 5)
        self.staticTextEnvVarNotes = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Add one Key/Pair (Key=Value) in each line to provide as environment variable.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextEnvVarNotes.Wrap(-1)

        fgSizer2.Add(self.staticTextEnvVarNotes, 1, wx.ALL | wx.EXPAND, 5)
        self.m_panel3.SetSizer(fgSizer2)
        self.m_panel3.Layout()
        fgSizer2.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2Save = wx.Button(self, wx.ID_SAVE)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Save)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer1.Add(m_sdbSizer2, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SHOW, self.configurationShow)
        self.m_sdbSizer2Save.Bind(wx.EVT_BUTTON, self.configurationSave)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def configurationShow(self, event):
        event.Skip()

    def configurationSave(self, event):
        event.Skip()

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About Workdir", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bitmapLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.bitmapLogo, 0, wx.ALL, 5)
        self.staticTextName = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextName.Wrap(-1)

        bSizer2.Add(self.staticTextName, 0, wx.ALL, 5)
        self.staticTextLicence = wx.StaticText(self, wx.ID_ANY, u"Licenced under", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextLicence.Wrap(-1)

        bSizer2.Add(self.staticTextLicence, 0, wx.ALL, 5)
        self.staticTextGithub = wx.StaticText(self, wx.ID_ANY, u"More on GitHub", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextGithub.Wrap(-1)

        self.staticTextGithub.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString))
        self.staticTextGithub.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer2.Add(self.staticTextGithub, 0, wx.ALL, 5)
        self.staticTextIcon8 = wx.StaticText(self, wx.ID_ANY, u"Icons by Icons8.com", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextIcon8.Wrap(-1)

        self.staticTextIcon8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        bSizer2.Add(self.staticTextIcon8, 0, wx.ALL, 5)
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()
        bSizer2.Add(m_sdbSizer2, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.staticTextGithub.Bind(wx.EVT_LEFT_DOWN, self.openGithub)
        self.staticTextIcon8.Bind(wx.EVT_LEFT_DOWN, self.openIcons8)

    def __del__(self):
        pass
    # Virtual event handlers, override them in your derived class

    def openGithub(self, event):
        event.Skip()

    def openIcons8(self, event):
        event.Skip()
