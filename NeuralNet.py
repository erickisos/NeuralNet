# -*- coding: utf-8 -*-
__author__ = 'Shogo, Isos, elNiño, Jorge'

import math
import numpy as np
from Neurona import Neurona


class Red_Neurona():
    def __init__(self):
        self.Neuro = Neurona()
    def Segmentacion(self, w):
        try:
            m = int(math.sqrt(len(w)))
            w = np.array(w)
            w = w.reshape(m, m)
        except:
            print("no se puede hacer la matrix")
        VectMedias=0
        VecSalidas = []
        for fila in range(0, m):
            fil = w[fila,:]
            salidas = fil.sum()
            if salidas == 0:
                VectMedias = VectMedias + 1
                VecSalidas.append(fila)
        Entradas = 0
        VecEnt = []
        for Columna in range(0, m):
            colum = w[:,Columna]
            entradas = colum.sum()
            if entradas == 0:
                Entradas = Entradas + 1
                VecEnt.append(Columna)
        Medias = m - (Entradas + VectMedias)
        midEntradas = []
        for i in range(0, m):
            midcol = w[:,i]
            mident = midcol.sum()
            if mident != 0:
                midEntradas.append(i)
        midSalidas = []
        for j in range(0, m):
            midfil = w[j,:]
            midsal=midfil.sum()
            if midsal != 0:
                midSalidas.append(j)
        VectMedias = []
        for e in range(0, len(midEntradas)):
            for f in range(0, len(midSalidas)):
                if midEntradas[e] == midSalidas[f]:
                    VectMedias.append(midEntradas[e])
        return VecEnt, VectMedias, VecSalidas, w

    def asignacion(self, entradas, medios, salidas,matrix):
        a = []
        b = []
        intro = neo.Neuro.x
        bias = neo.Neuro.a
        w = matrix
        l = len(entradas)+len(medios)+ len(sali)
        for e in medios:
            pesoMedios = w[:,e]
            pesoMedios = list(pesoMedios)
            n = neo.Neuro.Sumatoria(intro, pesoMedios)
            sig = neo.Neuro.Sigmoide(bias, n)
            a.append(sig)
        for i in salidas:
            cosoDePrueba = []
            pesosSalidas = w[:,i]
            pesosSalidas = list(pesosSalidas)
            for elemento in medios:
                cosoDePrueba.append(pesosSalidas[elemento])
            ns = neo.Neuro.Sumatoria(a, cosoDePrueba)
            sigS = neo.Neuro.Sigmoide(bias, ns)
            b.append(sigS)
        print b

neo = Red_Neurona()
entr, med, sali, matrix = neo.Segmentacion(neo.Neuro.w)
c = neo.asignacion(entr, med, sali, matrix)