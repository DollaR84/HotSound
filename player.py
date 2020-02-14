"""
Player sounds for project.

Created on 15.02.2020

@author: Ruslan Dolovanyuk

"""

import pyaudio
import threading
import wave


class Player:
    """Class player sounds."""

    def __init__(self):
        """Initialize player class."""
        self.audio = pyaudio.PyAudio()
        self.devices = []

        self.set_outputs()

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
