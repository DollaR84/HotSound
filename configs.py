"""
Configs module.

Created on 11.02.2020

@author: Ruslan Dolovanyuk

"""

from dialogs.dialogs import RetCode

from dialogs.options import SettingsDialog

from wxdb import WXDB


class Config(WXDB):
    """Config program in database."""

    def __init__(self):
        """Initialization config class."""
        super().__init__('settings')

        if not self.db.if_exists('settings'):
            self.setup_config()

        self.load()

    def load(self):
        """Load settings from database."""
        script = 'SELECT * FROM settings'
        data = self.db.get(script)
        self.ids = {}
        for line in data:
            setattr(self, line[1], line[2])
            self.ids[line[1]] = line[0]

    def set_languages(self, languages):
        """Set all supported languages from languages pack."""
        self.__languages = languages

    def get_languages(self):
        """Return dict all supported languages."""
        return self.__languages

    def get_outputs(self):
        """Return list output device names."""
        # This method need override in command module.
        pass

    def open_settings(self, parent):
        """Open settings dialog."""
        dlg = SettingsDialog(parent, self)
        if RetCode.OK == dlg.ShowModal():
            scripts = []
            dlg.config.pop('donate_url')
            dlg.config.pop('languages')
            dlg.config.pop('outputs')
            for key, value in dlg.config.items():
                if key == '__languages':
                    continue
                script = '''UPDATE settings SET value="%s" WHERE id=%d
                     ''' % (value, self.ids[key])
                scripts.append(script)
            self.db.put(scripts)
        dlg.Destroy()
        self.load()

    def setup_config(self):
        """Create table settings in database."""
        scripts = []
        script = '''CREATE TABLE settings (
                    id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    value TEXT NOT NULL) WITHOUT ROWID
                 '''
        scripts.append(script)
        for substr in SCRIPTS['settings']:
            script = 'INSERT INTO settings (id, name, value) VALUES ({})'.format(substr)
            scripts.append(script)
        self.db.put(scripts)


SCRIPTS = {
            "settings": [
                         '1, "donate_url", "https://privatbank.ua/sendmoney?payment=238a49dc4f28672ee467e18c5005cdc6287ac5d9"',
                         '2, "general_language", "ru"',
                         '3, "general_output", "0"'
                        ]
          }


def load(data):
    """Construct class from json data."""
    temp_class_1 = type('__TempClass', (), {})
    temp_object = temp_class_1()
    for name, data_section in data.items():
        temp_class_2 = type('__' + name, (), {})
        setattr(temp_object, name, temp_class_2())
        section = getattr(temp_object, name)
        for key, value in data_section.items():
            value = __sub_load(value)
            setattr(section, key, value)

    return temp_object


def __sub_load(value):
    """Sub function for load json data to class structures."""
    __temp_class = type('__TempClass', (), {})
    __temp_object = __temp_class()
    if isinstance(value, dict):
        for key, item in value.items():
            item = __sub_load(item)
            setattr(__temp_object, key, item)
            value = __temp_object
    return value
