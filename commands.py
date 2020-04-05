"""
Commands for graphical interface.

Created on 12.02.2020

@author: Ruslan Dolovanyuk

"""

import webbrowser

from dialogs import About
from dialogs import Message

from linker import Linker

from player import Player

import version

import wx


class Commands:
    """Helper class, contains command for bind events, menu and buttons."""

    def __init__(self, drawer):
        """Initialization commands class."""
        self.drawer = drawer
        self.phrases = self.drawer.phrases
        self.message = Message(self.drawer)
        self.linker = Linker()
        self.player = Player()

        self.config = self.drawer.config
        self.config.get_outputs = self.player.get_outputs
        self.player.config = self.config

        self.wildcard = 'Wave files (*.wav)|*.wav|' \
                        'All files (*.*)|*.*'

        self.__mods = [
                       wx.WXK_CONTROL,
                       wx.WXK_SHIFT,
                       wx.WXK_ALT,
                       wx.WXK_WINDOWS_LEFT,
                       wx.WXK_WINDOWS_RIGHT,
                       wx.WXK_WINDOWS_MENU,
                      ]

        self.set_window()

    def set_window(self):
        """Set size and position window from saving data."""
        self.drawer.SetPosition(self.config.get_pos())
        self.drawer.SetSize(self.config.get_size())
        self.drawer.Layout()

    def donate(self, event):
        """Run donate hyperlink in browser."""
        webbrowser.open(self.config.donate_url)

    def about(self, event):
        """Run about dialog."""
        About(
              self.drawer,
              self.phrases.about.title,
              self.phrases.about.name,
              version.VERSION,
              self.phrases.about.author
             ).ShowModal()

    def close(self, event):
        """Close event for button close."""
        self.drawer.Close(True)

    def close_window(self, event):
        """Close window event."""
        self.config.set_pos(self.drawer.GetScreenPosition())
        self.config.set_size(self.drawer.GetSize())
        self.config.close()
        self.linker.close()
        self.player.close()

        self.drawer.Destroy()

    def options(self, event):
        """Run settings dialog."""
        self.config.open_settings(self.drawer)

    def get_path_file(self):
        """Return path wave file."""
        path = ''
        file_dlg = wx.FileDialog(self.drawer, self.phrases.titles.choice_file, '', '', self.wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if wx.ID_OK == file_dlg.ShowModal():
            path = file_dlg.GetPath()
            file_dlg.Destroy()
        return path

    def process(self, event):
        """Main process eventer for button."""
        keycode = event.GetKeyCode()

        if not keycode in self.__mods:
            if event.CmdDown() and event.ShiftDown():
                self.linker.del_link(keycode)
                self.drawer.data.SetValue(self.linker.get_all_links())
                self.drawer.Layout()
            elif event.CmdDown():
                path = self.get_path_file()
                if path != '':
                    self.linker.set_link(keycode, path)
                    self.drawer.data.SetValue(self.linker.get_all_links())
                    self.drawer.Layout()
            else:
                path = self.linker.get_link(keycode)
                if path is not None:
                    self.player.play(path)

        event.Skip()
