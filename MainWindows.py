# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 13:58:08 2022

@author: correa
"""


from biblioteques import *

from ClassificationML import ClassificationML
from FeaturesExtraction import FeaturesExtraction
from RegressionML import RegressionML

    
class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    
    send_data_classif = QtCore.pyqtSignal(str,str, object)  
    
    send_data_extractor =  QtCore.pyqtSignal(object, int)  
    
    send_data_concatenate = QtCore.pyqtSignal(list,list, list,list)  

    send_data_regression = QtCore.pyqtSignal(str,str, object) 
    
    send_data_test_reg = QtCore.pyqtSignal(object,object) 
    
    def __init__(self):
    
        super(MainWindows, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1020, 825)
        self.statusConcat.hide()
        
        self.cwd = os.getcwd()
        
        self.listLoadData.verticalScrollBar().valueChanged.connect(self.listTargets.verticalScrollBar().setValue)
        self.listTargets.verticalScrollBar().valueChanged.connect(self.listLoadData.verticalScrollBar().setValue)
        
        self.listLoadData_test.verticalScrollBar().valueChanged.connect(self.listTargets_test.verticalScrollBar().setValue)
        self.listTargets_test.verticalScrollBar().valueChanged.connect(self.listLoadData_test.verticalScrollBar().setValue)

        self.width = 25

        ######################################################################
        #Classification instance + thread + signals
        self.ClassifML = ClassificationML()
        
        self.training_Classification_thread = QThread(parent=self) 
        self.ClassifML.moveToThread(self.training_Classification_thread)
        self.training_Classification_thread.start()
        
        self.send_data_classif.connect(self.ClassifML.training)
        self.ClassifML.send_results.connect(self.resultTraining)
        
        self.trainButton.clicked.connect(self.training_classif)
        
        ######################################################################
        #Regression instance + thread +signals
        self.RegressML = RegressionML()
        
        self.training_Regression_thread = QThread(parent=self) 
        self.RegressML.moveToThread(self.training_Regression_thread)
        self.training_Regression_thread.start()
        
        self.send_data_regression.connect(self.RegressML.training)
        self.send_data_test_reg.connect(self.RegressML.testing)
        
        
        self.RegressML.send_results_train.connect(lambda x:self.outputText_2.setText('Coef. R2 train: '+ x))
        
        self.RegressML.send_results_test.connect(self.resulTesting_regression)
                                
        self.trainRegreButton.clicked.connect(self.training_regression)
        
        self.testRegressionButton.clicked.connect(self.testRegression)
        
        self.featsTestPlot_combo.activated.connect(self.regression_graphFeats)
        
        
        ######################################################################
        #Load data tab
        
        self.dataFrameSignals = pd.DataFrame(None)
        self.dataFrameSignalsTargets = pd.DataFrame(None)
        
        self.dataFrameSignals_test = pd.DataFrame(None)
        self.dataFrameSignalsTargets_test = pd.DataFrame(None)

        self.openButton_load.clicked.connect(self.openData)
        self.plotSignalButton.clicked.connect(self.plot_signals)
        self.clearSignalButton.clicked.connect(self.clear_Graph)
 
    
        self.concatenateButton.clicked.connect(self.send_Concatenation)
        self.resetButton.clicked.connect(self.reset)
        
        self.listLinesTargets = []
        self.listLinesTargets_test = []
        
        self.files_train_ToConcatenate = []
        self.files_test_ToConcatenate = []
        
        
        self.workerConcat = Concatenate()

        self.concatenate_thread = QThread(parent=self) 
        self.workerConcat.moveToThread(self.concatenate_thread)
        self.concatenate_thread.start()
        
        self.send_data_concatenate.connect(self.workerConcat.concatenate)
        self.workerConcat.send_data_mainwindows.connect(self.updateSignals)
        
        
        ######################################################################
        #Feature extraction tabs ; intance + thread +signal
        
        self.dataFrameFeats_train = pd.DataFrame(None)
        self.dataFrameFeats_test = pd.DataFrame(None)
        
        self.Extractor = FeaturesExtraction() 
        self.extractor_thread = QThread(parent=self) 
        self.Extractor.moveToThread(self.extractor_thread)
        self.extractor_thread.start()
        
        self.send_data_extractor.connect(self.Extractor.updateAtributs)
        self.generateButton.clicked.connect(self.generateFeatures)
        
        self.saveButton.clicked.connect(self.saveFeatures)
 
        ######################################################################
        #Features visualization tabs
        
        self.openButton_featFile.clicked.connect(self.loadFeatures)
        
        self.visualDataX.activated.connect(self.dataVisualization)
        self.visualDataY.activated.connect(self.dataVisualization)

   

    def initializeComboBox(self):
        
        self.visualDataX.clear()
        self.visualDataY.clear()
        
        self.visualDataX.addItems(self.dataFrameFeats_train.columns)
        self.visualDataY.addItems(self.dataFrameFeats_train.columns)
        
        self.visualDataX.setCurrentText(self.dataFrameFeats_train.columns[1])
        self.visualDataY.setCurrentText(self.dataFrameFeats_train.columns[1])


    def dataVisualization(self): 
        
        x = self.visualDataX.currentIndex()
        y = self.visualDataY.currentIndex()
        self.visualData.plot_graph_data(np.array(self.dataFrameFeats_train.iloc[:,x]),np.array(self.dataFrameFeats_train.iloc[:,y]))

        
    #################################################################
    #Load data Tab
     
    #Read a file CSV (DateFrame)
    
    def openData(self):
        
        x = TableModel(self.dataFrameSignals)
        self.tableView_data.setModel(x)
        
        if self.checkloadTrain.isChecked():
        
            dialog = QFileDialog(self)
            dialog.setNameFilter("Choisir un fichier .CSV: (*.csv)")
            dialog.setViewMode(QFileDialog.List)
            dialog.setFileMode(QFileDialog.ExistingFiles)
            
            if dialog.exec_():
                fileNames = dialog.selectedFiles()
    
                for i in range(len(fileNames)):
                    
                    
                    fileNameTrain = fileNames[i].split('/')[-1]
                    
                    # self.fileNameTrain = fileNameTrain.split('.')[0]
            
                    self.files_train_ToConcatenate.append(fileNameTrain)        
            
                    self.fileLoadedPath.setText(fileNameTrain)
                    
                    self.dataFrameSignals = pd.read_csv(fileNameTrain,header=None)
                    
                    self.dataFrameSignals = self.dataFrameSignals.append(self.dataFrameSignals)
                    
                    x = TableModel(self.dataFrameSignals)
                    
                    self.tableView_data.setModel(x)
                    self.listLoadData.addItem(fileNameTrain)
                    
                    lineEdit = QLineEdit()
                    lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
                    lineEdit.setStyleSheet('border-bottom: 1px solid white;')
                    prov = QListWidgetItem()
                    
                    self.listLinesTargets.append(lineEdit)
                    
                    self.listTargets.addItem(prov)
                    self.listTargets.setItemWidget(prov,lineEdit)
        
        else: 
            
            #Pour vider le tableau avant d'afficher les donnes de test
            x = TableModel(self.dataFrameSignals_test)
            self.tableView_data.setModel(x)

            dialog = QFileDialog(self)
            dialog.setNameFilter("Choisir un fichier .CSV: (*.csv)")
            dialog.setViewMode(QFileDialog.List)
            dialog.setFileMode(QFileDialog.ExistingFiles)
            
            if dialog.exec_():
                fileNames = dialog.selectedFiles()
    
                for i in range(len(fileNames)):
                    
                    
                    fileName = fileNames[i].split('/')[-1]
                    
                    # self.fileName = fileName.split('.')[0]
            
                    self.files_test_ToConcatenate.append(fileName)        
            
                    self.fileLoadedPath.setText(fileName)
                    
                    self.dataFrameSignals_test = pd.read_csv(fileName,header=None)
                    
                    self.dataFrameSignals_test = self.dataFrameSignals_test.append(self.dataFrameSignals_test)
                    
                    x = TableModel(self.dataFrameSignals_test)
                    
                    self.tableView_data.setModel(x)
                    self.listLoadData_test.addItem(fileName)
                    
                    lineEdit = QLineEdit()
                    lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
                    
                    lineEdit.setStyleSheet('border-bottom: 1px solid white;')
                    prov = QListWidgetItem()
                    
                    self.listLinesTargets_test.append(lineEdit)
                    
                    self.listTargets_test.addItem(prov)
                    self.listTargets_test.setItemWidget(prov,lineEdit)
            
            
    def reset(self):
        
        #Nettoyage des variables et réinitialisation d'objets d'interface
        
        #VARIABLES
        self.dataFrameSignals = pd.DataFrame(None)
        self.dataFrameSignalsTargets = pd.DataFrame(None)
        
        self.dataFrameSignals_test = pd.DataFrame(None)
        self.dataFrameSignalsTargets_test = pd.DataFrame(None)
        
        self.files_train_ToConcatenate.clear()
        self.files_test_ToConcatenate.clear()
        self.listLinesTargets_test.clear()
        
        
        #OBJECTS
        
        self.statusConcat.setText('Concaténation en cours...')
        self.listLoadData.clear()
        self.listLoadData_test.clear()
        self.listTargets.clear()
        self.listTargets_test.clear()
        
        self.fileLoadedPath.setText('')
        
        x = TableModel(self.dataFrameSignals)
        self.tableView_data.setModel(x)
           

    def send_Concatenation(self):
        
        
        # path_file = self.cwd + '/Signals_concatenated.csv'
        # self.dataFrameSignals.to_csv(path_file, header=None, index=False)
        
        self.concatenate_thread.start()
        self.send_data_concatenate.emit(self.listLinesTargets, self.files_train_ToConcatenate,self.listLinesTargets_test,self.files_test_ToConcatenate)
    
    def updateSignals(self,dataFrameConcatenated_train , dataFrameConcatenated_test):
        
        #Si l'on fait la concatenation des signaux, on met a jour le dataFrameSignals
        
        if self.listLoadData.count()==0:
            print('Il n y pas des fichier Train a concatener')
            pass
        else:
            #Train
            self.dataFrameSignalsTargets = dataFrameConcatenated_train['Target']
            dataFrameConcatenated_train = dataFrameConcatenated_train.drop(columns=['Target'])
            self.dataFrameSignals = dataFrameConcatenated_train
        
        if self.listLoadData_test.count()==0:
            print('Il n y pas des fichier Test a concatener')
            pass
        else:
            #Test
            self.dataFrameSignalsTargets_test = dataFrameConcatenated_test['Target']
            dataFrameConcatenated_test = dataFrameConcatenated_test.drop(columns=['Target'])
            self.dataFrameSignals_test = dataFrameConcatenated_test

       
        self.concatenate_thread.quit()
        self.concatenate_thread.wait()
        
        self.statusConcat.setStyleSheet('color:#49dc00;')
        self.statusConcat.setText('Concaténation terminée !')
    
    def plot_signals(self):
        
        if self.tableView_data.currentIndex().row() == -1:
            pass
        else: 
            row = self.tableView_data.currentIndex().row()
        
            self.plotOriginalSignals.plot_original_Signal(self.dataFrameSignals.iloc[row,:],self.width,row)
            
    def clear_Graph(self):
        
        self.plotOriginalSignals.clear_graph()
    
        
    
    
    ################################################################## 
    #Machine Learning Tab

    #Sub-tab : Classification
    
    def training_classif(self):
        
        self.training_Classification_thread.start()
        self.send_data_classif.emit(self.transformerCombo.currentText(),self.estimatorCombo.currentText(),self.dataFrameFeats_train)
    
    def resultTraining(self,report,
                       N,train_score,val_score,
                       y_test ,y_pred):
        
        self.outputText.setText(report)

        self.graphScore.plot_graph(N,train_score,val_score)
        
        

        labels = list(set((map(float, self.dataFrameSignalsTargets.tolist()))))
        
        self.graphConfusion.plot_conf_mat(y_test ,y_pred, labels)
        
        self.training_Classification_thread.quit()
        self.training_Classification_thread.wait()
        
    #Sub-tab : Regression  
    
    def training_regression(self):
        
        
        self.graphResultRegression.clear_graph()
        self.graphTestRegression.clear_graph()
        
        self.training_Regression_thread.start()
        self.send_data_regression.emit(self.transformerCombo_2.currentText(),self.estimatorCombo_2.currentText(),self.dataFrameFeats_train)
     
    def resultTraining_regre(self):
        
        self.outputText_2.setText('Score train :' + score)


        self.training_Regression_thread.quit()
        self.training_Regression_thread.wait()
    
    def testRegression(self):
        
        self.training_Regression_thread.start()
        
        if len(self.dataFrameFeats_test)==0 :  #Si on avait deja extait des caracts. avant 
        
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Choisir un fichier de test .CSV:', f"{self.cwd}" , filter="(**.csv )")
            
            if file[0] != '': 
                
                data_test = pd.read_csv(file[0])
                # print(self.data_test.head())
                
                self.X_test_regr = data_test.drop('Target', axis=1)
                self.y_test_regr = data_test['Target']
                
                self.send_data_test_reg.emit(self.X_test_regr, self.y_test_regr)

            else: 
                print("Veuillez sélectionner un fichier")
    
           
            
        else :                                 #Si on n'avait pas deja extait des caracts. avant 
            print('Caracts')
            
            self.X_test_regr = dataFrameFeats_test.drop('Target', axis=1)
            self.y_test_regr = dataFrameFeats_test['Target']
            
            self.send_data_test_reg.emit(self.X_test_regr, self.y_test_regr)
            
      
        
    def resulTesting_regression(self,coef_R2_test ,y_pred):
       
        self.outputText_2.setText( self.outputText_2.toPlainText() + '\n' + 'Coef. R2 test: ' + coef_R2_test ) 
        
        self.y_pred_regression = y_pred
        
        self.featsTestPlot_combo.clear()
        
        self.featsTestPlot_combo.addItems(self.X_test_regr.columns)
        self.featsTestPlot_combo.setCurrentText(self.X_test_regr.columns[1])

        self.graphResultRegression.plot_scatter_regreResult(self.y_test_regr,self.y_pred_regression)

        self.training_Regression_thread.quit()
        self.training_Regression_thread.wait()
        
    def regression_graphFeats(self):   
        
        x = self.featsTestPlot_combo.currentIndex()
        self.graphTestRegression.plot_scatter_regreTest(np.array(self.X_test_regr.iloc[:,x]), np.array(self.y_test_regr),np.array(self.y_pred_regression))     
        
    ################################################################## 
    # Features extraction tab
    
    def generateFeatures(self):
        
        self.dataFrameFeatures = pd.DataFrame(None) #Pour effacer le dataframe

        data_train_test = self.dataFrameSignals.append(self.dataFrameSignals_test)

        targets_train_test = self.dataFrameSignalsTargets.append(self.dataFrameSignalsTargets_test)

        self.send_data_extractor.emit(data_train_test,self.width)
  
        time.sleep(0.1)
        
        xf , fft_values = self.Extractor.get_fft_values()     
        
        # Si l'on veut faire un graph    
        
        # print(f_values)
        # print("-------------------")
        # print(fft_values)
        
        # plt.figure()
        # plt.plot(xf,abs(fft_values[0]))
        # plt.xlim(0,20)
        # plt.show()

        
        ##################################################
        #Features time domain
        if self.check_t_Amp.isChecked(): 
                    
            ampMax, timeMax = self.Extractor.value_max()  
            
            self.dataFrameFeatures['t_AmpMax'] = ampMax
            self.dataFrameFeatures['t_TimeAmpMax'] = timeMax
            

        if self.check_t_LMH.isChecked(): 
            
            LMH = self.Extractor.FWHM()
            
            self.dataFrameFeatures['t_LMH'] = LMH
            
        if self.check_t_RMS.isChecked(): 
            
            rms = self.Extractor.rms()
            
            self.dataFrameFeatures['t_RMS'] = rms
            
        #################################################
        #Features frequency domain
        
        if self.check_f_Amp.isChecked(): 
            
            f_AmpMax , freqMax = self.Extractor.f_value_max()
            
            # print(len(f_Ampmax))
            
            self.dataFrameFeatures['f_AmpMax'] = f_AmpMax
            self.dataFrameFeatures['f_FreqAmpMax'] = freqMax

        if self.check_f_LMH.isChecked(): 
            
            f_LMH = self.Extractor.f_FWHM()
            self.dataFrameFeatures['f_LMH'] = f_LMH  
        
        if self.check_f_RMS.isChecked(): 
            
            f_rms = self.Extractor.f_rms()
            self.dataFrameFeatures['f_RMS'] = f_rms    
        
        #################################################
        #Features statistiques
        
        if self.check_mean.isChecked(): 
            
            mean = self.Extractor.meanVal()
            self.dataFrameFeatures['mean'] = mean 
            
        if self.check_madian.isChecked(): 
            
            median = self.Extractor.medianVal()
            self.dataFrameFeatures['median'] = median 

        if self.check_std.isChecked(): 
            
            std = self.Extractor.stdVal()
            self.dataFrameFeatures['std'] = std 
            
        if self.check_var.isChecked(): 
            
            var = self.Extractor.varVal()
            self.dataFrameFeatures['var'] = var 
        
        ###################################################
        #Visualization in table
 
        self.dataFrameFeatures['Target'] = list(map(float, targets_train_test.tolist()))
        
        data = TableModel(self.dataFrameFeatures)
        self.tableView_features.setModel(data)
        

    
    def saveFeatures(self):
        
        self.dataFrameFeats_train = self.dataFrameFeatures.iloc[:self.dataFrameSignals.shape[0],:]
        
        self.dataFrameFeats_test = self.dataFrameFeatures.iloc[self.dataFrameSignals.shape[0]:,:]
        
        del self.dataFrameFeatures
        
        self.dataFrameFeats_train.to_csv(self.cwd + '/sig_Feautures_train.csv',index=False)
        
        self.dataFrameFeats_test.to_csv(self.cwd + '/sig_Feautures_test.csv',index=False)
        
        self.initializeComboBox()
        
        self.matrixCorrelation.plot_corr_mat(self.dataFrameFeats_train)
        
        
        
    ##########################################################################
    def loadFeatures (self):
        
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Choisir un fichier des caracteristiques .CSV:', f"{self.cwd}" , filter="(**.csv )")
        
        if file[0] != '': 
        
            fileName = file[0].split('/')[-1]
            self.fileName = fileName.split('.')[0]

            self.featFile_path_feats.setText(file[0])
            
            self.dataFrameFeats_train = pd.read_csv(file[0])
        else: 
            print("Veuillez sélectionner un fichier")
            
        self.initializeComboBox()
        
        # print(self.dataFrameFeatures.head())
        
        self.matrixCorrelation.plot_corr_mat(self.dataFrameFeats_train)
        
        
        
        
        
        
        
        
        
        
class Concatenate(QObject):
    
    send_data_mainwindows = QtCore.pyqtSignal(object,object) 
    
    def __init__(self):

        super(Concatenate, self).__init__()
    
    def concatenate(self,listLinesTargets,files_train_ToConcatenate,listLinesTargets_tes,files_test_ToConcatenate):
        
        cwd = os.getcwd()
        
        items_train = []
        items_test = []
           
        dataFrameConcatenated_train =  pd.DataFrame(None)
        dataFrameConcatenated_test =  pd.DataFrame(None)
        
        #Train
        
        for x in range(len(listLinesTargets)):
            
            items_train.append(listLinesTargets[x].text())  
            
            dat = pd.read_csv(cwd +'/'+ files_train_ToConcatenate[x],header=None)
            
            t = items_train[x]

            target = [t for x in range(dat.shape[0])]
            
            dat['Target'] = target
            
            dataFrameConcatenated_train = dataFrameConcatenated_train.append(dat)
       
        #Test
        
        for x in range(len(listLinesTargets_tes)):
             
             items_test.append(listLinesTargets_tes[x].text())  
             
             datTest = pd.read_csv(cwd +'/'+ files_test_ToConcatenate[x],header=None)
             
             t = items_test[x]
 
             target = [t for x in range(datTest.shape[0])]
             
             datTest['Target'] = target
             
             dataFrameConcatenated_test = dataFrameConcatenated_test.append(datTest)



        path_file_train = cwd + '/signauxConcatenes_train.csv'
        
        path_file_test = cwd + '/signauxConcatenes_test.csv'

        
        dataFrameConcatenated_train.to_csv(path_file_train, header=None, index=False)
        
        dataFrameConcatenated_test.to_csv(path_file_test, header=None, index=False)
        
        self.send_data_mainwindows.emit(dataFrameConcatenated_train,dataFrameConcatenated_test)
    
    