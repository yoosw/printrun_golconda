import wx
import os

from printrun.utils import imagefile

def Print_Control(root, parentpanel):

    if os.name == "nt":
        root.text_loading_file = wx.StaticText(parentpanel, label=str(root.var_loading_file_name), pos=(100, 35))
        root.text_loading_file.SetFont(root.font_20)
    else:
        root.text_loading_file = wx.StaticText(parentpanel, label=str(root.var_loading_file_name), pos=(80, 35))
        root.text_loading_file.SetFont(root.font_24)
    #======================= gauge start
    root.timer = wx.Timer(parentpanel, 1)
    root.count = 0
    root.gauge = wx.Gauge(parentpanel, range=99, pos=(32, 88), size=(456, 27))

    root.Bind(wx.EVT_TIMER, root.TimerHandler)
    root.timer = wx.Timer(root)
    root.timer.Start(100)

    # gauge count
    if os.name == "nt":
        root.text_percentage = wx.StaticText(parentpanel, label=str(root.var_loading_count) + "%", pos=(535, 80))
        root.text_percentage.SetFont(root.font_26)
    else:
        root.text_percentage = wx.StaticText(parentpanel, label=str(root.var_loading_count) + "%", pos=(540, 80))
        root.text_percentage.SetFont(root.font_28)
    #======================= guage end
    # past time
    # bmp_print_home = wx.Bitmap(imagefile("flexor/printing/print_time.png"), wx.BITMAP_TYPE_ANY)

    if os.name == "nt":
        # wx.StaticBitmap(parentpanel, -1, bmp_print_home, (432, 126))
        root.text_printing_time = wx.StaticText(parentpanel, label='00:00:00', pos=(510, 120))
        root.text_printing_time.SetFont(root.font_22)
    else:
        # wx.StaticBitmap(parentpanel, -1, bmp_print_home, (432, 126))
        root.text_printing_time = wx.StaticText(parentpanel, label='00:00:00', pos=(500, 116))
        root.text_printing_time.SetFont(root.font_22)

    # nozle, start
    bmp_print_list = wx.Bitmap(imagefile("flexor/printing/printing_filelist.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_fan_speed_ok = wx.Bitmap(imagefile("flexor/printing/printing_ok.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_start = wx.Bitmap(imagefile("flexor/printing/printing_start.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_start_ch = wx.Bitmap(imagefile("flexor/printing/printing_start_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_stop = wx.Bitmap(imagefile("flexor/printing/printing_stop.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_stop_ch = wx.Bitmap(imagefile("flexor/printing/printing_stop_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_pause = wx.Bitmap(imagefile("flexor/printing/printing_pause.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_resume = wx.Bitmap(imagefile("flexor/printing/printing_resume.png"), wx.BITMAP_TYPE_PNG)
    # root.bmp_print_filament = wx.Bitmap(imagefile("flexor/printing/printing_fila.png"), wx.BITMAP_TYPE_PNG)
    # root.bmp_print_filament_ch = wx.Bitmap(imagefile("flexor/printing/printing_fila_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_emergency = wx.Bitmap(imagefile("flexor/printing/printing_emergency.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_emergency_ch = wx.Bitmap(imagefile("flexor/printing/printing_emergency_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_led = wx.Bitmap(imagefile("flexor/printing/printing_led.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_print_led_ch = wx.Bitmap(imagefile("flexor/printing/printing_led_ch.png"), wx.BITMAP_TYPE_PNG)

    # nozzle1
    # wx.StaticBitmap(parentpanel, -1, bmp_print_nozzle1_temp, (29, 188))
    # if os.name == "nt":
    #     root.text_print_nozzle_temp1_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(98, 200))
    #     root.text_print_nozzle_temp1_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(98, 230))
    #
    # else:
    #     root.text_print_nozzle_temp1_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(96, 200))
    #     root.text_print_nozzle_temp1_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(96, 230))
    # root.text_print_nozzle_temp1_set.SetFont(root.font_18)
    # root.text_print_nozzle_temp1_on.SetFont(root.font_18)
    # root.text_print_nozzle_temp1_set.SetForegroundColour("#748AC5") # set text color
    # root.text_print_nozzle_temp1_on.SetForegroundColour("#ED1D24")

    # nozzle2
    # wx.StaticBitmap(parentpanel, -1, bmp_print_nozzle2_temp, (217, 188))

    # if os.name == "nt":
    #     root.text_print_nozzle_temp2_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(263, 200))
    #     root.text_print_nozzle_temp2_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(263, 230))
    #
    # else:
    #     root.text_print_nozzle_temp2_set = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(258, 200))
    #     root.text_print_nozzle_temp2_on = wx.StaticText(parentpanel, label=("0" + u"\u00B0C"), pos=(258, 230))
    # root.text_print_nozzle_temp2_set.SetFont(root.font_18)
    # root.text_print_nozzle_temp2_on.SetFont(root.font_18)
    # root.text_print_nozzle_temp2_set.SetForegroundColour("#748AC5") # set text color
    # root.text_print_nozzle_temp2_on.SetForegroundColour("#ED1D24")

    # print_speed, pan speed
    # wx.StaticBitmap(parentpanel, -1, bmp_print_print_speed, (22, 320))
    # wx.StaticBitmap(parentpanel, -1, bmp_print_fan_speed, (212, 313))

    # swyoo 2015.09.15 for combobox select
    #======================= combobox start
    root.speed_values = ['50', '75', '100', '125', '150']
    root.select_speed_val = ['50%', '75%', '100%', '125%', '150%']

    root.pan_values = ['0', '80', '102', '153', '204', '255']
    root.select_pan_val = ['OFF', '20%', '40%', '60%', '80%', '100%']

    if os.name == "nt":
        dis_panel = root.bitmap1
    else:
        dis_panel = parentpanel

    if os.name == "nt":
        root.speed_combo = wx.ComboBox(dis_panel, -1, value="100%", pos=(132, 215), size=(80, -1), choices=root.select_speed_val, style=wx.CB_READONLY)
    else:
        root.speed_combo = wx.ComboBox(dis_panel, -1, value="100%", pos=(135, 213), size=(80, -1), choices=root.select_speed_val, style=wx.CB_READONLY)

    if os.name == "nt":
        root.speed_combo.SetFont(root.font_14)
    else:
        root.speed_combo.SetFont(root.font_20)

    if os.name == "nt":
        root.pan_combo = wx.ComboBox(dis_panel, -1, value="100%", pos=(456, 215), size=(80, -1), choices=root.select_pan_val, style=wx.CB_READONLY)
    else:
        root.pan_combo = wx.ComboBox(dis_panel, -1, value="100%", pos=(460, 213), size=(80, -1), choices=root.select_pan_val, style=wx.CB_READONLY)

    if os.name == "nt":
        root.pan_combo.SetFont(root.font_14)
    else:
        root.pan_combo.SetFont(root.font_20)

    btn_bmp_print_fan_speed_ok_1 = wx.BitmapButton(dis_panel, -1, root.bmp_print_fan_speed_ok, (217, 209), style=wx.NO_BORDER)
    btn_bmp_print_fan_speed_ok_1.Bind(wx.EVT_BUTTON, lambda e: root.do_setspeed_flexo())
    btn_bmp_print_fan_speed_ok_2 = wx.BitmapButton(dis_panel, -1, root.bmp_print_fan_speed_ok, (541, 209), style=wx.NO_BORDER)
    btn_bmp_print_fan_speed_ok_2.Bind(wx.EVT_BUTTON, lambda e: root.On_Pan_Select())
    #======================= combobox end

    # start, pause, stop
    if os.name == "nt":
        root.btn_bmp_print_list = wx.BitmapButton(dis_panel, -1, bmp_print_list, (26, 23), style=wx.NO_BORDER)
        root.btn_bmp_print_list.Bind(wx.EVT_BUTTON, root.loadfile)

        root.btn_bmp_print_start = wx.BitmapButton(dis_panel, -1, root.bmp_print_start, (45, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_start.Bind(wx.EVT_BUTTON, root.printfile)

        root.btn_bmp_print_pause = wx.BitmapButton(dis_panel, -1, root.bmp_print_pause, (169, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_pause.Bind(wx.EVT_BUTTON, root.pause)

        root.btn_bmp_print_stop = wx.BitmapButton(dis_panel, -1, root.bmp_print_stop, (295, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_stop.Bind(wx.EVT_BUTTON, root.on_stop)

        # root.btn_bmp_print_filament_ch = wx.BitmapButton(dis_panel, -1, root.bmp_print_filament, (377, 316), style=wx.NO_BORDER)
        # root.btn_bmp_print_filament_ch.Bind(wx.EVT_BUTTON, root.On_Filament_Change)

        root.btn_bmp_print_emergency = wx.BitmapButton(dis_panel, -1, root.bmp_print_emergency, (419, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_emergency.Bind(wx.EVT_BUTTON, root.on_reset)

        root.btn_bmp_print_led = wx.BitmapButton(dis_panel, -1, root.bmp_print_led, (557, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_led.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("led_on"))
    else:
        root.btn_bmp_print_list = wx.BitmapButton(dis_panel, -1, bmp_print_list, (20, 20), style=wx.NO_BORDER)
        root.btn_bmp_print_list.Bind(wx.EVT_BUTTON, root.loadfile)

        root.btn_bmp_print_start = wx.BitmapButton(dis_panel, -1, root.bmp_print_start, (45, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_start.Bind(wx.EVT_BUTTON, root.printfile)

        root.btn_bmp_print_pause = wx.BitmapButton(dis_panel, -1, root.bmp_print_pause, (169, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_pause.Bind(wx.EVT_BUTTON, root.pause)

        root.btn_bmp_print_stop = wx.BitmapButton(dis_panel, -1, root.bmp_print_stop, (295, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_stop.Bind(wx.EVT_BUTTON, root.on_stop)

        # root.btn_bmp_print_filament_ch = wx.BitmapButton(dis_panel, -1, root.bmp_print_filament, (374, 316), style=wx.NO_BORDER)
        # root.btn_bmp_print_filament_ch.Bind(wx.EVT_BUTTON, root.On_Filament_Change)

        root.btn_bmp_print_emergency = wx.BitmapButton(dis_panel, -1, root.bmp_print_emergency, (419, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_emergency.Bind(wx.EVT_BUTTON, root.on_reset)

        root.btn_bmp_print_led = wx.BitmapButton(dis_panel, -1, root.bmp_print_led, (557, 333), style=wx.NO_BORDER)
        root.btn_bmp_print_led.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("led_on"))

    root.text_printing_guide = wx.StaticText(dis_panel, label='printing menu', pos=(21, 441))
    root.text_printing_guide.SetFont(root.font_16)

    return
