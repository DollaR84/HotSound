"""
Commands for graphical interface.

Created on 12.02.2020

@author: Ruslan Dolovanyuk

"""

import pyaudio
import webbrowser

from dialogs.dialogs import About
from dialogs.dialogs import Message

from linker import Linker

import version


class Commands:
    """Helper class, contains command for bind events, menu and buttons."""

    def __init__(self, drawer):
        """Initialization commands class."""
        self.drawer = drawer
        self.phrases = self.drawer.phrases
        self.message = Message(self.drawer)
        self.linker = Linker()

        self.config = self.drawer.config
        self.config.get_outputs = self.get_outputs

        self.audio = pyaudio.PyAudio()
        self.devices = []

        self.set_window()
        self.set_outputs()

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

        self.drawer.Destroy()

    def options(self, event):
        """Run settings dialog."""
        self.config.open_settings(self.drawer)

    def set_outputs(self):
        """Set outputs audio devices."""
        info = self.audio.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        for i in range(num_devices):
            if self.audio.get_device_info_by_host_api_device_index(0,i).get('maxOutputChannels') > 0:
                self.devices.append(self.audio.get_device_info_by_host_api_device_index(0, i))

    def get_outputs(self):
        """Return list all supported output audio devices."""
        return [device.get('name') for device in self.devices]

    def process(self, event):
        """Main process eventer for button."""
        pass
