# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:36:17 2022

@author: valentin
"""

import scipy.io
import pandas as pd

m = scipy.io.loadmat('G1.mat')

t= m['t']
print(t[0,-1])
# data = m['G1']

# g1 = pd.DataFrame(data)

# g1.to_csv('g1.csv',index=False,header=False)

# m = scipy.io.loadmat('G2.mat')

# data = m['G2']

# g1 = pd.DataFrame(data)

# g1.to_csv('g2.csv',index=False,header=False)


# m = scipy.io.loadmat('G3.mat')

# data = m['G3']

# g1 = pd.DataFrame(data)

# g1.to_csv('g3.csv',index=False,header=False)

# m = scipy.io.loadmat('G4.mat')

# data = m['G4']

# g1 = pd.DataFrame(data)

# g1.to_csv('g4.csv',index=False,header=False)

# m = scipy.io.loadmat('G5.mat')

# data = m['G5']

# g1 = pd.DataFrame(data)

# g1.to_csv('g5.csv',index=False,header=False)

# m = scipy.io.loadmat('G6.mat')

# data = m['G6']

# g1 = pd.DataFrame(data)

# g1.to_csv('g6.csv',index=False,header=False)

m = scipy.io.loadmat('G1V.mat')

data = m['G1V']

g1 = pd.DataFrame(data)

g1.to_csv('g1v.csv',index=False,header=False)

m = scipy.io.loadmat('G2V.mat')

data = m['G2V']

g1 = pd.DataFrame(data)

g1.to_csv('g2v.csv',index=False,header=False)


m = scipy.io.loadmat('G3V.mat')

data = m['G3V']

g1 = pd.DataFrame(data)

g1.to_csv('g3v.csv',index=False,header=False)

m = scipy.io.loadmat('G4V.mat')

data = m['G4V']

g1 = pd.DataFrame(data)

g1.to_csv('g4v.csv',index=False,header=False)

m = scipy.io.loadmat('G5V.mat')

data = m['G5V']

g1 = pd.DataFrame(data)

g1.to_csv('g5v.csv',index=False,header=False)

m = scipy.io.loadmat('G6V.mat')

data = m['G6V']

g1 = pd.DataFrame(data)

g1.to_csv('g6v.csv',index=False,header=False)
