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

def multiplicacion(matrizA, matrizB, h):
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
lista2=[]
for m in range(2,int(n)+1):
    matrizA=crear_matriz1(int(m),int(m))
    matrizB=crear_matriz2(int(m),int(m))
    lista=[]
    for i in range(10):
            t0=time.clock()
            multiplicacion(matrizA,matrizB,m)
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
    