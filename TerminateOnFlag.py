# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:54:08 2021

@author: idf-ia
"""

from biblioteques import *

flag = False

class TerminateOnFlag(keras.callbacks.Callback):
  
    def on_batch_end(self, batch, logs=None):
        
        if flag :
            
            print(" \n Training will finish after this batch \n")
            self.model.stop_training = True   
        

def clasifTrainStop():

    global flag
    flag = True      

def clasifTrainStart():

    global flag
    flag = False 