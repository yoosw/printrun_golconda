__author__ = 'yoo'
# Calculator GUI:

# ___________v
# [7][8][9][/]
# [4][5][6][*]
# [1][2][3][-]
# [0][.][C][+]
# [    =     ]

# from __future__ import division # So that 8/3 will be 2.6666 and not 2
import wx
from math import * # So we can evaluate "sqrt(8)"

class Calculator(wx.Dialog):
    '''Main calculator dialog'''
    def __init__(self, title):
        # wx.Dialog.__init__(self, None, -1, "Calculator")
        # wx.Dialog.__init__(self, None, -1, title, style = (wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER))
        self.title_txt = title
        wx.Dialog.__init__(self, None, -1, title)
        sizer = wx.BoxSizer(wx.VERTICAL) # Main vertical sizer

        # ____________v
        # self.display = wx.ComboBox(self, -1) # Current calculation
        self.display = wx.TextCtrl(self, -1, '')
        font1 = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.display.SetFont(font1)
        sizer.Add(self.display, 0, wx.EXPAND) # Add to main sizer

        # # [7][8][9][/]
        # # [4][5][6][*]
        # # [1][2][3][-]
        # # [0][.][C][+]
        # gsizer = wx.GridSizer(4, 4)
        # for row in (("7", "8", "9", "/"),
        #             ("4", "5", "6", "*"),
        #             ("1", "2", "3", "-"),
        #             ("0", ".", "C", "+")):
        #     for label in row:
        #         b = wx.Button(self, -1, label)
        #         gsizer.Add(b)
        #         self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        # sizer.Add(gsizer, 1, wx.EXPAND)
        # [7][8][9]
        # [4][5][6]
        # [1][2][3]
        # [0][.][C]
        gsizer = wx.GridSizer(5, 3)
        font_cal = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        for row in (("7", "8", "9"),
                    ("4", "5", "6"),
                    ("1", "2", "3"),
                    ("0", ".", "C"),
                    ("-", "MOVE", "Off")):
            for label in row:
                # b = wx.Button(self, -1, label)
                b = wx.Button(self, -1, label, size=(80, 50))
                b.SetFont(font_cal)
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(gsizer, 1, wx.EXPAND)

        # swyoo add
        # b.SetFont(font_16)

        # [    =     ]
        # b = wx.Button(self, -1, "=")
        # self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        # sizer.Add(b, 0, wx.EXPAND)
        # self.equal = b

        # [    OK     ]
        # b = wx.Button(self, -1, "OK")
        if 0:
            b = wx.Button(self, -1, "OK", size=(80, 50))
            self.Bind(wx.EVT_BUTTON, self.OnButton, b)
            sizer.Add(b, 0, wx.EXPAND)
            self.equal = b

        # swyoo add
        self.cal_value = "pass"

        # Set sizer and center
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()

    def OnButton(self, evt):
        '''Handle button click event'''
        # Get title of clicked button
        label = evt.GetEventObject().GetLabel()

        # if label == "=": # Calculate
        #     try:
        #         compute = self.display.GetValue()
        #         # Ignore empty calculation
        #         if not compute.strip():
        #             return
        #
        #         # Calculate result
        #         result = eval(compute)
        #
        #         # Add to history
        #         self.display.Insert(compute, 0)
        #
        #         # Show result
        #         self.display.SetValue(str(result))
        #     except Exception, e:
        #         wx.LogError(str(e))
        #         return

        if label == "MOVE":  #if label == "OK":
            compute = self.display.GetValue()
            int_val = 0
            if not compute.strip():
                return

            try:
                int_val = eval(compute)
                if self.title_txt == "zoffset":
                    if int_val < 0 or int_val > 5:
                        dlg = wx.MessageDialog(self, _("z offset is between 0 to 5"), _("Exit"), wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        dlg.Destroy()
                        self.display.SetValue("")
                        return
                    else:
                        int_val = -int_val

                self.cal_value = str(int_val)
            except Exception, e:
                self.display.SetValue(e)

            self.Close()
        elif label == "C": # Clear
            self.display.SetValue("")

        elif label == "Off": # Clear
            # self.display.SetValue("")
            self.Close()
        else: # Just add button text to current calculation
            self.display.SetValue(self.display.GetValue() + label)
            # self.equal.SetFocus() # Set the [=] button in focus

# if __name__ == "__main__":
#     # Run the application
#     app = wx.PySimpleApp()
#     dlg = Calculator()
#     dlg.ShowModal()
#     dlg.Destroy()
