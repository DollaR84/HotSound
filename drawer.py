"""
Graphical form for project.

Created on 11.02.2020

@author: Ruslan Dolovanyuk

"""

import pickle

from commands import Commands

import configs

from menu import Menu

import wx


class Drawer:
    """Graphical form for project."""

    def __init__(self):
        """Initialization drawer form."""
        self.app = wx.App()
        self.wnd = MainFrame()
        self.wnd.Show(True)
        self.app.SetTopWindow(self.wnd)

    def mainloop(self):
        """Graphical main loop running."""
        self.app.MainLoop()


class MainFrame(wx.Frame):
    """Create user interface."""

    def __init__(self):
        """Initialization interface."""
        self.config = configs.Config()
        with open('languages.dat', 'rb') as lang_file:
            self.phrases = configs.load(pickle.load(lang_file)[self.config.general_language])
        super().__init__(None, wx.ID_ANY, self.phrases.titles.caption)
        self.command = Commands(self)
        self.menu = Menu(self)

        self.panel = wx.Panel(self, wx.ID_ANY)
        sizer_panel = wx.BoxSizer(wx.HORIZONTAL)
        sizer_panel.Add(self.panel, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer_panel)

        self.CreateStatusBar()
        self.__create_widgets()
        self.__create_bindings()

    def __create_widgets(self):
        """Create widgets program."""
        self.data = wx.TextCtrl(self.panel, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.but_process = wx.Button(self.panel, wx.ID_ANY, self.phrases.widgets.but_process)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.data, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.but_process, 0, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)

    def __create_bindings(self):
        """Create bindings for widgets and other events."""
        self.Bind(wx.EVT_CLOSE, getattr(self.command, 'close_window'))
        self.Bind(wx.EVT_BUTTON, getattr(self.command, 'process'), self.but_process)
