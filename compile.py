"""
Compile module in python library pid.

Created on 15.06.2019

@author: Ruslan Dolovanyuk

example running:
    python compile.py build_ext --inplace

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
               Extension("dialogs", ["dialogs.py"]),
               Extension("options", ["options.py"]),
               Extension("commands", ["commands.py"]),
               Extension("drawer", ["drawer.py"]),
               Extension("menu", ["menu.py"]),
               Extension("configs", ["configs.py"]),
               Extension("database", ["database.py"]),
               Extension("version", ["version.py"]),
               Extension("wxdb", ["wxdb.py"]),
               Extension("linker", ["linker.py"]),
               Extension("player", ["player.py"]),
              ]

setup(
      name='main',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules
)
