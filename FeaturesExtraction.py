# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:26:39 2022

@author: correa
"""

from biblioteques import *
# from domaine_Frequentiel import *
# from domaine_Temporel import *


class FeaturesExtraction(QObject):
    
    def __init__(self):
    
        super(FeaturesExtraction, self).__init__()
        
        self.dataFrameSignals= pd.DataFrame(None)
        self.width = None
        
        self.fft_values = []
        self.f_width = None
        
        
    def updateAtributs(self,dataFrame,width):
        
        self.dataFrameSignals = dataFrame
        self.width = width
        
        
        
    ##########################################################################
    #Domaine temporel

    def rms(self):             # ************** RMS **************
        
        rms = []
    
        for i in range(0, self.dataFrameSignals.shape[0]):
            
            amplitude = self.dataFrameSignals.iloc[i,:] 
            rms.append(np.sqrt(np.mean(amplitude**2)))
       
        # print("fin de la for ")
        return rms
  
    def Hilbert(self,amplitude):         # *** Tuple Valuer max et temps ***
        
        analytical_signal = hilbert(amplitude)
        amplitude_envelope = np.abs(analytical_signal)
        return amplitude_envelope
    
    
    def value_max(self):
        
        val_max = []
        time_val_max = []
        
        print("Shapeeee of datafs",self.dataFrameSignals.shape[0])
        
        
        for i in range(0, self.dataFrameSignals.shape[0]): 
            
            amplitude = self.dataFrameSignals.iloc[i,:]
            # print(i)
            temp = np.arange(0,self.width,self.width/len(amplitude))
            
            amp = self.Hilbert(amplitude)
            pos = np.where(amp == max(amp))
            tem_pos = temp[pos]
            
            val_max.append(max(amp))
            time_val_max.append(tem_pos[0])
            
        
        return val_max , time_val_max

    
    
    def FWHM(self):      # ******Largeur a mi hauteur LMH  ******
        
        LMH = []    
    
        for i in range(0, self.dataFrameSignals.shape[0]): 
            
            amplitude = self.dataFrameSignals.iloc[i,:]     
    
            x = np.arange(0,self.width,self.width/len(amplitude))
            y = amplitude
            halfmax = y.max() / 2
            maxpos = y.argmax()
            leftpos = (np.abs(y[:maxpos] - halfmax)).argmin()
            rightpos = (np.abs(y[maxpos:] - halfmax)).argmin() + maxpos
            
            fullwidthathalfmax = x[rightpos] - x[leftpos]
            
            LMH.append(fullwidthathalfmax)
            
            #Plot pour visualisation 
            '''
            plt.hlines(halfmax, x[leftpos], x[rightpos], color='crimson', ls=':')
            plt.text(x[maxpos], halfmax, f'{fullwidthathalfmax:.3f}\n', color='crimson', ha='center', va='center')
            plt.ylim(ymin=0)
            '''
            
        return LMH
    
    
    ##########################################################################
    #Domaine frequentiel
    
    def get_fft_values(self):
        
        N = len(self.dataFrameSignals.iloc[0,:])
        t_n = self.width
        T = t_n / N
        f_s = 1/T
        self.fft_values.clear()
        # xf = fftfreq(N, 1 / f_s)
        
        f_values = np.linspace(0.0, 1.0/(2.0*T), N//2)
   
        self.f_width = max(f_values)
        
        
        for i in range(0, self.dataFrameSignals.shape[0]): 
            
            amplitude = self.dataFrameSignals.iloc[i,:] 
            
            fft_values_ = fft(np.array(amplitude))
            
            self.fft_values.append(2.0/N * np.abs(fft_values_[0:N//2]))

        return f_values, self.fft_values
 
    
    def f_rms(self):
        
        f_rms = []
        
        for i in range(len(self.fft_values)): 
            # print(len(self.fft_values))
            f_rms.append(np.sqrt(np.mean(self.fft_values[i]**2)))
        return f_rms

    
    def f_Hilbert(self,amplitude):
        analytical_signal = hilbert(amplitude)
        amplitude_envelope = np.abs(analytical_signal)
        return amplitude_envelope
   
    def f_value_max(self):
        
        fAmpMax =[]
        freqMax= []
        
        for i in range(len(self.fft_values)): 
            
            amplitude = self.fft_values[i]
            temp = np.arange(0,self.f_width,self.f_width/len(amplitude))
            amp = self.f_Hilbert(amplitude)
            pos = np.where(amp == max(amp))
            tem_pos=temp[pos]
            
            fAmpMax.append( max(amp))
            freqMax.append(tem_pos[0])
            
        return fAmpMax , freqMax

    
    def f_FWHM(self):
        
        fullwidthathalfmax =[]
        
        for i in range(len(self.fft_values)): 
            amplitude = self.fft_values[i]
            x = np.arange(0,self.f_width,self.f_width/len(amplitude))
            y = amplitude
            halfmax = y.max() / 2
            maxpos = y.argmax()
            leftpos = (np.abs(y[:maxpos] - halfmax)).argmin()
            rightpos = (np.abs(y[maxpos:] - halfmax)).argmin() + maxpos
            fullwidthathalfmax.append(x[rightpos] - x[leftpos])
      
        
        return fullwidthathalfmax
        

    #####################################################################
    #Statistiques 
    
    def meanVal(self):
        
        meanVal=[]
        for i in range(0, self.dataFrameSignals.shape[0]):       
            amplitude = self.dataFrameSignals.iloc[i,:] 
            meanVal.append(np.nanmean(amplitude))
            
        return meanVal
    
    def medianVal(self):
        
        medianVal=[]
        for i in range(0, self.dataFrameSignals.shape[0]):       
            amplitude = self.dataFrameSignals.iloc[i,:] 
            medianVal.append(np.nanpercentile(amplitude, 50))
            
        return medianVal
    
    def varVal(self):
        
        varVal=[]
        for i in range(0, self.dataFrameSignals.shape[0]):       
            amplitude = self.dataFrameSignals.iloc[i,:] 
            varVal.append(np.nanvar(amplitude))
            
        return varVal
    
    def stdVal(self):
        
        stdVal=[]
        for i in range(0, self.dataFrameSignals.shape[0]):       
            amplitude = self.dataFrameSignals.iloc[i,:] 
            stdVal.append(np.nanstd(amplitude))
            
        return stdVal
        
        

