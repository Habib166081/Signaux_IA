# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:22:45 2022

@author: valentin
"""

from biblioteques import *

class ClassificationWS (QObject):

    send_results_train = QtCore.pyqtSignal(str,np.ndarray,np.ndarray,object)
    send_results_test = QtCore.pyqtSignal(str,np.ndarray,np.ndarray,object)
    c_graph_info = QtCore.pyqtSignal(list,list,list,list)
   
    
    def __init__(self):
    
        super(ClassificationWS, self).__init__()
        
        self.X_train = None
        self.y_train = None
        
        self.use_cuda = torch.cuda.is_available()

        
        self.model_regr = None

    def training(self, dataFrameX,dataFrameY, J,Q,epochs,lr,neur,batch):
        
        self.J = J
        self.Q = Q

        self.X_train = torch.from_numpy(dataFrameX.to_numpy().astype(np.float32)).contiguous()
        self.y_train = dataFrameY.to_numpy()
        
        self.le = LabelEncoder()
        self.le.fit(self.y_train)
        self.y_train = self.le.transform(self.y_train)
        
        scattering = Scattering1D(J, self.X_train.shape[1], Q)
        
        if self.use_cuda:
            scattering.cuda()
            self.X_train = self.X_train.cuda()
        
        Sx_all = scattering.forward(self.X_train)
        
        log_eps = 1e-6

        Sx_all = Sx_all[:,1:,:]
        Sx_all = torch.log(torch.abs(Sx_all) + log_eps)
        Sx_all = torch.mean(Sx_all, dim=-1)
        
        self.mu_tr = Sx_all.mean(dim=0)
        self.std_tr = Sx_all.std(dim=0)
        Sx_tr = (Sx_all - self.mu_tr) / self.std_tr
        
        num_input = Sx_tr.shape[-1]
        ytorch = torch.from_numpy(self.y_train)

        num_classes = ytorch.unique().numel()

        Sx_tr_np = Sx_tr.cpu().numpy()

        self.input, self.target = shuffle(Sx_tr_np, self.y_train, random_state=0)

        self.target = keras.utils.to_categorical(self.target)
                
        self.model = keras.Sequential([
          layers.Dense(neur, activation='relu', input_shape = [num_input]),
          layers.Dropout(0.2),
          layers.Dense(num_classes, activation='softmax')
        ])

        
        self.model.compile(loss='categorical_crossentropy',
                      optimizer=keras.optimizers.Adam(learning_rate=lr),
                      metrics=['accuracy'])
        
        log_val_loss=[]
        log_loss=[]
        
        log_acc=[]
        log_val_acc=[]
    
        epoch_end_callback = LambdaCallback(on_epoch_end=lambda epoch,logs: [log_val_loss.append(logs.get('val_loss')),log_loss.append(logs.get('loss')),log_acc.append(logs.get('accuracy')), log_val_acc.append(logs.get('val_accuracy')),
                                                                        self.c_graph_info.emit(log_val_loss,log_loss,log_acc,log_val_acc)])
        history = self.model.fit(
          self.input, self.target,
          epochs=epochs, validation_split = 0.2, verbose=1,batch_size=batch,callbacks=epoch_end_callback)
        
        pred = self.model.predict(self.input)
        
        pred_index = np.argmax(pred, axis=1)
        
        targetlab = np.argmax(self.target, axis=1)
            
        rep = str(classification_report(np.array(self.le.inverse_transform(targetlab),dtype=str).tolist(), np.array(self.le.inverse_transform(pred_index),dtype=str).tolist()))

        
        self.send_results_train.emit(rep,pred_index,targetlab,self.le)


    def test(self, dataFrameX,dataFrameY):
        self.X_test = torch.from_numpy(dataFrameX.to_numpy().astype(np.float32)).contiguous()
        self.y_test = dataFrameY.to_numpy()
        self.y_test = self.le.transform(self.y_test)
        
        scattering = Scattering1D(self.J, self.X_train.shape[1], self.Q)
        
        if self.use_cuda:
            scattering.cuda()
            self.X_test = self.X_test.cuda()
        
        Sx_all = scattering.forward(self.X_test)
        
        log_eps = 1e-6

        Sx_all = Sx_all[:,1:,:]
        Sx_all = torch.log(torch.abs(Sx_all) + log_eps)
        Sx_all = torch.mean(Sx_all, dim=-1)
        
        Sx_tr = (Sx_all - self.mu_tr) / self.std_tr
        Sx_tr_np = Sx_tr.cpu().numpy()
        
        pred = self.model.predict(Sx_tr_np)
        pred_index = np.argmax(pred, axis=1)
        
        rep = str(classification_report(np.array(self.le.inverse_transform(self.y_test),dtype=str).tolist(), np.array(self.le.inverse_transform(pred_index),dtype=str).tolist()))
                    
        self.send_results_test.emit(rep,pred_index,self.y_test,self.le)
        
    def saving(self,file):
        self.model.save(file)
