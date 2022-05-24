# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:27:04 2022

@author: correa
"""


import ctypes # Ces trois lignes sont pour affichage du logo
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,QObject
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QLineEdit,QListWidgetItem, QFileDialog

from fenetre_machineLearning import Ui_MainWindow    
from TableModel import TableModel
######################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time


from kymatio.numpy import Scattering1D
from scipy.signal import hilbert
from scipy.fft import fft, fftfreq


from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from sklearn.metrics import f1_score, confusion_matrix, classification_report
from sklearn.metrics import r2_score

from sklearn.model_selection import learning_curve

#regression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso



