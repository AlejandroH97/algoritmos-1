#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:59:03 2018

@author: juanitobanana
"""

import time
import numpy as np
import pylab as pl

n = raw_input()



def crear_matriz1(numero_filas, numero_columnas):
    matriz = []
    for i in range(numero_filas):
            matriz.append([])
            for j in range(numero_columnas):
                    n = 1
                    matriz[i].append(n)
    return matriz

def crear_matriz2(numero_filas, numero_columnas):
    matriz = []
    for i in range(numero_filas):
            matriz.append([])
            for j in range(numero_columnas):
                    n = 2
                    matriz[i].append(n)
    return matriz


lista2=[]
for h in range(2,int(n)):
    matrizA= crear_matriz1(h,h)
    matrizB= crear_matriz2(h,h)
    lista=[]
    for i in range(10):
        t0=time.clock()
        def multiplicacion():
            c=[]
            for k in range(0,h):
                aux = []
                for j in range(0,h):
                    aux1=0
                    for i in range(0,h):
                        aux1=aux1+(matrizA[k][i]*matrizB[i][j])
                        aux.append(aux1)
                        c.append(aux)
            return c
        tf=time.clock()
        lista.append(tf-t0)
        avg=np.average(lista)
    lista2.append(avg)
rango = np.arange(1,int(n)-1,1)
pl.ylabel("y")
pl.xlabel('x')
pl.plot(rango, lista2)
pl.show()
print lista2