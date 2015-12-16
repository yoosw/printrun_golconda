import wx
from .toolbar import MainToolbar
from .toolbar_print import PrintToolbar
from .controls import ControlsSizer, add_extra_controls

def createTabbedGui_sub(root, parentpanel):

    root.mainsizer_help = wx.BoxSizer(wx.VERTICAL)

    panel_1 = root.newPanel(parentpanel)
    panel_2 = root.newPanel(parentpanel)

    if 1: # swyoo 2015.09.01 port, connect, reset etc
        root.toolbarsizer = MainToolbar(root, panel_1, use_wrapsizer = True)
    else:
        root.toolbarsizer = PrintToolbar(root, panel_1, use_wrapsizer=True)

    # panel_1 : print, pause, off
    panel_1.SetSizer(root.toolbarsizer)
    root.mainsizer_help.Add(panel_1, 0, wx.EXPAND)

    # panel_2 => middlesizer
    # leftsizer : motor
    # rightsizer : Heat, Bed, graph, gauge
    root.middlesizer = wx.BoxSizer(wx.HORIZONTAL)
    panel_2.SetSizer(root.middlesizer)

    leftsizer = wx.BoxSizer(wx.VERTICAL)
    controls_sizer = ControlsSizer(root, panel_2, True)
    leftsizer.Add(controls_sizer, 1, wx.ALIGN_CENTER)

    rightsizer = wx.BoxSizer(wx.VERTICAL)
    extracontrols = wx.GridBagSizer()

    add_extra_controls(extracontrols, root, panel_2, controls_sizer.extra_buttons)

    rightsizer.AddStretchSpacer()
    rightsizer.Add(extracontrols, 0, wx.ALIGN_CENTER)

    root.middlesizer.Add(leftsizer, 0, wx.ALIGN_CENTER | wx.RIGHT, border = 10)
    root.middlesizer.Add(rightsizer, 1, wx.ALIGN_CENTER)

    root.mainsizer_help.Add(panel_2, 1)
    parentpanel.SetSizer(root.mainsizer_help)
    return

# swyoo 2015.09.30. create for main ui and printrun ui
def createGui_sub(root, compact = False, mini = False, parentpanel = None):
    root.mainsizer = wx.BoxSizer(wx.VERTICAL)
    root.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
    upperpanel = root.newPanel(parentpanel, False)
    root.toolbarsizer = MainToolbar(root, upperpanel)
    lowerpanel = root.newPanel(parentpanel)
    upperpanel.SetSizer(root.toolbarsizer)
    lowerpanel.SetSizer(root.lowersizer)
    leftpanel = root.newPanel(lowerpanel)

    controls_sizer = ControlsSizer(root, leftpanel, mini_mode=mini)
    leftpanel.SetSizer(controls_sizer)

    root.lowersizer.Add(leftpanel, 0, wx.EXPAND)
    root.mainsizer.Add(upperpanel, 0, wx.EXPAND)
    root.mainsizer.Add(lowerpanel, 1, wx.EXPAND)
    parentpanel.SetSizer(root.mainsizer)
    # parentpanel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
    # self.Bind(wx.EVT_CLOSE, self.kill)

    root.mainsizer.Layout()