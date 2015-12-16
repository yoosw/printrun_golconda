import wx

import os
from .widgets import TempGauge

from printrun.utils import imagefile

def Setting_Control(root, parentpanel):

    mainsizer = wx.BoxSizer(wx.VERTICAL)

    panel_1 = root.newPanel(parentpanel)
    # panel_1.SetBackgroundColour('#FFFFFF')
    panel_2 = root.newPanel(parentpanel)
    # panel_2.SetBackgroundColour('#FFFFFF')

    image_file = "flexor/setting/setting_bg.png"
    bmp_bg = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    background_image = wx.StaticBitmap(panel_1, -1, bmp_bg, (0, 0))

    image_file2 = "flexor/setting/setting_bg2.png"
    bmp_bg2 = wx.Image(imagefile(image_file2), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    background_image2 = wx.StaticBitmap(panel_2, -1, bmp_bg2, (0, 0))

    mainsizer.Add(panel_1, 0, wx.EXPAND)
    mainsizer.Add(panel_2, 0, wx.EXPAND)
    # =============
    bmp_setting_nozzle_down = wx.Bitmap(imagefile("flexor/setting/setting_down.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_nozzle_up = wx.Bitmap(imagefile("flexor/setting/setting_up.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_in = wx.Bitmap(imagefile("flexor/setting/setting_in.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_out = wx.Bitmap(imagefile("flexor/setting/setting_out.png"), wx.BITMAP_TYPE_PNG)

    bmp_setting_on = wx.Bitmap(imagefile("flexor/setting/setting_on.png"), wx.BITMAP_TYPE_PNG)
    bmp_setting_off = wx.Bitmap(imagefile("flexor/setting/setting_off.png"), wx.BITMAP_TYPE_PNG)

    imsi_temp1 = int(root.settings.last_temperature)
    if imsi_temp1 > 0:
        root.var_temp_1_value = imsi_temp1
    imsi_temp2 = int(root.settings.last_bed_temperature)
    if imsi_temp2 > 0:
        root.var_temp_2_value = imsi_temp2

    if os.name == "nt":
        dis_panel = background_image
        dis_panel2 = background_image2
    else:
        dis_panel = panel_1
        dis_panel2 = panel_2

    root.text_temp_1 = wx.StaticText(dis_panel, label=(str(root.var_temp_1_value) + u"\u00B0C"), pos=(178, 92))
    root.text_temp_1.SetFont(root.font_16)
    root.text_temp_2 = wx.StaticText(dis_panel2, label=(str(root.var_temp_2_value) + u"\u00B0C"), pos=(178, 92))
    root.text_temp_2.SetFont(root.font_16)

    if os.name == "nt":
        btn_bmp_setting_nozzle_down1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_down, (125, 82), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_down1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "down"))
        btn_bmp_setting_nozzle_up1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_up, (251, 82), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_up1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "up"))

        btn_bmp_setting_in1 = wx.BitmapButton(dis_panel, -1, bmp_setting_in, (443, 81), style=wx.NO_BORDER)
        btn_bmp_setting_in1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude1"))
        btn_bmp_setting_out1 = wx.BitmapButton(dis_panel, -1, bmp_setting_out, (555, 81), style=wx.NO_BORDER)
        btn_bmp_setting_out1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse1"))

        btn_bmp_setting_nozzle_down2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_nozzle_down, (125, 82), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_down2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "down"))
        btn_bmp_setting_nozzle_up2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_nozzle_up, (251, 82), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_up2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "up"))

        btn_bmp_setting_in2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_in, (443, 81), style=wx.NO_BORDER)
        btn_bmp_setting_in2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude2"))
        btn_bmp_setting_out2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_out, (555, 81), style=wx.NO_BORDER)
        btn_bmp_setting_out2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse2"))
    else:
        btn_bmp_setting_nozzle_down1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_down, (116, 77), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_down1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "down"))
        btn_bmp_setting_nozzle_up1 = wx.BitmapButton(dis_panel, -1, bmp_setting_nozzle_up, (244, 77), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_up1.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_one", "up"))

        btn_bmp_setting_in1 = wx.BitmapButton(dis_panel, -1, bmp_setting_in, (438, 77), style=wx.NO_BORDER)
        btn_bmp_setting_in1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude1"))
        btn_bmp_setting_out1 = wx.BitmapButton(dis_panel, -1, bmp_setting_out, (550, 77), style=wx.NO_BORDER)
        btn_bmp_setting_out1.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse1"))

        btn_bmp_setting_nozzle_down2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_nozzle_down, (116, 77), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_down2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "down"))
        btn_bmp_setting_nozzle_up2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_nozzle_up, (244, 77), style=wx.NO_BORDER)
        btn_bmp_setting_nozzle_up2.Bind(wx.EVT_BUTTON, lambda e: root.temp_ch("head_two", "up"))

        btn_bmp_setting_in2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_in, (443, 77), style=wx.NO_BORDER)
        btn_bmp_setting_in2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Extrude2"))
        btn_bmp_setting_out2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_out, (550, 77), style=wx.NO_BORDER)
        btn_bmp_setting_out2.Bind(wx.EVT_BUTTON, lambda e: root.On_extrude("Reverse2"))

    if os.name == "nt":
        btn_bmp_setting_on1 = wx.BitmapButton(dis_panel, -1, bmp_setting_on, (108, 149), style=wx.NO_BORDER)
        btn_bmp_setting_on1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "on"))
        btn_bmp_setting_off1 = wx.BitmapButton(dis_panel, -1, bmp_setting_off, (561, 149), style=wx.NO_BORDER)
        btn_bmp_setting_off1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "off"))

        btn_bmp_setting_on2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_on, (108, 149), style=wx.NO_BORDER)
        btn_bmp_setting_on2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "on"))
        btn_bmp_setting_off2 = wx.BitmapButton(dis_panel2, -1, bmp_setting_off, (561, 149), style=wx.NO_BORDER)
        btn_bmp_setting_off2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "off"))
    else:
        btn_bmp_setting_on1 = wx.BitmapButton(dis_panel, -1, bmp_setting_on, (108, 142), style=wx.NO_BORDER)
        btn_bmp_setting_on1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "on"))
        btn_bmp_setting_off1 = wx.BitmapButton(dis_panel, -1, bmp_setting_off, (561, 142), style=wx.NO_BORDER)
        btn_bmp_setting_off1.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_one", "off"))

        btn_bmp_setting_on2 = wx.BitmapButton(panel_2, -1, bmp_setting_on, (108, 142), style=wx.NO_BORDER)
        btn_bmp_setting_on2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "on"))
        btn_bmp_setting_off2 = wx.BitmapButton(panel_2, -1, bmp_setting_off, (561, 142), style=wx.NO_BORDER)
        btn_bmp_setting_off2.Bind(wx.EVT_BUTTON, lambda e: root.do_settemp_sec("nozzle_two", "off"))

    temp1_sizer = wx.BoxSizer(wx.HORIZONTAL)
    temp2_sizer = wx.BoxSizer(wx.HORIZONTAL)

    text_left = wx.StaticText(panel_1, label='')
    text_right = wx.StaticText(panel_1, label='')
    text_left2 = wx.StaticText(panel_2, label='')
    text_right2 = wx.StaticText(panel_2, label='')

    if os.name == "nt":
        root.hottgauge = TempGauge(panel_1, size=(364, 28), title=_("Heater1:"), maxval=300, bgcolor='#FFFFFF')
        root.hottgauge2 = TempGauge(panel_2, size=(364, 28), title=_("Heater2:"), maxval=300, bgcolor='#FFFFFF')
        temp1_sizer.Add(text_left, 0, flag=wx.LEFT, border=188)
        temp1_sizer.Add(root.hottgauge, 0, flag=wx.TOP, border=154)
        temp1_sizer.Add(text_right, 0, flag=wx.TOP, border=200)

        temp2_sizer.Add(text_left2, 0, flag=wx.LEFT, border=188)
        temp2_sizer.Add(root.hottgauge2, 0, flag=wx.TOP, border=156)
        temp2_sizer.Add(text_right2, 0, flag=wx.TOP, border=263)
    else:
        root.hottgauge = TempGauge(panel_1, size=(370, 28), title=_("Heater1:"), maxval=300, bgcolor='#FFFFFF')
        root.hottgauge2 = TempGauge(panel_2, size=(370, 28), title=_("Heater2:"), maxval=300, bgcolor='#FFFFFF')
        temp1_sizer.Add(text_left, 0, flag=wx.LEFT, border=188)
        temp1_sizer.Add(root.hottgauge, 0, flag=wx.TOP, border=153)
        temp1_sizer.Add(text_right, 0, flag=wx.TOP, border=200)

        temp2_sizer.Add(text_left2, 0, flag=wx.LEFT, border=188)
        temp2_sizer.Add(root.hottgauge2, 0, flag=wx.TOP, border=156)
        temp2_sizer.Add(text_right2, 0, flag=wx.TOP, border=263)

    root.text_setting_guide = wx.StaticText(panel_2, label='setting menu', pos=(21, 220))
    root.text_setting_guide.SetFont(root.font_16)

    panel_1.SetSizer(temp1_sizer)
    panel_2.SetSizer(temp2_sizer)

    parentpanel.SetSizer(mainsizer)

    return

def Setting_Temp_Gauge_One(root, parentpanel):
    # Temperature gauges #
    temp1_sizer = wx.BoxSizer(wx.HORIZONTAL)

    root.hottgauge = TempGauge(parentpanel, size = (-1, 30), title = _("Heater1:"), maxval = 300, bgcolor = '#E6E7E7')

    text_left = wx.StaticText(parentpanel, label=' ')
    text_right = wx.StaticText(parentpanel, label=' ')

    temp1_sizer.Add(text_left, 0,  flag=wx.LEFT, border=200)
    temp1_sizer.Add(root.hottgauge, 1,  flag=wx.TOP, border=328)
    temp1_sizer.Add(text_right, 0,  flag=wx.LEFT, border=120)

    parentpanel.SetSizer(temp1_sizer)

    return

