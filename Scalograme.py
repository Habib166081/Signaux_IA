# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:16:35 2022

@author: boukrana
"""


from biblioteques import *
from scipy import signal

import os




class scalograme(QObject):
    button_active = QtCore.pyqtSignal(bool) 
    arret_thrad = QtCore.pyqtSignal(bool) 
    compteur_signal = QtCore.pyqtSignal(bool,int) 
    def __init__(self ,plotScalograme):

        super(scalograme, self).__init__()
        self.plotScalograme=plotScalograme
        self.Data = pd.DataFrame(None)
        self.width=25
        self.file=""
        self.compteur = True
        
        
    def scalog(self):
        self.button_active.emit(True)
        t = np.arange(0,self.width,self.width/(len(self.Data.columns)-1))
        dt = t[1]-t[0]
        fs = 1/dt
        w = 6

        for i in range(len(self.Data)):
            freq = np.linspace(1, fs/2, 100)
            widths = w*fs / (2*freq*np.pi)
            cwtm = signal.cwt(self.Data.iloc[i,:-1], signal.morlet2, widths, w=w)

            if not os.path.exists(self.file + "/" +str(self.Data.iloc[i,-1])):
                os.makedirs(self.file + "/" +str(self.Data.iloc[i,-1]))
            else:
                pass
            self.plotScalograme.canvas.ax.clear()
            self.plotScalograme.canvas.figure.set_facecolor('white')
            self.plotScalograme.canvas.ax.axis('off')
            self.plotScalograme.canvas.ax.pcolormesh( t ,freq, np.abs(cwtm) , cmap='jet', shading='None')
            self.plotScalograme.canvas.figure.savefig(self.file + "/" +str(self.Data.iloc[i,-1]) +"/Sig{}.png".format(i))   
            self.plotScalograme.canvas.draw_idle()
        
            if self.compteur:
                self.compteur_signal.emit(True,i)
            else:
                self.compteur_signal.emit(False,i)
        self.arret_thrad(True)
        self.button_active.emit(False)


            
        
    

    def DataFrameTrain(self,width,dataframe,compteur):
        self.Data = dataframe
        self.width = width
        if compteur:
            self.compteur=True
        else:
            self.compteur=False
            
    
    def SavePath(self,file):
        self.file=file















