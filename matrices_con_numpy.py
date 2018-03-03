#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:23:48 2018

@author: juanitobanana
"""

import time
import numpy as np
import pylab as pl


n = int(raw_input())


lista2=[]
for m in range(2,int(n)+1):
    matrizA= np.full((m,m),1)
    matrizB= np.full((m,m),2)
    lista=[]
    for i in range(10):
            t0=time.clock()
            np.dot(matrizA,matrizB)
            tf=time.clock()
            ca=(tf-t0)/(2*int(m)**3)
            lista.append(ca)
    avg=np.average(lista)
    lista2.append(avg)

rango = np.arange(1,int(n),1)
pl.ylabel("y")
pl.xlabel('x')
pl.plot(rango, lista2)
pl.show()
print lista2

