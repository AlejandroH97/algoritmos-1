import time
import numpy as np
import pylab as pl




def fibo_iterado(n):
    if n== 0:
        return 0
    a,b = 0,1
    for i in range(1, n):
        a, b = b, a + b
    return b



lista_fib=[]
lista_fibr=[]
dato= raw_input("ingrese el numero maximo de fibonacci que desea calcular: ")
t0 = time.clock()
for i in range (1, int(dato)+1):
    k = fibo_iterado(i)
    tf = time.clock()
    lista_fib.append(tf-t0)
    print "el tiempo estimado para",i ," es de: ",tf-t0, " y el resultado es :", k


rango = np.arange(1,int(dato)+1,1)
pl.ylabel("y")
pl.xlabel('x')
pl.plot(rango, lista_fib)
pl.show()