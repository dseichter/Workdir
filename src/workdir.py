# importing wx files
import wx
# import the newly created GUI file
import gui


class WorkDirFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)
        
        
    def workdirClose(self, event):
        self.Close()

    def workdirShow(self, event):
        wx.MessageBox('Implement me!',
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        directories = ['C:\\', 'C:\\temp', 'C:\\Users\\dseichter\\Projects\\dseichter\\Workdir']
        
        newpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer1 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer1.AddGrowableCol(0)
        fgSizer1.AddGrowableRow(0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        newpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        
        for directory in directories:
             
            directoryname = wx.StaticText(newpanel, wx.ID_ANY, directory, wx.DefaultPosition, wx.DefaultSize, 0)
            directoryname.Wrap(-1)

            fgSizer1.Add(directoryname, 1, wx.ALL | wx.EXPAND, 5)
            newbuttonCMD1 = wx.Button(newpanel, wx.ID_ANY, u"CMD", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD1, 0, wx.ALL, 5)
            newbuttonCMD2 = wx.Button(newpanel, wx.ID_ANY, u"GIT BASH", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD2, 0, wx.ALL, 5)
            newbuttonCMD3 = wx.Button(newpanel, wx.ID_ANY, u"EXPLORER", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD3, 0, wx.ALL, 5)
            newbuttonCMD4 = wx.Button(newpanel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD4, 0, wx.ALL, 5)
            newbuttonCMD5 = wx.Button(newpanel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD5, 0, wx.ALL, 5)
            newbuttonCMD6 = wx.Button(newpanel, wx.ID_ANY, u"n/a", wx.DefaultPosition, wx.DefaultSize, 0)
            fgSizer1.Add(newbuttonCMD6, 0, wx.ALL, 5)
            
            # self.newpanel.SetSizer(newsizer)
            # self.newpanel.Layout()
            # newsizer.Fit(self.newpanel)
            
            # iterate over all children of the parent
           
            #fgSizer1 = self.GetChildren("fgSizer1").Add(self.newpanel, 1, wx.EXPAND | wx.ALL, 5)
            #fgSizer1.Add(self.newpanel, 1, wx.EXPAND | wx.ALL, 5)
            #self.SetSizer(fgSizer1)
            newpanel.SetSizer(fgSizer1)
            newpanel.Layout()
            fgSizer1.Fit(newpanel)
            

    def buttonCMDclick6(self, event):
        wx.MessageBox('Implement me!',
                      'Info',
                      wx.OK | wx.ICON_INFORMATION)
        
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = WorkDirFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()