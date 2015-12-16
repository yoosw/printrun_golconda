__author__ = 'yoo'

import wx

import os
from .utils import make_autosize_button

# swyoo 2015.08.31 for image display in linux
from printrun.utils import imagefile

def HomeToolbar(root, parentpanel=None, use_wrapsizer=False):
    if not parentpanel: parentpanel = root.panel

    ToolbarSizer = wx.WrapSizer if use_wrapsizer and wx.VERSION > (2, 9) else wx.BoxSizer
    self = ToolbarSizer(wx.HORIZONTAL)

    image_file = "flexor/home/main_bg.png"
    bmp_bg = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    background_image = wx.StaticBitmap(parentpanel, -1, bmp_bg, (0, 0))

    if os.name == "nt":
        dis_panel = background_image
    else:
        dis_panel = parentpanel

    # swyoo remove and open at original control
    if 0:  #os.name == "nt":
        root.rescanbtn = make_autosize_button(dis_panel, _("Port"), root.rescanports,
                                              _("Communication Settings\nClick to rescan ports"))
        # self.Add(root.rescanbtn, 0, wx.TOP | wx.LEFT, 10)
        self.Add(root.rescanbtn, 0, wx.TOP | wx.LEFT, 20)

        root.serialport = wx.ComboBox(dis_panel, -1, choices=root.scanserial(),
                                      style=wx.CB_DROPDOWN)
        root.serialport.SetToolTip(wx.ToolTip(_("Select Port Printer is connected to")))
        root.rescanports()
        self.Add(root.serialport, 0, wx.TOP | wx.LEFT, 10)
        root.baud = 115200

        root.dis_ch1 = make_autosize_button(dis_panel, _("View Ch"), root.display_ch, _("View size change"))
        self.Add(root.dis_ch1, 0, wx.TOP | wx.LEFT, 10)

    ########################################################################
    root.bmp_home_connect = wx.Bitmap(imagefile("flexor/home/main_connect.png"), wx.BITMAP_TYPE_ANY)
    root.bmp_home_connected = wx.Bitmap(imagefile("flexor/home/main_connected.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_filelist = wx.Bitmap(imagefile("flexor/home/main_filelist.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_control = wx.Bitmap(imagefile("flexor/home/main_control.png"), wx.BITMAP_TYPE_ANY)
    bmp_home_setting = wx.Bitmap(imagefile("flexor/home/main_help.png"), wx.BITMAP_TYPE_ANY)

    btn_bmp_home_filelist = wx.BitmapButton(dis_panel, -1, bmp_home_filelist, (52, 128), style=wx.NO_BORDER)
    btn_bmp_home_filelist.Bind(wx.EVT_BUTTON, root.loadfile)
    btn_bmp_home_control = wx.BitmapButton(dis_panel, -1, bmp_home_control, (267, 141), style=wx.NO_BORDER)
    btn_bmp_home_control.Bind(wx.EVT_BUTTON, lambda e: root.switch_tab(2))
    btn_bmp_home_setting = wx.BitmapButton(dis_panel, -1, bmp_home_setting, (459, 136), style=wx.NO_BORDER)
    btn_bmp_home_setting.Bind(wx.EVT_BUTTON, lambda e: root.switch_tab(3))
    if os.name == "nt":
        root.btn_bmp_home_connect = wx.BitmapButton(dis_panel, -1, root.bmp_home_connect, (408, 385), style=wx.NO_BORDER)
    else:
        root.btn_bmp_home_connect = wx.BitmapButton(dis_panel, -1, root.bmp_home_connect, (406, 383), style=wx.NO_BORDER)
    root.btn_bmp_home_connect.Bind(wx.EVT_BUTTON, root.connect)
    ########################################################################

    return self
