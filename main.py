# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 14:01:43 2022

@author: correa
"""

from biblioteques import *
from MainWindows import *


if __name__ == '__main__':
 
    app = QtWidgets.QApplication.instance() # checks if QApplication already exists 
    
    if not app: # create QApplication if it doesnt exist 
        app = QtWidgets.QApplication([])
    
    
    app.setStyle('Fusion')

 
    ml_windows = MainWindows()
    ml_windows.setWindowIcon(QIcon('images\Logo_mini.png'))
    ml_windows.show()
    
    app.exec_()