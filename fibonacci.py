
import time
import numpy as np
import pylab as pl



def fibo_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
       return 1
    return fibo_recursivo(n-1) + fibo_recursivo(n-2)

def fibo_iterado(n):
    if n== 0:
        return 0
    a,b = 0,1
    for i in range(1, n):
        a, b = b, a + b
    return b



lista_fib=[]
lista_fibr=[]
t0 = time.clock()
for i in range (1, 35):
    k = fibo_iterado(i)
    tf = time.clock()
    lista_fib.append(tf-t0)


t0 = time.clock()
for i in range (1,35):
    k = fibo_recursivo(i)
    tf = time.clock()
    lista_fibr.append(tf - t0)



rango = np.arange(1,35,1)
pl.ylabel("y")
pl.xlabel('x')
pl.plot(rango, lista_fib, lista_fibr)
pl.show()




