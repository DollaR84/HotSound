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
            json.dump(self.__links, links_file)
