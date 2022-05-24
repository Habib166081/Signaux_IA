# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:38:58 2021

@author: correa
"""
from biblioteques import *
#from getFrames import get_frames
#from saveImages import save_images
#from fenetreClasses import Ui_Dialog
from TerminateOnFlag import *


class printStep(keras.callbacks.Callback):
    def __init__(self,signal):
        super(printStep, self).__init__()
        self.signal= signal

        
    def on_epoch_begin(self, epoch, logs=None):
        self.epoch_step = 0
    
    def on_batch_end(self, batch, logs=None):
        self.epoch_step += 1
        progress = self.epoch_step / self.params["steps"]
        # print(progress)
        self.signal.emit(progress)

#--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/Worker class for training and inference threading/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--#
class Worker(QObject): #classification class
#    c_preds = QtCore.pyqtSignal(QPixmap,str,str)
    change_col = QtCore.pyqtSignal(int)
    c_graph_info = QtCore.pyqtSignal(list,list,list,list)
    model_is_loaded = QtCore.pyqtSignal()
    actual_epoch= QtCore.pyqtSignal(int)
    percentage_epoch = QtCore.pyqtSignal(float)
    c_conf_info = QtCore.pyqtSignal(np.ndarray,np.ndarray,list)
    done_training = QtCore.pyqtSignal(int)
    
    c_save_labels = QtCore.pyqtSignal(str,list)

    def __init__(self):
        super().__init__()
        self.i_model=VGG16(include_top=False)
        self.c_model=''
        self.c_classes=[]
        self.c_model_name=''
        
        
        self.cwd=os.getcwd()
        #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        #self.cwd = desktop + '/AccessSignaux v2.0'
        
        
        
        self.c_st=0
    #------------------------------------inference tab ---------------------------------------------# 
    def loadmodel(self,path):

        self.c_st=0
        # print('Loading classification Model ')
        self.i_model= load_model(path)
        self.model_is_loaded.emit()
        # print('classification Model Loaded')
        txt_path=path.replace(".h5",".txt")             #so we can read the txt file instead
        with open(txt_path) as f:               
            lines=f.readlines()
            self.i_classes=list(lines[1].split("|"))    #transforming the 
            self.i_classes.pop()
            # print(self.i_classes)
            # print(type(self.i_classes))
            try:
                self.d_classes_color=list(lines[2].split("|"))     
                self.d_classes_color.pop()
            except:
                None
            
            
            
    def c_zero(self):
        self.c_st=0
        
    def c_predictions(self,path,tempo):
        
        
        if path == '':
            show_dialog_modele()
        else:
  
            tempo=tempo
            #classes=['butterfly','cat','dog','horse','spider']   #replace by reading .txt for the according model
            #it=QDirIterator(path,["*.jpg","*.jpeg","*.JPEG","*.png","*.bmp","*.JPG"])
            
            imagelabels=os.listdir(path)   #get all image labes inside my folder
            nbImg = len(imagelabels)
            for c in imagelabels[self.c_st:]:
                
                try:
                    
                    img_path=os.path.join(path,c)     
                    image=QPixmap(img_path)     #Pixmap from our actual image path(it) 
        
                    # load an image from file
                    img = load_img(img_path,target_size=(256,256))
                    img = img_to_array(img)
                    img= np.expand_dims(img, axis=0)  #np.ndarray
                    
                    
                    #prediction for our actual image
                    classif_pred=self.i_model.predict(img/255.0)    #prediction array
                    print("pred",classif_pred)
                    
                    pred=self.i_classes[np.argmax(classif_pred[0])]     #get prediction index with higher prediction % and associates with the class
                    
                    try:
                        color = int(self.d_classes_color[np.argmax(classif_pred)])
                        self.change_col.emit(color)
                    except:
                        pass
                    print("pred",pred)
                    text = f'{self.c_st} / ' + str(nbImg)
                    
                    img2 = load_img(img_path,target_size=(512,512))
                    # plt.figure(figsize=(20,12))
                    # plt.imshow(img)
                    img2 = img_to_array(img2)
                    img2=img2.astype(np.uint8)
                    

                    height, width = (512,512)
                    bytesPerLine = 3 * width
                    img_frame = QImage(img2, width, height, bytesPerLine, QImage.Format_RGB888)
                    qpixmap_img = QPixmap.fromImage(img_frame)

                    # print(image)
                    #self.c_preds.emit(qpixmap_img,pred,text)  #emitting image and predictions results to the main model
                    
                    time.sleep(tempo)
                    self.c_st=self.c_st+1
                except Exception:
                    pass
            self.c_st=0
            
           
                
##########################--------classification training------------------------------------#    

      #--  
    def classification_training(self,isdata_aug,c_dir,c_batch,c_transfer,nb_classes,c_epochs,c_lr,c_patience, _listParameters):
      

        log_val_loss=[]
        log_loss=[]
        
        log_acc=[]
        log_val_acc=[]
        
        if c_patience == 0:
            c_patience = 1000 #test pour ne pas avoir de problemes avec un earlystop trop court quand c_patience=0
        checkpoint_path=f'{self.cwd}/Checkpoints tmp'
        # saved-model-{epoch:02d}-{val_loss:.2f}
        epoch_end_callback = LambdaCallback(on_epoch_end=lambda epoch,logs: [log_val_loss.append(logs.get('val_loss')),log_loss.append(logs.get('loss')),log_acc.append(logs.get('accuracy')), log_val_acc.append(logs.get('val_accuracy')),
                                                                        self.c_graph_info.emit(log_val_loss,log_loss,log_acc,log_val_acc), self.actual_epoch.emit(epoch)])
        
        #epoch_begin_callback = LambdaCallback(on_epoch_begin=lambda epoch: self.actual_epoch.emit(epoch))	
        
        checkpoint=tf.keras.callbacks.ModelCheckpoint( os.path.join(checkpoint_path,"Best_Model.h5"), monitor='val_loss', verbose=1, save_best_only=True,
                                                      save_weights_only=False, mode='auto', save_freq='epoch',options=None)
        
        early_stop=tf.keras.callbacks.EarlyStopping(patience= c_patience)
        
        stopFlag = TerminateOnFlag()
        
        printFlag = printStep(self.percentage_epoch)
        
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=4, verbose=1, min_lr=c_lr/10000)
        # print(f"patience = {c_patience}")

        ###################################################################
        classes = [name for name in os.listdir(c_dir) if os.path.isdir(os.path.join(c_dir, name))]
        
        classes_labels = {classes[i] : i for i in range(len(classes))}
        
        #nb_classes = len(classes)
        
        imgs_all = []
        labels_all = []
        
        
        types = ('*.jpg', '*.jpeg', '*.png', '*.bmp')
        
        
        files_train = []
        labels_train = []
        files_valid = []
        labels_valid = []
        
        for i in range(len(classes)):
            imgs_list = []
            lbls_list = []
            for files in types:
                imgs_list.extend(glob.glob(c_dir+'//'+classes[i]+'//'+files))
            lbls_list = [i] * len(imgs_list)
            nb_val = len(imgs_list)//5
            imgs_list = shuffle(imgs_list)
            files_train += imgs_list[nb_val:]
            labels_train += lbls_list[nb_val:]
            files_valid += imgs_list[:nb_val]
            labels_valid += lbls_list[:nb_val]
        
        files_train, labels_train = shuffle(files_train, labels_train)
        files_valid, labels_valid = shuffle(files_valid, labels_valid)
        


        if isdata_aug == True:        
            params_train = {'dim': (256,256),
                          'batch_size': c_batch,
                          'n_classes': nb_classes,
                          'n_channels': 3,
                          'shuffle': True,
                          'aug':True}
        else:
            params_train = {'dim': (256,256),
                          'batch_size': c_batch,
                          'n_classes': nb_classes,
                          'n_channels': 3,
                          'shuffle': True,
                          'aug':False}
        
        params_valid = {'dim': (256,256),
                      'batch_size': c_batch,
                      'n_classes': nb_classes,
                      'n_channels': 3,
                      'shuffle': False,
                      'aug':False}
        
        train_generator = DataGenerator(files_train, labels_train, **params_train,listParameters=_listParameters)
        val_generator = DataGenerator(files_valid, labels_valid, **params_valid,listParameters=_listParameters)

             
        # print(f"validation gen: {val_generator}")
        if c_transfer == 'MobileNet':
            base_model=MobileNet(include_top=False, weights='imagenet',input_shape=(256, 256, 3))    #en fonction de la caméra definir le input shape
        if c_transfer == 'Oxford VGG16 Model':
            # print("vgg16 selected")
            base_model=VGG16(include_top=False, weights='imagenet',input_shape=(256, 256, 3))    #en fonction de la caméra definir le input shape
        elif c_transfer == 'Google Inception Model':
            # print("inception selected")
            base_model=InceptionV3(include_top=False,input_shape=(256, 256, 3))
        elif c_transfer == 'Microsoft ResNet Model':
            # print("resnet selected")
            base_model=ResNet50(include_top=False,input_shape=(256, 256, 3))
        elif c_transfer == 'Oxford VGG19 Model':
            # print("resnet selected")
            base_model=VGG19(include_top=False,input_shape=(256, 256, 3))
            
            
            
            
    

        #print(c_transfer)
        #base_model.summary()
        
        x = base_model.output
        x = Flatten()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dense(1024, activation='relu')(x)               #2056
        x = Dense(nb_classes, activation="softmax")(x)
        self.c_model = Model(inputs=base_model.input, outputs=x)

        
        self.c_model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=c_lr),
                      metrics=['accuracy'])
        
        
        self.c_model.fit(train_generator,epochs=c_epochs,validation_data=val_generator,callbacks= [epoch_end_callback,reduce_lr,early_stop,checkpoint,stopFlag,printFlag]) #,checkpoint
        self.done_training.emit(1)
        
        self.c_classes = classes
        #self.c_classes=list(train_generator.class_indices)  #get classes w/ the right indexes
        
        # print(self.c_classes)  
        #print(self.c_classes[2])  
        print("Model has been trained")
        
        # self.c_graph_info.emit(acc,val_acc)
        
        
        #confusion matrix:
        print("making confusion mat")
        best_mod=load_model(os.path.join(checkpoint_path,"Best_Model.h5"))
        Y_pred = best_mod.predict(val_generator)
        y_pred = np.argmax(Y_pred, axis=1)
        val_labels = np.array(labels_valid)
        # print(f"Shape: val_labels 1: {val_labels.shape}")
        # print(f"Shape: y_pred 1: {y_pred.shape}")
        val_labels = val_labels[0:len(y_pred)]
        self.c_conf_info.emit(val_labels, y_pred,self.c_classes)  
        # print(f"labels_valid: {type(val_labels)}\ny_pred: {type(y_pred)}")
        # print(f"\nShapes: val_labels: {val_labels.shape}\ny_pred: {y_pred.shape}")

        
        
        
    def save_c_model(self,path):

        try:
            best_model_dir=f'{self.cwd}/Checkpoints tmp/Best_Model.h5'
            shutil.move(best_model_dir,f"{path}")
            # self.c_model.save(f"{path}.h5")     #save the model stored in a global variable with the name we gave it
            print("Model has been saved")
        
            
        
            f=open(f"{path[:-3]}.txt","w")           #creates a .txt with the same name as the model
            f.write("classification\n")        #type of model
            
            
            for c in self.c_classes:            #classes of this model --> "|" separator
                f.write(f"{c}|")
    
            f.close()
            
            
            self.c_save_labels.emit(path,self.c_classes)
        except: 
            print("Veuillez entraîner un modèle")
            pass
        



      

      

      

        

    