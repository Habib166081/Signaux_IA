# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:15:32 2022

@author: correa
"""

from biblioteques import *

class ClassificationML (QObject):
    
    send_results = QtCore.pyqtSignal(str,object,object,object,object,object)  
    
    
    def __init__(self):
    
        super(ClassificationML, self).__init__()
        
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        
    def training(self, transformer,estimator, dataFrame):
        
        train_set, test_set = train_test_split(dataFrame,test_size=0.2, random_state = 0)

        self.X_train = train_set.drop('Target', axis=1)
        self.y_train = train_set['Target']
        
        
        self.X_test = test_set.drop('Target', axis=1)
        self.y_test = test_set['Target']
        
        #---------------------------------------------------------------------------
        # Trasformeurs
        
        if transformer == 'None': 
            
            preprocessor = None
            
        elif transformer == 'PolynomialFeatures':
         
            preprocessor = make_pipeline(PolynomialFeatures(2, include_bias=False), SelectKBest(f_classif, k=10))
        
        #---------------------------------------------------------------------------
        # Estimateurs
        
        if estimator == 'RandomForest':
        
            RandomForest = make_pipeline(preprocessor, RandomForestClassifier(random_state=0))      
            self.evaluation(RandomForest)

        elif estimator == 'AdaBoost':
 
            AdaBoost = make_pipeline(preprocessor, AdaBoostClassifier(random_state=0))
            self.evaluation(AdaBoost)
            
        elif estimator == 'SVM':
            
            SVM = make_pipeline(preprocessor, StandardScaler(), SVC(random_state=0))
            self.evaluation(SVM)
            
        elif estimator == 'KNN':
        
            KNN = make_pipeline(preprocessor, StandardScaler(), KNeighborsClassifier())
            self.evaluation(KNN)
          
        elif estimator =='LogisticRegression':
            
            LogisticRegression = make_pipeline(preprocessor, StandardScaler(),LogisticRegression(random_state=0))
            self.evaluation(LogisticRegression)
    
    def evaluation(self, model):
        
        # print('je suis dans evaluation')
    
        model.fit(self.X_train, self.y_train)
        ypred = model.predict(self.X_test)
        

        
        N, train_score, val_score = learning_curve(model, self.X_train, self.y_train,
                                                  cv=4, scoring=None,
                                                  train_sizes=np.linspace(0.1, 1, 10))
        

        
        self.send_results.emit(str(classification_report(self.y_test, ypred)),
                               N, train_score.mean(axis=1),val_score.mean(axis=1),
                               self.y_test, ypred)
        
        


        

    
    