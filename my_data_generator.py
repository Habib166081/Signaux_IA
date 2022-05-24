import numpy as np
import cv2
import tensorflow as tf

class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, files, labels, batch_size=8, dim=(256,256), n_channels=3,
                 n_classes=3, shuffle=False, aug=False,listParameters=[None]*13):
        self.dim = dim
        self.batch_size = batch_size
        self.labels = labels
        self.files = files
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.aug = aug
        self.on_epoch_end()
        
        
        ######################################################################
        #Transformations choises
        #[rot90,rot180,rot270,FlipH,FlipV,Clip1,upper_ct,lower_ct,Clip2,upper_br,lower_br,GausBlur,kernel]
        
        self.Rot90 = listParameters[0]
        self.Rot180 = listParameters[1]
        self.Rot270 = listParameters[2]
        
        self.FlipH = listParameters[3]
        self.FlipV = listParameters[4]
        
        self.Clip1 = listParameters[5]
        self.upper_ct = listParameters[6]
        self.lower_ct = listParameters[7]

        self.Clip2 = listParameters[8]
        self.upper_br = listParameters[9]       
        self.lower_br = listParameters[10]
        
        self.GausBlur = listParameters[11]
        self.kernel = listParameters[12]
        
        ######################################################################
        
    def __len__(self):
        return int(np.floor(len(self.files) / self.batch_size))

    def __getitem__(self, index):
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        files_temp = [self.files[k] for k in indexes]
        labels_temp = [self.labels[k] for k in indexes]
        X, y = self.__data_generation(files_temp, labels_temp)

        return X, y

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.files))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, files_temp, labels_temp):
        X = np.empty((self.batch_size, *self.dim, self.n_channels))
        y = np.empty((self.batch_size), dtype=int)
        

        for i in range(len(files_temp)):
            img = cv2.imread(files_temp[i])
            if img is None:
                print('On est en my_data_generator !!')
                print(files_temp[i])
                if i>0:
                    img = cv2.imread(files_temp[i-1])
                else:
                    img = cv2.imread(files_temp[i+1])
            img = img[:,:,0:self.n_channels]
            img = img.astype('float32')
            
            if self.aug == True:
                
                if self.Clip1:
                    if np.random.uniform(0,1) >= (0.5):
                        delta = np.random.uniform(self.lower_br, self.upper_br)
                        img = np.clip(img + delta, 0, 255)
                
                if self.Clip2:
                    if np.random.uniform(0,1) >= (0.5):
                        factor = np.random.uniform(self.lower_ct, self.upper_ct)
                        img = np.clip(127.5 + factor * (img - 127.5), 0, 255)
                    
                if self.Rot90:
                    if np.random.uniform(0,1) >= (0.5):
                        img = np.rot90(img)
                    
                if self.Rot180:  
                    if np.random.uniform(0,1) >= (0.5):
                        img = np.rot90(np.rot90(img))
                        
                if self.Rot270:                          
                    if np.random.uniform(0,1) >= (0.5):
                        img = np.rot90(np.rot90(np.rot90(img)))             
                
                if self.FlipV:
                    if np.random.uniform(0,1) >= (0.5):
                          img = np.flipud(img)
                
                if self.FlipH:     
                    if np.random.uniform(0,1) >= (0.5):
                        img = np.fliplr(img)
                        
                if self.GausBlur:

                    if np.random.uniform(0,1) >= (0.5):
                        img = cv2.GaussianBlur(img, self.kernel,cv2.BORDER_DEFAULT)
            
            img = cv2.resize(img, self.dim)
            img = img/255.0

            X[i,] = img
            y[i] = labels_temp[i]
                        
        return X, tf.keras.utils.to_categorical(y, num_classes=self.n_classes)