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
ID_ABOUT = 1002


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
        self.menuitemHelpAbout = wx.MenuItem(self.menuitemHelp, ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuitemHelp.Append(self.menuitemHelpAbout)

        self.m_menubar1.Append(self.menuitemHelp, u"Help")

        self.SetMenuBar(self.m_menubar1)

        fgSizer1 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer1.AddGrowableCol(0)
        fgSizer1.AddGrowableRow(0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.SetSizer(fgSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.workdirClose)
        self.Bind(wx.EVT_SHOW, self.workdirShow)
        self.Bind(wx.EVT_MENU, self.miFileClose, id=self.menuitemFileClose.GetId())
        self.Bind(wx.EVT_MENU, self.miExtrasConfiguration, id=self.menuitemExtrasConfiguration.GetId())
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

    def miHelpAbout(self, event):
        event.Skip()

# #########################################################################
# # Class dialogConfiguration
# #########################################################################


class dialogConfiguration(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Configuration", pos=wx.DefaultPosition, size=wx.Size(876, 483), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer6 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)


        fgSizer6.Add((0, 0), 1, wx.EXPAND, 5)
        self.m_staticText2 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)
        self.m_staticText3 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        fgSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)
        self.m_staticText4 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer6.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_staticText5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer6.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_staticText6 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        fgSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)
        self.m_staticText7 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        fgSizer6.Add(self.m_staticText7, 0, wx.ALL, 5)
        self.m_staticText8 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        fgSizer6.Add(self.m_staticText8, 0, wx.ALL, 5)
        self.m_textCtrl1 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        self.m_textCtrl2 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        self.m_textCtrl3 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        self.m_checkBox1 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox1, 0, wx.ALL, 5)
        self.m_checkBox2 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox2, 0, wx.ALL, 5)
        self.m_colourPicker1 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker1, 0, wx.ALL, 5)
        self.m_staticText9 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        fgSizer6.Add(self.m_staticText9, 0, wx.ALL, 5)
        self.m_textCtrl4 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        self.m_textCtrl5 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl5, 0, wx.ALL, 5)
        self.m_textCtrl6 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        self.m_checkBox3 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox3, 0, wx.ALL, 5)
        self.m_checkBox4 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox4, 0, wx.ALL, 5)
        self.m_colourPicker2 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker2, 0, wx.ALL, 5)
        self.m_staticText10 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        fgSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)
        self.m_textCtrl7 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        self.m_textCtrl8 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl8, 0, wx.ALL, 5)
        self.m_textCtrl9 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl9, 0, wx.ALL, 5)
        self.m_checkBox5 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox5, 0, wx.ALL, 5)
        self.m_checkBox6 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox6, 0, wx.ALL, 5)
        self.m_colourPicker3 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker3, 0, wx.ALL, 5)
        self.m_staticText11 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        fgSizer6.Add(self.m_staticText11, 0, wx.ALL, 5)
        self.m_textCtrl10 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl10, 0, wx.ALL, 5)
        self.m_textCtrl11 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl11, 0, wx.ALL, 5)
        self.m_textCtrl12 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl12, 0, wx.ALL, 5)
        self.m_checkBox7 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox7, 0, wx.ALL, 5)
        self.m_checkBox8 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox8, 0, wx.ALL, 5)
        self.m_colourPicker4 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker4, 0, wx.ALL, 5)
        self.m_staticText12 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        fgSizer6.Add(self.m_staticText12, 0, wx.ALL, 5)
        self.m_textCtrl13 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl13, 0, wx.ALL, 5)
        self.m_textCtrl14 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl14, 0, wx.ALL, 5)
        self.m_textCtrl15 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl15, 0, wx.ALL, 5)
        self.m_checkBox9 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox9, 0, wx.ALL, 5)
        self.m_checkBox10 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox10, 0, wx.ALL, 5)
        self.m_colourPicker5 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker5, 0, wx.ALL, 5)
        self.m_staticText13 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        fgSizer6.Add(self.m_staticText13, 0, wx.ALL, 5)
        self.m_textCtrl16 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl16, 0, wx.ALL, 5)
        self.m_textCtrl17 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl17, 0, wx.ALL, 5)
        self.m_textCtrl18 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_textCtrl18, 0, wx.ALL, 5)
        self.m_checkBox11 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox11, 0, wx.ALL, 5)
        self.m_checkBox12 = wx.CheckBox(self.m_panel5, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.m_checkBox12, 0, wx.ALL, 5)
        self.m_colourPicker6 = wx.ColourPickerCtrl(self.m_panel5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer6.Add(self.m_colourPicker6, 0, wx.ALL, 5)
        self.m_panel5.SetSizer(fgSizer6)
        self.m_panel5.Layout()
        fgSizer6.Fit(self.m_panel5)
        bSizer1.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText14 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        gSizer1.Add(self.m_staticText14, 0, wx.ALL, 5)
        self.m_staticText15 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        gSizer1.Add(self.m_staticText15, 0, wx.ALL, 5)
        self.m_textCtrl20 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        gSizer1.Add(self.m_textCtrl20, 0, wx.ALL, 5)
        self.m_textCtrl21 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE)
        gSizer1.Add(self.m_textCtrl21, 0, wx.ALL, 5)
        self.m_staticText16 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        gSizer1.Add(self.m_staticText16, 0, wx.ALL, 5)
        self.m_staticText17 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        gSizer1.Add(self.m_staticText17, 0, wx.ALL, 5)
        self.m_panel3.SetSizer(gSizer1)
        self.m_panel3.Layout()
        gSizer1.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass

# #########################################################################
# # Class dialogAbout
# #########################################################################


class dialogAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About Workdir", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
