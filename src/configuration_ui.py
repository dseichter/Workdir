# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings

class dialogConfiguration(gui.dialogConfiguration):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogConfiguration.__init__(self, parent)
        
    def configurationShow(self, event):
       
        # load the configuration
        directories = settings.load_directories()
        if directories is not None:
            # parse arra of strings into a single string
            directories = '\n'.join(directories)
            self.textCtrlDirectories.SetValue(directories)

        # load the environment variables
        env = settings.load_env_vars()
        if env is not None:
            env = '\n'.join(env)
            self.textCtrlEnvVars.SetValue(env)    
            
        # load the commands
        cmd1 = settings.load_command('CMD1')
        if cmd1 is not None:
            self.textCtrlLabelCMD1.SetValue(cmd1['label'])
            self.textCtrlCommandCMD1.SetValue(cmd1['command'])
            self.textCtrlParameterCMD1.SetValue(cmd1['parameters'])
            self.checkBoxConfirmCMD1.SetValue(cmd1['use_env'])
            self.checkBoxEnvVarCMD1.SetValue(cmd1['confirmation'])
            #self.colourPickerCMD1.SetColour(cmd1['colour'])

    def configurationSave(self, event):
        # save the configuration
        directories = {}
        
        # save textCtrlDirectories into array of strings
        directories = self.textCtrlDirectories.GetValue().split('\n')
        settings.save_directories(directories)
        
        env = {}
        env = self.textCtrlEnvVars.GetValue().split('\n')
        settings.save_env_vars(env)
        
        cmd1 = {}
        cmd1['label'] = self.textCtrlLabelCMD1.GetValue()
        cmd1['command'] = self.textCtrlCommandCMD1.GetValue()
        cmd1['parameters'] = self.textCtrlParameterCMD1.GetValue()
        cmd1['use_env'] = self.checkBoxConfirmCMD1.GetValue()
        cmd1['confirmation'] = self.checkBoxEnvVarCMD1.GetValue()
        #cmd1['colour'] = self.colourPickerCMD1.GetColour()
        settings.save_command('CMD1', cmd1)
        
        
        
        