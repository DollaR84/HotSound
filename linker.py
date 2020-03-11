"""
Linker keyboard keys with sound files.

Created on 14.02.2020

@author: Ruslan Dolovanyuk

"""

import json


class Linker:
    """Class link keys with sound files."""

    def __init__(self):
        """Initialize linker class."""
        try:
            links_file = open('links.json', 'r', encoding="utf-8")
        except IOError:
            self.__links = {}
        else:
            with links_file:
                self.__links = json.load(links_file)

    def close(self):
        """Saving links before closing program."""
        with open('links.json', 'w', encoding="utf-8") as links_file:
            json.dump(self.__links, links_file, indent='   ')

    def set_link(self, keycode, path):
        """Set path of wav file to key code in dict links."""
        self.__links[keycode] = path

    def get_link(self, keycode):
        """Return path to wav file for keycode from dict links."""
        return self.__links.get(keycode, None)

    def del_link(self, keycode):
        """Delete row in dict of wav file."""
        if keycode in self.__links:
            del self.__links[keycode]

    def get_all_links(self):
        """Return all links in string format for view."""
        links = sorted(['{} - {}'.format(keycode, path) for keycode, path in self.__links.items()])
        return '\n'.join(links)
