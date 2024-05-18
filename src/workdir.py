# importing wx files
import wx
# import the newly created GUI file
import gui


class WorkDirFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)
        
    def newbuttonCMD1Click(self, event, text=None):
        wx.MessageBox('Implement me 1!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
    def newbuttonCMD2Click(self, event, text=None):
        wx.MessageBox('Implement me 2!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
    def newbuttonCMD3Click(self, event, text=None):
        wx.MessageBox('Implement me 3!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
    def newbuttonCMD4Click(self, event, text=None):
        wx.MessageBox('Implement me 4!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
    def newbuttonCMD5Click(self, event, text=None):
        wx.MessageBox('Implement me 5!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
    def newbuttonCMD6Click(self, event, text=None):
        wx.MessageBox('Implement me 6!' + text,
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)    
    
        
    def workdirClose(self, event):
        self.Close()

    def workdirShow(self, event):
        directories = ['C:\\', 'C:\\temp', 'C:\\Users\\dseichter\\Projects\\dseichter\\Workdir']
        
        fgSizerMain = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizerMain.SetFlexibleDirection(wx.BOTH)
        fgSizerMain.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        # add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizerMain.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)
        
        # add a sizer to the panel
        fgSizerDirectory = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizerDirectory.SetFlexibleDirection(wx.BOTH)
        fgSizerDirectory.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        # add the sizer to the panel
        self.panel.SetSizer(fgSizerDirectory)
        self.panel.Layout()
        fgSizerDirectory.Fit(self.panel)
        
        for directory in directories:
            directoryname = wx.StaticText(self.panel, wx.ID_ANY, directory, wx.DefaultPosition, wx.DefaultSize, 0)
            directoryname.Wrap(-1)
            fgSizerDirectory.Add(directoryname, 1, wx.ALL | wx.EXPAND, 5)
            
            newbuttonCMD1 = wx.Button(self.panel, wx.ID_ANY, u"CMD", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD1.SetToolTip('CMD1')
            newbuttonCMD1.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD1Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD1, 0, wx.ALL, 5)
            
            newbuttonCMD2 = wx.Button(self.panel, wx.ID_ANY, u"GIT BASH", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD2.SetToolTip('CMD2')
            newbuttonCMD2.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD2Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD2, 0, wx.ALL, 5)
            
            newbuttonCMD3 = wx.Button(self.panel, wx.ID_ANY, u"EXPLORER", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD3.SetToolTip('CMD3')
            newbuttonCMD3.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD3Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD3, 0, wx.ALL, 5)
            
            newbuttonCMD4 = wx.Button(self.panel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD4.SetToolTip('CMD4')
            newbuttonCMD4.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD4Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD4, 0, wx.ALL, 5)           
            
            newbuttonCMD5 = wx.Button(self.panel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD5.SetToolTip('CMD5')
            newbuttonCMD5.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD5Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD5, 0, wx.ALL, 5)
            
            newbuttonCMD6 = wx.Button(self.panel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD6.SetToolTip('CMD6')
            newbuttonCMD6.Bind(wx.EVT_BUTTON, lambda event: self.newbuttonCMD6Click(event, text=directory))
            fgSizerDirectory.Add(newbuttonCMD6, 0, wx.ALL, 5)

        self.SetSizer(fgSizerMain)
        self.Layout()
        self.Fit()

        
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = WorkDirFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()