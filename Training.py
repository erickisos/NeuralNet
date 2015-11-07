__author__ = 'shogo'


import numpy as np
from math import exp, sqrt
import random
import math


class BackPro():
    def __init__(self):
        pass

    def Matix(self, x, s):
        #Variables para crear crear la matrix
        lx = len(x)
        ls = len(s)
        lm = ((lx+ls)/2)+1
        allNeuro = lx+ls+lm
        arreglo = allNeuro*allNeuro

        # Se crea la matrix
        Matrix = []
        for e in range(0, arreglo):
            Matrix.append(1)
        Matrix = np.array(Matrix)
        Matrix = Matrix.reshape(allNeuro, allNeuro)

        # Se ponen a cero los valores de entrada en la matrix
        for Entrada in range(0, lx):
            Matrix[:,Entrada] = 0

        # Se ponen a cero los valores de salidas en la matrix
        start = allNeuro - ls
        for Salidas in range(start, allNeuro):
            Matrix[Salidas,:] = 0

        # Se ubica el indice de las diferents neuronas
        m = allNeuro
        w = Matrix
        VectMedias=0
        VecSalidas = []
        for fila in range(0, m):
            fil = w[fila,:]
            fil = np.abs(fil)
            salidas = fil.sum()
            if salidas == 0:
                VectMedias = VectMedias + 1
                VecSalidas.append(fila)
        Entradas = 0
        VecEnt = []
        for Columna in range(0, m):
            colum = w[:,Columna]
            colum = np.abs(colum)
            entradas = colum.sum()
            if entradas == 0:
                Entradas = Entradas + 1
                VecEnt.append(Columna)
        Medias = m - (Entradas + VectMedias)
        midEntradas = []
        for i in range(0, m):
            midcol = w[:,i]
            midcol = np.abs(midcol)
            mident = midcol.sum()
            if mident != 0:
                midEntradas.append(i)
        midSalidas = []
        for j in range(0, m):
            midfil = w[j,:]
            midfil = np.abs(midfil)
            midsal=midfil.sum()
            if midsal != 0:
                midSalidas.append(j)
        VectMedias = []
        for e in range(0, len(midEntradas)):
            for f in range(0, len(midSalidas)):
                if midEntradas[e] == midSalidas[f]:
                    VectMedias.append(midEntradas[e])

        # Elimina conecciones de entradas con salidas
        for Dato in VecSalidas:
            Matrix[VecEnt,Dato] = 0

        # Elimina conecciones de medias con medias
        for Datomedio in VectMedias:
            Matrix[VectMedias, Datomedio] = 0

        print(Matrix)
        print(VecEnt, VectMedias, VecSalidas)


x = [1, 1]
s = [1,]

neu = BackPro()
neu.Matix(x, s)