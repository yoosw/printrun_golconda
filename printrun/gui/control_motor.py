import wx
import os

from printrun.utils import imagefile

def Motor_Control(root, parentpanel):

    # motor image
    bmp_motor_x_box = wx.Bitmap(imagefile("flexor/motor/motor_x.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y_box = wx.Bitmap(imagefile("flexor/motor/motor_y.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z_box = wx.Bitmap(imagefile("flexor/motor/motor_z.png"), wx.BITMAP_TYPE_PNG)
    bmp_zoffset = wx.Bitmap(imagefile("flexor/motor/motor_zoffset.png"), wx.BITMAP_TYPE_PNG)

    root.bmp_motor_x_arrow1 = wx.Bitmap(imagefile("flexor/motor/motor_xarrow1.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_x_arrow1_ch = wx.Bitmap(imagefile("flexor/motor/motor_xarrow1_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_x_arrow2 = wx.Bitmap(imagefile("flexor/motor/motor_xarrow2.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_x_arrow2_ch = wx.Bitmap(imagefile("flexor/motor/motor_xarrow2_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_y_arrow1 = wx.Bitmap(imagefile("flexor/motor/motor_yarrow1.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_y_arrow1_ch = wx.Bitmap(imagefile("flexor/motor/motor_yarrow1_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_y_arrow2 = wx.Bitmap(imagefile("flexor/motor/motor_yarrow2.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_y_arrow2_ch = wx.Bitmap(imagefile("flexor/motor/motor_yarrow2_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_z_arrow1 = wx.Bitmap(imagefile("flexor/motor/motor_zarrow1.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_z_arrow1_ch = wx.Bitmap(imagefile("flexor/motor/motor_zarrow1_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_z_arrow2 = wx.Bitmap(imagefile("flexor/motor/motor_zarrow2.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_z_arrow2_ch = wx.Bitmap(imagefile("flexor/motor/motor_zarrow2_ch.png"), wx.BITMAP_TYPE_PNG)

    root.bmp_motor_auto = wx.Bitmap(imagefile("flexor/motor/motor_auto.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_off = wx.Bitmap(imagefile("flexor/motor/motor_off.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_bobbin_in = wx.Bitmap(imagefile("flexor/motor/motor_bobbin_in.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_bobbin_out = wx.Bitmap(imagefile("flexor/motor/motor_bobbin_out.png"), wx.BITMAP_TYPE_PNG)

    bmp_motor_x_home = wx.Bitmap(imagefile("flexor/motor/motor_xhome.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_y_home = wx.Bitmap(imagefile("flexor/motor/motor_yhome.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_z_home = wx.Bitmap(imagefile("flexor/motor/motor_zhome.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_0 = wx.Bitmap(imagefile("flexor/motor/motor_0.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_1 = wx.Bitmap(imagefile("flexor/motor/motor_1.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_10 = wx.Bitmap(imagefile("flexor/motor/motor_10.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_0_ch = wx.Bitmap(imagefile("flexor/motor/motor_0_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_1_ch = wx.Bitmap(imagefile("flexor/motor/motor_1_ch.png"), wx.BITMAP_TYPE_PNG)
    root.bmp_motor_10_ch = wx.Bitmap(imagefile("flexor/motor/motor_10_ch.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_xyz_home = wx.Bitmap(imagefile("flexor/motor/motor_autohome.png"), wx.BITMAP_TYPE_PNG)
    bmp_motor_stop = wx.Bitmap(imagefile("flexor/motor/motor_motorstop.png"), wx.BITMAP_TYPE_PNG)

    # image connect
    if os.name == "nt":
        root.text_motor_x_position = wx.StaticText(parentpanel, label=':0.0', pos=(102, 34))
        root.text_motor_x_position.SetFont(root.font_26)
    else:
        root.text_motor_x_position = wx.StaticText(parentpanel, label=':0.0', pos=(88, 34))
        root.text_motor_x_position.SetFont(root.font_28)
    root.text_motor_x_position.SetForegroundColour("#EB2526")

    if os.name == "nt":
        root.text_motor_y_position = wx.StaticText(parentpanel, label=':0.0', pos=(102, 96))
        root.text_motor_y_position.SetFont(root.font_26)
    else:
        root.text_motor_y_position = wx.StaticText(parentpanel, label=':0.0', pos=(88, 96))
        root.text_motor_y_position.SetFont(root.font_28)
    root.text_motor_y_position.SetForegroundColour("#47B648")

    if os.name == "nt":
        root.text_motor_z_position = wx.StaticText(parentpanel, label=':0.0', pos=(102, 159))
        root.text_motor_z_position.SetFont(root.font_26)
    else:
        root.text_motor_z_position = wx.StaticText(parentpanel, label=':0.0', pos=(88, 159))
        root.text_motor_z_position.SetFont(root.font_28)
    root.text_motor_z_position.SetForegroundColour("#2F4A91")

    imsi_zoffset = float(root.build_dimensions_list[5])
    if imsi_zoffset < 0:
        imsi_zoffset = -imsi_zoffset
    if os.name == "nt":
        root.text_zoffset = wx.StaticText(parentpanel, label=':' + str(imsi_zoffset), pos=(151, 223))
        root.text_zoffset.SetFont(root.font_26)
    else:
        root.text_zoffset = wx.StaticText(parentpanel, label=':' + str(imsi_zoffset), pos=(138, 223))
        root.text_zoffset.SetFont(root.font_26)

    # motor
    if os.name == "nt":
        dis_panel = root.bitmap2
    else:
        dis_panel = parentpanel

    if os.name == "nt":
        btn_bmp_motor_x_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_x_box, (47, 27), style=wx.NO_BORDER)
        btn_bmp_motor_x_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("x"))
        btn_bmp_motor_y_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_y_box, (47, 89), style=wx.NO_BORDER)
        btn_bmp_motor_y_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("y"))
        btn_bmp_motor_z_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_z_box, (47, 152), style=wx.NO_BORDER)
        btn_bmp_motor_z_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("z"))
        btn_bmp_zoffset_cal = wx.BitmapButton(dis_panel, -1, bmp_zoffset, (47, 215), style=wx.NO_BORDER)
        btn_bmp_zoffset_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("zoffset"))
    else:
        btn_bmp_motor_x_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_x_box, (30, 27), style=wx.NO_BORDER)
        btn_bmp_motor_x_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("x"))
        btn_bmp_motor_y_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_y_box, (30, 89), style=wx.NO_BORDER)
        btn_bmp_motor_y_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("y"))
        btn_bmp_motor_z_cal = wx.BitmapButton(dis_panel, -1, bmp_motor_z_box, (30, 152), style=wx.NO_BORDER)
        btn_bmp_motor_z_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("z"))
        btn_bmp_zoffset_cal = wx.BitmapButton(dis_panel, -1, bmp_zoffset, (30, 215), style=wx.NO_BORDER)
        btn_bmp_zoffset_cal.Bind(wx.EVT_BUTTON, lambda e: root.load_calculator_motor("zoffset"))

    if os.name == "nt":
        root.btn_bmp_motor_x_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_x_arrow1_ch, (296, 113), style=wx.NO_BORDER)
        root.btn_bmp_motor_x_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("x", -1))

        root.btn_bmp_motor_x_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_x_arrow2, (482, 115), style=wx.NO_BORDER)
        root.btn_bmp_motor_x_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("x", 1))

        root.btn_bmp_motor_y_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_y_arrow1, (390, 27), style=wx.NO_BORDER)
        root.btn_bmp_motor_y_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("y", -1))

        root.btn_bmp_motor_y_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_y_arrow2, (390, 202), style=wx.NO_BORDER)
        root.btn_bmp_motor_y_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("y", 1))

        root.btn_bmp_motor_z_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_z_arrow1, (555, 22), style=wx.NO_BORDER)
        root.btn_bmp_motor_z_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("z", 1))

        root.btn_bmp_motor_z_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_z_arrow2, (555, 199), style=wx.NO_BORDER)
        root.btn_bmp_motor_z_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("z", -1))
    else:
        root.btn_bmp_motor_x_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_x_arrow1_ch, (296, 113), style=wx.NO_BORDER)
        root.btn_bmp_motor_x_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("x", -1))

        root.btn_bmp_motor_x_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_x_arrow2, (482, 115), style=wx.NO_BORDER)
        root.btn_bmp_motor_x_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("x", 1))

        root.btn_bmp_motor_y_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_y_arrow1, (390, 24), style=wx.NO_BORDER)
        root.btn_bmp_motor_y_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("y", -1))

        root.btn_bmp_motor_y_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_y_arrow2, (390, 198), style=wx.NO_BORDER)
        root.btn_bmp_motor_y_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("y", 1))

        root.btn_bmp_motor_z_arrow1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_z_arrow1, (555, 22), style=wx.NO_BORDER)
        root.btn_bmp_motor_z_arrow1.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("z", 1))

        root.btn_bmp_motor_z_arrow2 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_z_arrow2, (555, 195), style=wx.NO_BORDER)
        root.btn_bmp_motor_z_arrow2.Bind(wx.EVT_BUTTON, lambda e: root.move_unit_distance("z", -1))

    if os.name == "nt":
        root.btn_bmp_motor_auto = wx.BitmapButton(dis_panel, -1, root.bmp_motor_off, (94, 312), style=wx.NO_BORDER)
        root.btn_bmp_motor_auto.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_auto_on"))
        root.btn_bmp_motor_bobbin_in = wx.BitmapButton(dis_panel, -1, bmp_motor_bobbin_in, (94, 373), style=wx.NO_BORDER)
        root.btn_bmp_motor_bobbin_in.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_forward"))
        root.btn_bmp_motor_bobbin_out = wx.BitmapButton(dis_panel, -1, bmp_motor_bobbin_out, (148, 373), style=wx.NO_BORDER)
        root.btn_bmp_motor_bobbin_out.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_reverse"))

        btn_bmp_motor_x_home = wx.BitmapButton(dis_panel, -1, bmp_motor_x_home, (240, 307), style=wx.NO_BORDER)
        btn_bmp_motor_x_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("x"))
        btn_bmp_motor_y_home = wx.BitmapButton(dis_panel, -1, bmp_motor_y_home, (319, 307), style=wx.NO_BORDER)
        btn_bmp_motor_y_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("y"))
        btn_bmp_motor_z_home = wx.BitmapButton(dis_panel, -1, bmp_motor_z_home, (397, 307), style=wx.NO_BORDER)
        btn_bmp_motor_z_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("z"))

        root.btn_bmp_motor_0 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_0, (246, 373), style=wx.NO_BORDER)
        root.btn_bmp_motor_0.Bind(wx.EVT_BUTTON, lambda e: root.move_set(0.1))
        root.btn_bmp_motor_1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_1_ch, (325, 373), style=wx.NO_BORDER)
        root.btn_bmp_motor_1.Bind(wx.EVT_BUTTON, lambda e: root.move_set(1))
        root.btn_bmp_motor_10 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_10, (403, 373), style=wx.NO_BORDER)
        root.btn_bmp_motor_10.Bind(wx.EVT_BUTTON, lambda e: root.move_set(10))

        btn_bmp_motor_xyz_home = wx.BitmapButton(dis_panel, -1, bmp_motor_xyz_home, (483, 312), style=wx.NO_BORDER)
        btn_bmp_motor_xyz_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("all"))
        btn_bmp_motor_stop = wx.BitmapButton(dis_panel, -1, bmp_motor_stop, (483, 373), style=wx.NO_BORDER)
        btn_bmp_motor_stop.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("Motors off"))
    else:
        root.btn_bmp_motor_auto = wx.BitmapButton(dis_panel, -1, root.bmp_motor_off, (90, 305), style=wx.NO_BORDER)
        root.btn_bmp_motor_auto.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_auto_on"))
        root.btn_bmp_motor_bobbin_in = wx.BitmapButton(dis_panel, -1, bmp_motor_bobbin_in, (90, 367), style=wx.NO_BORDER)
        root.btn_bmp_motor_bobbin_in.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_forward"))
        root.btn_bmp_motor_bobbin_out = wx.BitmapButton(dis_panel, -1, bmp_motor_bobbin_out, (144, 367), style=wx.NO_BORDER)
        root.btn_bmp_motor_bobbin_out.Bind(wx.EVT_BUTTON, lambda e: root.gpio_control("motor_reverse"))

        btn_bmp_motor_x_home = wx.BitmapButton(dis_panel, -1, bmp_motor_x_home, (240, 302), style=wx.NO_BORDER)
        btn_bmp_motor_x_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("x"))
        btn_bmp_motor_y_home = wx.BitmapButton(dis_panel, -1, bmp_motor_y_home, (319, 302), style=wx.NO_BORDER)
        btn_bmp_motor_y_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("y"))
        btn_bmp_motor_z_home = wx.BitmapButton(dis_panel, -1, bmp_motor_z_home, (397, 302), style=wx.NO_BORDER)
        btn_bmp_motor_z_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("z"))

        root.btn_bmp_motor_0 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_0, (246, 367), style=wx.NO_BORDER)
        root.btn_bmp_motor_0.Bind(wx.EVT_BUTTON, lambda e: root.move_set(0.1))
        root.btn_bmp_motor_1 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_1_ch, (325, 367), style=wx.NO_BORDER)
        root.btn_bmp_motor_1.Bind(wx.EVT_BUTTON, lambda e: root.move_set(1))
        root.btn_bmp_motor_10 = wx.BitmapButton(dis_panel, -1, root.bmp_motor_10, (403, 367), style=wx.NO_BORDER)
        root.btn_bmp_motor_10.Bind(wx.EVT_BUTTON, lambda e: root.move_set(10))

        btn_bmp_motor_xyz_home = wx.BitmapButton(dis_panel, -1, bmp_motor_xyz_home, (480, 305), style=wx.NO_BORDER)
        btn_bmp_motor_xyz_home.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("all"))
        btn_bmp_motor_stop = wx.BitmapButton(dis_panel, -1, bmp_motor_stop, (480, 367), style=wx.NO_BORDER)
        btn_bmp_motor_stop.Bind(wx.EVT_BUTTON, lambda e: root.homeButtonClicked("Motors off"))

    root.text_motor_guide = wx.StaticText(dis_panel, label='motor menu', pos=(21, 441))
    root.text_motor_guide.SetFont(root.font_16)

    return
