# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

import logging

try:
    import wx
except:
    logging.error(_("WX is not installed. This program requires WX to run."))
    raise

from printrun.utils import install_locale
install_locale('pronterface')

from .controls import ControlsSizer, add_extra_controls
from .viz import VizPane
from .log import LogPane
from .toolbar import MainToolbar
# swyoo 2015.09.30 change toolbar position
from .toolbar_home import HomeToolbar

# swyoo 2015.08.31 for image display in linux
from printrun.utils import imagefile

# swyoo 2015.09.08 divide os nt, linux
import os
# swyoo 2015.09.09 add for tap move
# import time
from control_setting import Setting_Control
from control_printing import Print_Control
from control_motor import Motor_Control
from control_help import Setting_Help
from control_original import createTabbedGui_sub, createGui_sub

from .widgets import TempGauge
from .utils import make_autosize_button

class ToggleablePane(wx.BoxSizer):

    def __init__(self, root, label, parentpanel, parentsizers):
        super(ToggleablePane, self).__init__(wx.HORIZONTAL)
        if not parentpanel: parentpanel = root.panel
        self.root = root
        self.visible = True
        self.parentpanel = parentpanel
        self.parentsizers = parentsizers
        self.panepanel = root.newPanel(parentpanel)
        self.button = wx.Button(parentpanel, -1, label, size = (22, 18), style = wx.BU_EXACTFIT)
        self.button.Bind(wx.EVT_BUTTON, self.toggle)

    def toggle(self, event):
        if self.visible:
            self.Hide(self.panepanel)
            self.on_hide()
        else:
            self.Show(self.panepanel)
            self.on_show()
        self.visible = not self.visible
        self.button.SetLabel(">" if self.button.GetLabel() == "<" else "<")

class LeftPaneToggleable(ToggleablePane):
    def __init__(self, root, parentpanel, parentsizers):
        super(LeftPaneToggleable, self).__init__(root, "<", parentpanel, parentsizers)
        self.Add(self.panepanel, 0, wx.EXPAND)
        self.Add(self.button, 0)

    def set_sizer(self, sizer):
        self.panepanel.SetSizer(sizer)

    def on_show(self):
        for sizer in self.parentsizers:
            sizer.Layout()

    def on_hide(self):
        for sizer in self.parentsizers:
            # Expand right splitterwindow
            if isinstance(sizer, wx.SplitterWindow):
                if sizer.shrinked:
                    button_width = self.button.GetSize()[0]
                    sizer.SetSashPosition(sizer.GetSize()[0] - button_width)
            else:
                sizer.Layout()

class LogPaneToggleable(ToggleablePane):
    def __init__(self, root, parentpanel, parentsizers):
        super(LogPaneToggleable, self).__init__(root, ">", parentpanel, parentsizers)
        self.Add(self.button, 0)
        pane = LogPane(root, self.panepanel)
        self.panepanel.SetSizer(pane)
        self.Add(self.panepanel, 1, wx.EXPAND)
        self.splitter = self.parentpanel.GetParent()

    def on_show(self):
        self.splitter.shrinked = False
        self.splitter.SetSashPosition(self.splitter.GetSize()[0] - self.orig_width)
        self.splitter.SetMinimumPaneSize(self.orig_min_size)
        self.splitter.SetSashGravity(self.orig_gravity)
        if hasattr(self.splitter, "SetSashSize"): self.splitter.SetSashSize(self.orig_sash_size)
        if hasattr(self.splitter, "SetSashInvisible"): self.splitter.SetSashInvisible(False)
        for sizer in self.parentsizers:
            sizer.Layout()

    def on_hide(self):
        self.splitter.shrinked = True
        self.orig_width = self.splitter.GetSize()[0] - self.splitter.GetSashPosition()
        button_width = self.button.GetSize()[0]
        self.orig_min_size = self.splitter.GetMinimumPaneSize()
        self.orig_gravity = self.splitter.GetSashGravity()
        self.splitter.SetMinimumPaneSize(button_width)
        self.splitter.SetSashGravity(1)
        self.splitter.SetSashPosition(self.splitter.GetSize()[0] - button_width)
        if hasattr(self.splitter, "SetSashSize"):
            self.orig_sash_size = self.splitter.GetSashSize()
            self.splitter.SetSashSize(0)
        if hasattr(self.splitter, "SetSashInvisible"): self.splitter.SetSashInvisible(True)
        for sizer in self.parentsizers:
            sizer.Layout()

