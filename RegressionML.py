# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 08:39:23 2022

@author: correa
"""

from biblioteques import *

class RegressionML (QObject):
    

    send_results_train = QtCore.pyqtSignal(str)
    send_results_test = QtCore.pyqtSignal(str,object)
    
    
    def __init__(self):
    
        super(RegressionML, self).__init__()
        
        self.X_train = None
        self.y_train = None
        

        
        self.model_regr = None
        
    
    def training(self, transformer, estimator, dataFrame):
        

        self.X_train = dataFrame.drop('Target', axis=1)
        self.y_train = dataFrame['Target']

        
        #---------------------------------------------------------------------------
        # Trasformeurs
        
        if transformer == 'None': 
            
            preprocessor = None
            
        elif transformer == 'PolynomialFeatures':
         
            preprocessor = make_pipeline(PolynomialFeatures(1, include_bias=False))
        
                                         
        #---------------------------------------------------------------------------
        # Estimateurs
        if estimator == 'None':
            pass


        elif estimator == 'LinearRegression':
            
            self.model_regr = make_pipeline(preprocessor, LinearRegression(fit_intercept=True))
            self.evaluation()
            
        elif estimator == 'Ridge':
            
            self.model_regr = make_pipeline(preprocessor, Ridge(alpha=.0001))
            self.evaluation()
            
        elif estimator == 'Lasso':
            
            self.model_regr = make_pipeline(preprocessor, Lasso(alpha=0.0001, max_iter=7000))
            self.evaluation()
            
            
    def evaluation(self,):
        
        # print(self.model_regr)
        
        self.model_regr.fit(self.X_train, self.y_train)
        
        score = self.model_regr.score(self.X_train, self.y_train)  #Score training
        
        self.send_results_train.emit(str(score))
        
        
        
    def testing(self,X_test,y_test):
        
        # print("---------------------------")
        # print(self.model_regr)  
   
        y_pred  = self.model_regr.predict(X_test)
        
        coeff_r2 = r2_score(y_test, y_pred)

        # print("Coeficient de determination R2: ", coeff_r2)
        
        # print(y_pred)
        
        self.send_results_test.emit(str(coeff_r2), y_pred)


        