"""
Module settings wx with database.

Created on 25.05.2019

@author: Ruslan Dolovanyuk

"""

from database import Database


class WXDB:
    """Class default settings gui wx in database."""

    def __init__(self, db_name):
        """Initialization base class settings wx in database."""
        self.db_name = db_name
        self.db = Database()

        self.db.connect(self.db_name + '.db')
        if not self.db.if_exists('window'):
            self.setup_wxdb()

    def close(self):
        """Save finish program."""
        self.db.disconnect()

    def get_pos(self):
        """Return position window."""
        script = 'SELECT px, py FROM window'
        return self.db.get(script)[0]

    def set_pos(self, pos):
        """Save position window."""
        script = 'UPDATE window SET px=%d, py=%d WHERE id=1' % tuple(pos)
        self.db.put(script)

    def get_size(self):
        """Return size window."""
        script = 'SELECT sx, sy FROM window'
        return self.db.get(script)[0]

    def set_size(self, size):
        """Save size window."""
        script = 'UPDATE window SET sx=%d, sy=%d WHERE id=1' % tuple(size)
        self.db.put(script)

    def setup_wxdb(self):
        """Create table in database."""
        scripts = []
        script = '''CREATE TABLE window (
                    id INTEGER PRIMARY KEY NOT NULL,
                    px INTEGER NOT NULL,
                    py INTEGER NOT NULL,
                    sx INTEGER NOT NULL,
                    sy INTEGER NOT NULL) WITHOUT ROWID
                 '''
        scripts.append(script)
        script = '''INSERT INTO window (id, px, py, sx, sy)
                    VALUES (1, 0, 0, 800, 600)'''
        scripts.append(script)
        self.db.put(scripts)
