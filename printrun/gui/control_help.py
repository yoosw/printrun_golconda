import wx
import os

from printrun.utils import imagefile
from .utils import make_autosize_button

def Setting_Help(root, parentpanel):

    image_file = "flexor/help/help_bg.png"
    bmp_bg = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    background_image = wx.StaticBitmap(parentpanel, -1, bmp_bg, (0, 0))

    if os.name == "nt":
        dis_panel = background_image
    else:
        dis_panel = parentpanel

    # ------------------imsi
    toolbar_sizer = wx.BoxSizer
    self = toolbar_sizer(wx.HORIZONTAL)

    # if os.name == "nt":
    # motor_on_btn = make_autosize_button(dis_panel, _("led on"), lambda e: root.gpio_control("led_on"), _("led on start"))
    # self.Add(motor_on_btn, 0, wx.TOP | wx.LEFT, 10)
    #
    # motor_off_btn = make_autosize_button(dis_panel, _("led off"), lambda e: root.gpio_control("led_off"), _("led off start"))
    # self.Add(motor_off_btn, 0, wx.TOP | wx.LEFT, 10)
    #
    # motor_on_btn = make_autosize_button(dis_panel, _("motor forward"), lambda e: root.gpio_control("motor_forward"), _("bobbin motor on"))
    # self.Add(motor_on_btn, 0, wx.TOP | wx.LEFT, 10)
    #
    # motor_on_btn = make_autosize_button(dis_panel, _("motor reverse"), lambda e: root.gpio_control("motor_reverse"), _("bobbin motor on"))
    # self.Add(motor_on_btn, 0, wx.TOP | wx.LEFT, 10)
    #
    # motor_off_btn = make_autosize_button(dis_panel, _("motor auto on"), lambda e: root.gpio_control("motor_auto_on"), _("bobbin motor off"))
    # self.Add(motor_off_btn, 0, wx.TOP | wx.LEFT, 10)
    #
    # motor_off_btn = make_autosize_button(dis_panel, _("motor auto off"), lambda e: root.gpio_control("motor_auto_off"), _("bobbin motor start by sensor"))
    # self.Add(motor_off_btn, 0, wx.TOP | wx.LEFT, 10)
    # ------------------imsi

    # =============
    bmp_help_admin = wx.Bitmap(imagefile("flexor/help/help_admin.png"), wx.BITMAP_TYPE_PNG)
    bmp_help_initialize = wx.Bitmap(imagefile("flexor/help/help_initialize.png"), wx.BITMAP_TYPE_PNG)

    if os.name == "nt":
        btn_bmp_help_admin = wx.BitmapButton(dis_panel, -1, bmp_help_admin, (408, 253), style=wx.NO_BORDER)
        btn_bmp_help_admin.Bind(wx.EVT_BUTTON, root.display_ch)
        btn_bmp_help_initialize = wx.BitmapButton(dis_panel, -1, bmp_help_initialize, (408, 330), style=wx.NO_BORDER)
        btn_bmp_help_initialize.Bind(wx.EVT_BUTTON, root.on_reset_value)
    else:
        btn_bmp_help_admin = wx.BitmapButton(dis_panel, -1, bmp_help_admin, (408, 253), style=wx.NO_BORDER)
        btn_bmp_help_admin.Bind(wx.EVT_BUTTON, root.display_ch)
        btn_bmp_help_initialize = wx.BitmapButton(dis_panel, -1, bmp_help_initialize, (408, 330), style=wx.NO_BORDER)
        btn_bmp_help_initialize.Bind(wx.EVT_BUTTON, root.on_reset_value)

    # if os.name == "nt":
    root.text_help_guide = wx.StaticText(dis_panel, label='help text', pos=(21, 441))
    root.text_help_guide.SetFont(root.font_16)

    return self
