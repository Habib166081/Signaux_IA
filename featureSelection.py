# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:45:02 2022

@author: picarda
"""
import pandas as pd

class FeatureSelection:
    
    def __init__(self):
        
        self.dataFrameFeature = pd.DataFrame(None)
        self.targets = pd.DataFrame(None)
        
    def select(self, paramSelection, dataFrameFeature):
        
        self.targets = dataFrameFeature.pop('target')
        self.dataFrameFeature = dataFrameFeature
        
        
        if paramSelection['type'] == 'variance':
            self.varianceSelection(paramSelection['threshold'])
            
        else:
            raise ValueError("The feature selection methode '" + str(paramSelection["type"]) + "' is not handled by the select function")
            
        
    def varianceSelection(self, threshold):
        print("test")
        
        
        
# Testing #

df = pd.read_csv('N:\P3\STAGIAIRES\Arthur Picard\Interface\sig_Feautures_train.csv')
f = FeatureSelection()
dico = {
        'type' : 'variance',
        'threshold' : 0.1
    }

f.select(dico, df)