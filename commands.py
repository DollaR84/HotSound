"""
Commands for graphical interface.

Created on 12.02.2020

@author: Ruslan Dolovanyuk

"""

import webbrowser

from dialogs.dialogs import About
from dialogs.dialogs import Message

from linker import Linker

from player import Player

import version


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

        self.drawer.Destroy()

    def options(self, event):
        """Run settings dialog."""
        self.config.open_settings(self.drawer)

    def process(self, event):
        """Main process eventer for button."""
        pass
