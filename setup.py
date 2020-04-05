'''
Setup script build exe windows application.

created on 05.04.2020

@author: Ruslan Dolovanyuk

Example running: python setup.py build

'''

from cx_Freeze import setup, Executable

import version

executables = [Executable('main.pyw',
                          targetName='hotsound.exe',
                          base='Win32GUI')]

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml', 'xmlrpc',
            'bz2', 'select', 'pydoc', 'ctypes', 'tkinter', 'distutils', 'test',
           ]

includes = ['json', 'pickle', 'webbrowser', 'wx',
'multiprocessing', 'pyaudio', 'wave', 'sqlite3',
            
           ]

zip_include_packages = ['collections', 'encodings', 'importlib',
                        'json', 'pickle', 'webbrowser', 'wx',
                        'multiprocessing', 'pyaudio', 'wave', 'sqlite3',
                       ]

include_files = [('commands.pyd', 'lib/commands.pyd'),
                  ('configs.pyd', 'lib/configs.pyd'),
                  ('database.pyd', 'lib/database.pyd'),
                  ('dialogs.pyd', 'lib/dialogs.pyd'),
                  ('linker.pyd', 'lib/linker.pyd'),
                  ('menu.pyd', 'lib/menu.pyd'),
                  ('options.pyd', 'lib/options.pyd'),
                  ('player.pyd', 'lib/player.pyd'),
                  ('version.pyd', 'lib/version.pyd'),
                  ('wxdb.pyd', 'lib/wxdb.pyd'),
                  'languages.dat',
                 ]

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='hotsound',
      version=version.VERSION,
      description='Sound wave sintezator on keyboard hotkeys.',
      executables=executables,
      options=options)
