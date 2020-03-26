"""
Player sounds for project.

Created on 15.02.2020

@author: Ruslan Dolovanyuk

"""

from multiprocessing import Process

import pyaudio
import time
import wave


class Player:
    """Class player sounds."""

    def __init__(self):
        """Initialize player class."""
        self.config = None
        self.__audio = pyaudio.PyAudio()
        self.__devices = []
        self.__devices_indexies = {}

        self.set_outputs()

    def close(self):
        """Close PyAudio."""
        self.__audio.terminate()

    def set_outputs(self):
        """Set outputs audio devices."""
        info = self.__audio.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        for i in range(num_devices):
            device = self.__audio.get_device_info_by_host_api_device_index(0, i)
            if device.get('maxOutputChannels') > 0:
                self.__devices.append(device)
                self.__devices_indexies[device.get('name')] = i

    def get_outputs(self):
        """Return list all supported output audio devices."""
        return [device.get('name') for device in self.__devices]

    def play(self, path):
        """Play wave file from path."""
        proc = Process(target=__play__, args=(path, self.__get_index_device()))
        proc.start()

    def __get_index_device(self):
        """Return index device from set config."""
        name = self.__devices[int(self.config.general_output)].get('name')
        return self.__devices_indexies[name]


def __play__(path, output_index):
    """Play wave file in owner process."""
    audio = pyaudio.PyAudio()
    wf = wave.open(path, 'rb')

    def __callback__(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = audio.open(
                        format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output_device_index=output_index,
                        output=True,
                        stream_callback=__callback__)

    stream.start_stream()
    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()
    audio.terminate()
