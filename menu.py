"""
Menu module for project.

Created on 26.01.2020

@author: Ruslan Dolovanyuk

"""

import wx


class Menu:
    """Create menu for project."""

    def __init__(self, parent):
        """Initialization menu."""
        self.drawer = parent
        self.phrases = self.drawer.phrases
        self.command = self.drawer.command

        self.__create_menu()
        self.__create_accel()
        self.__create_bindings()

    def __create_menu(self):
        """Create menu program."""
        menu_file = wx.Menu()
        self.drawer.exit = menu_file.Append(-1, self.phrases.menu.file.items.exit.name, self.phrases.menu.file.items.exit.help)

        menu_options = wx.Menu()
        self.drawer.options = menu_options.Append(-1, self.phrases.menu.options.items.settings.name, self.phrases.menu.options.items.settings.help)

        menu_help = wx.Menu()
        self.drawer.donate = menu_help.Append(-1, self.phrases.menu.help.items.donate.name, self.phrases.menu.help.items.donate.help)
        self.drawer.about = menu_help.Append(-1, self.phrases.menu.help.items.about.name, self.phrases.menu.help.items.about.help)

        menuBar = wx.MenuBar()
        menuBar.Append(menu_file, self.phrases.menu.file.title)
        menuBar.Append(menu_options, self.phrases.menu.options.title)
        menuBar.Append(menu_help, self.phrases.menu.help.title)
        self.drawer.SetMenuBar(menuBar)

    def __create_accel(self):
        """Create accelerated table for menu."""
        acceltbl = wx.AcceleratorTable([
                                       (wx.ACCEL_CTRL, ord('Q'), self.drawer.exit.GetId()),
                                       (wx.ACCEL_CTRL, ord('O'), self.drawer.options.GetId()),
                                       ])
        self.drawer.SetAcceleratorTable(acceltbl)

    def __create_bindings(self):
        """Create bindings for menu."""
        self.drawer.Bind(wx.EVT_MENU, getattr(self.command, 'close'), self.drawer.exit)
        self.drawer.Bind(wx.EVT_MENU, getattr(self.command, 'options'), self.drawer.options)
        self.drawer.Bind(wx.EVT_MENU, getattr(self.command, 'donate'), self.drawer.donate)
        self.drawer.Bind(wx.EVT_MENU, getattr(self.command, 'about'), self.drawer.about)
