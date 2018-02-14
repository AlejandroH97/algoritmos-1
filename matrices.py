import time

filasA= input()
columnasA= input()
filasB = input()
columnasB= input()



def crear_matriz(numero_filas, numero_columnas):
    matriz = []
    for i in range(numero_filas):
            matriz.append([])
            for j in range(numero_columnas):
                    n = input()
                    matriz[i].append(n)
    return matriz

matrizA= crear_matriz(filasA,columnasA)
matrizB= crear_matriz(filasB,columnasB)

t0=time.clock()
def multiplicacion():
    c=[]
    for k in range(0,columnasB):
        aux = []
        for j in range(0,filasA):
            aux1=0
            for i in range(0,filasB):
                aux1=aux1+(matrizA[k][i]*matrizB[i][j])
            aux.append(aux1)
        c.append(aux)

    return c

tf=time.clock()

print"la matriz resultante es: ", multiplicacion(), "y el tiempo que se demoro en multiplicar la matriz fue: ", tf-t0



