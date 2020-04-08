"""
Project running module.

Created on 26.01.2020

@author: Ruslan Dolovanyuk

"""

import multiprocessing

from drawer import Drawer


def main():
    drawer = Drawer()
    drawer.mainloop()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
