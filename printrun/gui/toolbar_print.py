__author__ = 'yoo'

import wx

from .utils import make_autosize_button

def PrintToolbar(root, parentpanel = None, use_wrapsizer = False):
    if not parentpanel: parentpanel = root.panel

    ToolbarSizer = wx.WrapSizer if use_wrapsizer and wx.VERSION > (2, 9) else wx.BoxSizer
    self = ToolbarSizer(wx.HORIZONTAL)

    if not hasattr(root, "printbtn"):
        root.printbtn = make_autosize_button(parentpanel, _("Print"), root.printfile, _("Start Printing Loaded File"))
        root.statefulControls.append(root.printbtn)
    else:
        root.printbtn.Reparent(parentpanel)
    self.Add(root.printbtn)

    if not hasattr(root, "pausebtn"):
        root.pausebtn = make_autosize_button(parentpanel, _("Pause"), root.pause, _("Pause Current Print"))
        root.statefulControls.append(root.pausebtn)
    else:
        root.pausebtn.Reparent(parentpanel)
    self.Add(root.pausebtn)

    root.offbtn = make_autosize_button(parentpanel, _("Off"), root.off, _("Turn printer off"), self)
    root.printerControls.append(root.offbtn)

    # swyoo 2015.09.08 imsi
    root.dis_ch2 = make_autosize_button(parentpanel, _("View Ch"), root.display_ch, _("View size change"), self)

    return self
