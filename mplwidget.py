# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:49:48 2022

@author: correa
"""



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib as mpl
from PyQt5.QtWidgets import QSizePolicy
import seaborn as sns
import numpy as np


import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets


class MplCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=15, height=13, dpi=80):
        mpl.style.use('seaborn')
        self.fig = Figure(figsize=(width, height), dpi=dpi)   
        
        self.ax = self.fig.add_subplot(111)     
        self.fig.subplots_adjust(left=0.13,right=0.95,bottom=0.1,top=0.90)
        
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        super(MplCanvas,self).__init__(self.fig)
        self.figure.set_facecolor('#10191e')
        
        
        
class MplWidget(QtWidgets.QWidget):

    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
    
        self.canvas = MplCanvas()
        #self.canvas.ax.set_facecolor("#283741")
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.mpl_toolbar)
        self.setLayout(self.vbl)
        
    def plot_graph(self, N , train_score , val_score ):


        #ax.set_title('Learning curve',fontweight="bold",color='white')
        #ax.legend(loc='upper right')
        
        self.clear_graph()
        
        self.canvas.ax.plot(N, train_score,"--o", label='train score',linewidth=3)
        self.canvas.ax.plot(N, val_score,"--o", label='Cross validation score',linewidth=3)
        
        self.canvas.ax.set_title('Learning curve',fontweight="bold",color='white')       
        self.canvas.ax.legend(loc='lower right')
        
        
        self.canvas.draw_idle()

        
    def plot_graph_data(self, x, y ):
  
        
        
        self.clear_graph()
        self.canvas.ax.plot(x, y,"o",linewidth=3)
        self.canvas.ax.set_title('Features relationship',fontweight="bold",color='white')


        
        self.canvas.draw_idle()
        
    def plot_conf_mat(self,true_class,y_pred,lbls):

        self.clear_graph()
    
        
        x_axis_labels = lbls # labels for x-axis
        y_axis_labels = lbls # labels for y-axis

        data=confusion_matrix(true_class, y_pred)
        
        a = sns.heatmap(data, xticklabels=x_axis_labels, yticklabels=y_axis_labels, annot=True, ax=self.canvas.ax,cbar=False,fmt='d')
        a.set_yticklabels(a.get_yticklabels(), rotation = 0)
        
        self.canvas.ax.set_title('Matrice de confusion',fontweight="bold",color='white')
        self.canvas.ax.set_ylabel('Vraies classes',fontweight="bold",color='white')
        self.canvas.ax.set_xlabel( 'Classes prédites',fontweight="bold",color='white')

        
        self.canvas.draw_idle()

        
    def plot_corr_mat(self,dataFrame):
        

        self.clear_graph()
        
        self.canvas.ax.set_title('Matrice de correlation',fontweight="bold",color='white')
        self.canvas.ax.set_ylabel('True classes',fontweight="bold",color='white')
        self.canvas.ax.set_xlabel('Predicted classes',fontweight="bold",color='white')
        
        
        mc = sns.heatmap(dataFrame.corr().abs(),annot=True, ax=self.canvas.ax,cbar=False,cmap='Greys');
        # print(dataFrame.corr())
        
        mc.set_yticklabels(mc.get_yticklabels(), rotation = 0)
        self.canvas.draw_idle()
        

    def plot_original_Signal(self,dataSerie, width,row):
        
        # self.canvas.ax.cla()
        amplitude = np.array(dataSerie)
        N = len(amplitude)
        temp = np.arange(0, width, width / N )

        self.canvas.ax.plot(temp, amplitude ,linewidth=3,label=f'Sig {row}')
        
        self.canvas.set_window_title('Original signals')     
        
        self.canvas.ax.legend(loc='lower right')
        
        self.canvas.draw_idle()

    def plot_scatter_regreResult(self,y_test,y_pred):
     
        self.clear_graph()
        self.canvas.ax.scatter(np.array(y_test), y_pred, label='y_pred')
        
        self.canvas.ax.plot(np.array(y_test),np.array(y_test),color='green')
        
        self.canvas.ax.set_ylabel('y_pred',fontweight="bold",color='white')
        self.canvas.ax.set_xlabel('y_test',fontweight="bold",color='white')
        
        self.canvas.ax.legend(loc='lower right')
        self.canvas.ax.set_title('Régression',fontweight="bold",color='white')

        self.canvas.draw_idle()
        
    def plot_scatter_regreTest(self,x,y_test,y_pred):
        
                
        self.clear_graph()
        self.canvas.ax.scatter(x, y_test, label='y_test')
        self.canvas.ax.scatter(x, y_pred, alpha=0.3,label='y_pred')
        self.canvas.ax.legend(loc='lower right')
        self.canvas.ax.set_title('Régression',fontweight="bold",color='white')

        self.canvas.draw_idle()
        
    def clear_graph(self):

        self.canvas.ax.cla()
        self.canvas.draw_idle()
        