class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # this list will contain all controls that should be only enabled
        # when we're connected to a printer
        self.panel = wx.Panel(self, -1)
        self.reset_ui()
        self.statefulControls = []
        # swyoo 2015.09.10 for hide tap5
        self.page_hidden = False
        self.tap_menu = 'home'

    # swyoo 2015.09.04 for guage
    def TimerHandler(self, event):

        # self.count = self.count + 1
        #
        # if self.count >= 100:
        #     # self.count = 0
        #     return
        # self.gauge.SetValue(self.count)
        self.gauge.SetValue(int(self.var_loading_count))

    def reset_ui(self):
        self.panels = []
        self.printerControls = []

    def newPanel(self, parent, add_to_list = True):
        panel = wx.Panel(parent)
        self.registerPanel(panel, add_to_list)
        return panel

    def registerPanel(self, panel, add_to_list = True):
        panel.SetBackgroundColour(self.bgcolor)
        if add_to_list: self.panels.append(panel)

    def createBaseGui(self):
        self.notesizer = wx.BoxSizer(wx.VERTICAL)
        # self.notebook = wx.Notebook(self.panel)
        # self.notebook = wx.Notebook(self.panel, style=wx.NB_LEFT)
        if os.name == "nt":
            self.notebook = wx.Notebook(self.panel, style=wx.BK_DEFAULT)
        else:
            self.notebook = wx.Notebook(self.panel, style=
                                                    # wx.BK_DEFAULT
                                                    # wx.BK_TOP
                                                    # #wx.BK_BOTTOM
                                                    wx.BK_LEFT
                                                    # wx.BK_RIGHT
                                                    #  | wx.NB_MULTILINE
                                                    )

        # self.notebook.SetBackgroundColour(self.bgcolor)
        self.notebook.SetBackgroundColour('#FFFFFF')

        self.page0panel = self.newPanel(self.notebook)
        self.page1panel = self.newPanel(self.notebook)
        self.page2panel = self.newPanel(self.notebook)
        self.page3panel = self.newPanel(self.notebook)
        self.page4panel = self.newPanel(self.notebook)
        self.page5panel = self.newPanel(self.notebook)
        # self.page6panel = self.newPanel(self.notebook)

        # swyoo 2015.08.29 set color, image
        self.page0panel.SetBackgroundColour('#FFFFFF')
        self.page1panel.SetBackgroundColour('#FFFFFF')
        self.page2panel.SetBackgroundColour('#FFFFFF')
        self.page3panel.SetBackgroundColour('#FFFFFF')
        self.page4panel.SetBackgroundColour('#FFFFFF')
        # self.page5panel.SetBackgroundColour('#FFFFFF')

        # swyoo 2015.09.02 set background image
        image_file = "flexor/printing/printing_bg.png"
        bmp1 = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self.page1panel, -1, bmp1, (0, 0))

        image_file = "flexor/motor/motor_bg.png"
        bmp2 = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap2 = wx.StaticBitmap(self.page2panel, -1, bmp2, (0, 0))

        # image_file = "flexor/setting/setting_bg.png"
        # bmp3 = wx.Image(imagefile(image_file), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # self.bitmap3 = wx.StaticBitmap(self.page3panel, -1, bmp3, (0, 0))

        # font_loading_file = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.font_14 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.font_16 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.font_16_bold = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.BOLD)
        self.font_18 = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font_bold_20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, u'Consolas')
        self.font_20 = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font_22 = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font_24 = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font_26 = wx.Font(26, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font_28 = wx.Font(28, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font_32 = wx.Font(32, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        #========================================================== tap0 : Home
        self.hometoolbarsizer = HomeToolbar(self, self.page0panel)
        self.page0panel.SetSizer(self.hometoolbarsizer)
        #========================================================== tap1 : Print
        Print_Control(self, self.page1panel)
        #========================================================== tap2 : Motor
        Motor_Control(self, self.page2panel)
        #========================================================== tap3 : Setting
        # Setting_Control(self,  self.page3panel)
        #========================================================== tap4 : help
        self.helptoolbarsizer = Setting_Help(self,  self.page3panel)
        self.page4panel.SetSizer(self.helptoolbarsizer)
        #========================================================== tap5 : Log
        # swyoo 2015.09.01 should pass VizPane for etc
        vizpane = VizPane(self, self.page4panel)

        self.mainsizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.mainsizer_4.Add(LogPane(self, self.page4panel), 1, wx.EXPAND)
        self.page4panel.SetSizer(self.mainsizer_4)
        #========================================================== tap6 : original
        if self.settings.uimode in (_("Tabbed"), _("Tabbed with platers")):
            createTabbedGui_sub(self, self.page5panel)
        else:
            createGui_sub(self, self.settings.uimode == _("Compact"),
                          self.settings.controlsmode == "Mini", self.page5panel)
        #========================================================== tap End
        self.notesizer.Add(self.notebook, 1, wx.EXPAND)
        self.notebook.AddPage(self.page0panel, _(""))
        self.notebook.AddPage(self.page1panel, _(""))
        self.notebook.AddPage(self.page2panel, _(""))
        self.notebook.AddPage(self.page3panel, _(""))
        if os.name == "nt":
            self.notebook.AddPage(self.page4panel, _("log"))
            self.notebook.AddPage(self.page5panel, _("Original"))

        # list containing notebook images:
        # .ico seem to be more OS portable
        il = wx.ImageList(102, 103) # the (16, 16) is the size in pixels of the images

        self.img0 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_main.png"), wx.BITMAP_TYPE_PNG))
        self.img1 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_printing.png"), wx.BITMAP_TYPE_PNG))
        self.img2 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_control.png"), wx.BITMAP_TYPE_PNG))
        # self.img3 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_setting.png"), wx.BITMAP_TYPE_PNG))
        self.img3 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_help.png"), wx.BITMAP_TYPE_PNG))
        # self.img4 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_log.png"), wx.BITMAP_TYPE_PNG))
        # self.img5 = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_original.png"), wx.BITMAP_TYPE_PNG))
        self.img0_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_main_ch.png"), wx.BITMAP_TYPE_PNG))
        self.img1_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_printing_ch.png"), wx.BITMAP_TYPE_PNG))
        self.img2_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_control_ch.png"), wx.BITMAP_TYPE_PNG))
        # self.img3_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_setting_ch.png"), wx.BITMAP_TYPE_PNG))
        self.img3_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_help_ch.png"), wx.BITMAP_TYPE_PNG))
        # self.img4_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_log_ch.png"), wx.BITMAP_TYPE_PNG))
        # self.img5_ch = il.Add(wx.Bitmap(imagefile("flexor/tap/tap_original_ch.png"), wx.BITMAP_TYPE_PNG))

        self.image_list = {
            0: self.img0,
            1: self.img1,
            2: self.img2,
            3: self.img3,
            4: self.img0_ch,
            5: self.img1_ch,
            6: self.img2_ch,
            7: self.img3_ch,
        }

        self.tap_list = {
            0: "home",
            1: "print",
            2: "motor",
            3: "help",
        }

        # swyoo 2015.09.01 add to tap the image
        # set images to pages:
        # #first assign image list created above to notebook:
        self.notebook.AssignImageList(il)
        # then assign each image in list to corresponding page.
        # #the sharp-eyed will see you could use a loop for this,
        # #but for maximum clarity/understanding I'm using the long way...
        self.notebook.SetPageImage(0, self.img0_ch)
        self.notebook.SetPageImage(1, self.img1)
        self.notebook.SetPageImage(2, self.img2)
        self.notebook.SetPageImage(3, self.img3)
        # if os.name == "nt":
        #     self.notebook.SetPageImage(4, self.img4)
        #     self.notebook.SetPageImage(5, self.img5)

        # if this isn't called the notebook background color doesn't work right when switching
        #  themes in XP.
        self.notebook.SetBackgroundColour(self.notebook.GetThemeBackgroundColour())
        self.panel.SetSizer(self.notesizer)

        # swyoo 2015.11.17 should change tap image
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

        # self.panel.SetSizerAndFit(self.notesizer)
        self.Bind(wx.EVT_CLOSE, self.kill)
        minsize = [600, 450]
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window
        self.Fit()

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()

        if old < 4:
            old_tap = self.image_list[old]
            self.notebook.SetPageImage(old, old_tap)
        if new < 4:
            new_tap = self.image_list[new + 4]
            self.notebook.SetPageImage(new, new_tap)

            self.tap_menu = self.tap_list[new]

        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        # self.log.write('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()

    def Visual_tab(self, event):
        if self.page_hidden:
            self.notebook.AddPage(self.page5panel, "Original")
            self.page_hidden = False
        else:
            self.notebook.RemovePage(5)
            self.page5panel.Hide()
            self.page_hidden = True

    # swyoo 2015.09.09 add for tap move
    def switch_tab(self, page):
        notebook = self.notebook
        # window so ok, but too late in raspi
        # if page == 1:
        #     time.sleep(0.5)
        # else:
        #     time.sleep(0.2)
        notebook.SetSelection(page)

    def createTabbedGui(self):
        self.notesizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = wx.Notebook(self.panel)
        self.notebook.SetBackgroundColour(self.bgcolor)
        page1panel = self.newPanel(self.notebook)
        page2panel = self.newPanel(self.notebook)
        self.mainsizer_page1 = wx.BoxSizer(wx.VERTICAL)
        page1panel1 = self.newPanel(page1panel)
        page1panel2 = self.newPanel(page1panel)
        self.toolbarsizer = MainToolbar(self, page1panel1, use_wrapsizer = True)
        page1panel1.SetSizer(self.toolbarsizer)
        self.mainsizer_page1.Add(page1panel1, 0, wx.EXPAND)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        page1panel2.SetSizer(self.lowersizer)
        leftsizer = wx.BoxSizer(wx.VERTICAL)
        controls_sizer = ControlsSizer(self, page1panel2, True)
        leftsizer.Add(controls_sizer, 1, wx.ALIGN_CENTER)
        rightsizer = wx.BoxSizer(wx.VERTICAL)
        extracontrols = wx.GridBagSizer()
        add_extra_controls(extracontrols, self, page1panel2, controls_sizer.extra_buttons)
        rightsizer.AddStretchSpacer()
        rightsizer.Add(extracontrols, 0, wx.ALIGN_CENTER)
        self.lowersizer.Add(leftsizer, 0, wx.ALIGN_CENTER | wx.RIGHT, border = 10)
        self.lowersizer.Add(rightsizer, 1, wx.ALIGN_CENTER)
        self.mainsizer_page1.Add(page1panel2, 1)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.splitterwindow = wx.SplitterWindow(page2panel, style = wx.SP_3D)
        page2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel1 = self.newPanel(self.splitterwindow)
        page2sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel2 = self.newPanel(self.splitterwindow)
        vizpane = VizPane(self, page2panel1)
        page2sizer1.Add(vizpane, 1, wx.EXPAND)
        page2sizer2.Add(LogPane(self, page2panel2), 1, wx.EXPAND)
        page2panel1.SetSizer(page2sizer1)
        page2panel2.SetSizer(page2sizer2)
        self.splitterwindow.SetMinimumPaneSize(1)
        self.splitterwindow.SetSashGravity(0.5)
        self.splitterwindow.SplitVertically(page2panel1, page2panel2,
                                            self.settings.last_sash_position)
        self.mainsizer.Add(self.splitterwindow, 1, wx.EXPAND)
        page1panel.SetSizer(self.mainsizer_page1)
        page2panel.SetSizer(self.mainsizer)
        self.notesizer.Add(self.notebook, 1, wx.EXPAND)
        self.notebook.AddPage(page1panel, _("Commands"))
        self.notebook.AddPage(page2panel, _("Status"))
        if self.settings.uimode == _("Tabbed with platers"):
            from printrun.stlplater import StlPlaterPanel
            from printrun.gcodeplater import GcodePlaterPanel
            page3panel = StlPlaterPanel(parent = self.notebook,
                                        callback = self.platecb,
                                        build_dimensions = self.build_dimensions_list,
                                        circular_platform = self.settings.circular_bed,
                                        simarrange_path = self.settings.simarrange_path,
                                        antialias_samples = int(self.settings.antialias3dsamples))
            page4panel = GcodePlaterPanel(parent = self.notebook,
                                          callback = self.platecb,
                                          build_dimensions = self.build_dimensions_list,
                                          circular_platform = self.settings.circular_bed,
                                          antialias_samples = int(self.settings.antialias3dsamples))
            self.registerPanel(page3panel)
            self.registerPanel(page4panel)
            self.notebook.AddPage(page3panel, _("Plater"))
            self.notebook.AddPage(page4panel, _("G-Code Plater"))
        self.panel.SetSizer(self.notesizer)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        # Custom buttons
        if wx.VERSION > (2, 9): self.cbuttonssizer = wx.WrapSizer(wx.HORIZONTAL)
        else: self.cbuttonssizer = wx.GridBagSizer()
        self.cbuttonssizer = wx.GridBagSizer()
        self.centerpanel = self.newPanel(page1panel2)
        self.centerpanel.SetSizer(self.cbuttonssizer)
        rightsizer.Add(self.centerpanel, 0, wx.ALIGN_CENTER)
        rightsizer.AddStretchSpacer()

        self.panel.SetSizerAndFit(self.notesizer)

        self.cbuttons_reload()
        minsize = self.lowersizer.GetMinSize()  # lower pane
        minsize[1] = self.notebook.GetSize()[1]
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window
        self.Fit()

    def createGui(self, compact = False, mini = False):
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        upperpanel = self.newPanel(self.panel, False)
        self.toolbarsizer = MainToolbar(self, upperpanel)
        lowerpanel = self.newPanel(self.panel)
        upperpanel.SetSizer(self.toolbarsizer)
        lowerpanel.SetSizer(self.lowersizer)
        leftpanel = self.newPanel(lowerpanel)
        left_pane = LeftPaneToggleable(self, leftpanel, [self.lowersizer])
        leftpanel.SetSizer(left_pane)
        left_real_panel = left_pane.panepanel
        controls_panel = self.newPanel(left_real_panel)
        controls_sizer = ControlsSizer(self, controls_panel, mini_mode = mini)
        controls_panel.SetSizer(controls_sizer)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.Add(controls_panel, 1, wx.EXPAND)
        left_pane.set_sizer(left_sizer)
        self.lowersizer.Add(leftpanel, 0, wx.EXPAND)
        if not compact:  # Use a splitterwindow to group viz and log
            rightpanel = self.newPanel(lowerpanel)
            rightsizer = wx.BoxSizer(wx.VERTICAL)
            rightpanel.SetSizer(rightsizer)
            self.splitterwindow = wx.SplitterWindow(rightpanel, style = wx.SP_3D)
            self.splitterwindow.SetMinimumPaneSize(150)
            self.splitterwindow.SetSashGravity(0.8)
            rightsizer.Add(self.splitterwindow, 1, wx.EXPAND)
            vizpanel = self.newPanel(self.splitterwindow)
            logpanel = self.newPanel(self.splitterwindow)
            self.splitterwindow.SplitVertically(vizpanel, logpanel,
                                                self.settings.last_sash_position)
            self.splitterwindow.shrinked = False
        else:
            vizpanel = self.newPanel(lowerpanel)
            logpanel = self.newPanel(left_real_panel)
        viz_pane = VizPane(self, vizpanel)
        # Custom buttons
        if wx.VERSION > (2, 9): self.cbuttonssizer = wx.WrapSizer(wx.HORIZONTAL)
        else: self.cbuttonssizer = wx.GridBagSizer()
        self.centerpanel = self.newPanel(vizpanel)
        self.centerpanel.SetSizer(self.cbuttonssizer)
        viz_pane.Add(self.centerpanel, 0, flag = wx.ALIGN_CENTER)
        vizpanel.SetSizer(viz_pane)
        if compact:
            log_pane = LogPane(self, logpanel)
        else:
            log_pane = LogPaneToggleable(self, logpanel, [self.lowersizer])
            left_pane.parentsizers.append(self.splitterwindow)
        logpanel.SetSizer(log_pane)
        if not compact:
            self.lowersizer.Add(rightpanel, 1, wx.EXPAND)
        else:
            left_sizer.Add(logpanel, 1, wx.EXPAND)
            self.lowersizer.Add(vizpanel, 1, wx.EXPAND)
        self.mainsizer.Add(upperpanel, 0, wx.EXPAND)
        self.mainsizer.Add(lowerpanel, 1, wx.EXPAND)
        self.panel.SetSizer(self.mainsizer)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        self.mainsizer.Layout()
        # This prevents resizing below a reasonnable value
        # We sum the lowersizer (left pane / viz / log) min size
        # the toolbar height and the statusbar/menubar sizes
        minsize = [0, 0]
        minsize[0] = self.lowersizer.GetMinSize()[0]  # lower pane
        minsize[1] = max(viz_pane.GetMinSize()[1], controls_sizer.GetMinSize()[1])
        minsize[1] += self.toolbarsizer.GetMinSize()[1]  # toolbar height
        displaysize = wx.DisplaySize()
        minsize[0] = min(minsize[0], displaysize[0])
        minsize[1] = min(minsize[1], displaysize[1])
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window

        self.cbuttons_reload()

    def gui_set_connected(self):
        self.xyb.enable()
        self.zb.enable()
        for control in self.printerControls:
            control.Enable()

    def gui_set_disconnected(self):
        self.printbtn.Disable()
        self.pausebtn.Disable()
        self.recoverbtn.Disable()
        for control in self.printerControls:
            control.Disable()
        self.xyb.disable()
        self.zb.disable()
