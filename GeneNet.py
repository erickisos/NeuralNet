__author__ = 'erick'
# -*- encoding: utf-8 -*-

from random import random, randrange
import numpy as np
import math


# from NeuralNet import Red_Neurona


class algoritmoGenetico(object):
    def seleccionNatural(self, individuos):
        self.redNeural = Red_Neurona()

    def cruzaEnUnPunto(self, indiv1, indiv2):
        """
        :param indiv1: tipo "lista" Individuo padre/madre que proveerá de parte de sus genes
        :param indiv2: tipo "lista" Individuo padre/madre que proveerá parte de sus genes
        :return: Devuelve dos listas, una por descendiente resultante de la mezcla entre los genes de los progenitores
        """
        if len(indiv1) > len(indiv2):
            maxRange = len(indiv1) - 1
        else:
            maxRange = len(indiv2) - 1
        crossPoint = randrange(0, maxRange)
        alpha = random()
        umbral = 0.6
        if alpha > umbral:
            descendiente1 = indiv1[0:crossPoint] + indiv2[crossPoint:]
            descendiente2 = indiv2[0:crossPoint] + indiv1[crossPoint:]
        else:
            descendiente1 = indiv2[0:crossPoint] + indiv1[crossPoint:]
            descendiente2 = indiv1[0:crossPoint] + indiv2[crossPoint:]
        return descendiente1, descendiente2

    def cruzaVariable(self, indiv1, indiv2):
        """
        :param indiv1: tipo "lista" Individuo padre/madre que proveerá de parte de sus genes
        :param indiv2: tipo "lista" Individuo padre/madre que proveerá parte de sus genes
        :return: Devuelve dos listas, una por descendiente resultante de la mezcla entre los genes de los progenitores
        """

        if len(indiv1) > len(indiv2):
            maxRange = len(indiv1)
        else:
            maxRange = len(indiv2)
        crossPoint_1 = randrange(0, maxRange)
        crossPoint_2 = randrange(0, maxRange)

    # ---------------------------Aqui ira comparacion entre puntos de cruza y seleccion de uniones-------------------------

    def genMutacion(self, individuo):
        """
        :param individuo: Individuo Tipo Lista, binarizada, los datos binarios deben estar como string
        :return: individuo mutado o no mutado, resultante de pasar por el proceso aleatorio de mutación
        """
        probabilidad = 0.05
        factorMutageno = random()
        for i in range(0, len(individuo)):
            if factorMutageno < probabilidad:
                if individuo[i] == '0':
                    individuo[i] = '1'
                else:
                    individuo[i] = '0'
        return individuo

    def generarIndividuos(self, cantidad, elementos):
        """
        Este método genera una población inicial basado en una cantidad de individuos y un número de elementos
        :param cantidad: Tipo Int, número de individuos que conformarán la población inicial
        :param elementos: Tipo Int, número de propiedades que poseerá cada individuo
        :return: Matriz de población aleatoria
        """

        IndivTotal = []
        cantidadIndividuos = cantidad
        valorPorIndividuo = elementos
        for i in range(0, cantidadIndividuos):
            IndivTotal.append(self.generarIndividuo(valorPorIndividuo))
        IndivTotal = np.array(IndivTotal)
        return IndivTotal

    def crearFenotipos(self, IndivTotal):

        c = []
        for elemento in range(0, len(IndivTotal)):
            a = list(IndivTotal[elemento, :])
            b = []
            for ind in a:
                b.append(self.dec2bin(ind))
            c.append(b)
        c = np.array(c)
        return c

    def crearGenotipos(self, fenotipo):
        z = []
        for elem in range(0, len(fenotipo)):
            x = list(fenotipo[elem, :])
            y = []
            for ind in x:
                y.append(self.bin2dec(ind))
            z.append(y)
        z = np.array(z)
        return z

    def generarIndividuo(self, cantidad):
        indiv = []
        for i in range(0, cantidad):
            indiv.append(self.randBi(random()))
        return indiv

    def randBi(self, randomNumber):
        factorInversor = random()
        factorMezcla = random()
        if factorInversor > factorMezcla:
            randomNumber = -randomNumber
        else:
            randomNumber = randomNumber
        randomNumber = round(randomNumber, 4)
        return randomNumber

    def dec2bin(self, f):
        signo = ""
        if f < 0:
            f = abs(f)
            signo = "1"
        else:
            signo = "0"

        if f >= 1:
            g = int(math.log(f, 2))
        else:
            g = -1
        h = g + 1
        ig = math.pow(2, g)
        st = ""
        while f > 0 or ig >= 1:
            if f < 1:
                if len(st[h:]) >= 10:  # 10 fractional digits max
                    break
            if f >= ig:
                st += "1"
                f -= ig
            else:
                st += "0"
            ig /= 2
        st = signo + st[:h] + st[h:]
        return st

    def bin2dec(self, binario):

        if binario[0] == '1':
            flag = "Negative"
        else:
            flag = "Positive"
        j = 0
        valor = float(0.0)
        for i in range(1, len(binario)):
            j = i
            if binario[i] == "1":
                valor = valor + 1 / float(pow(2, j))
            else:
                valor = valor + 0 / float(pow(2, j))
        if flag == "Negative":
            valor = -valor
        valor = round(valor, 4)
        return valor


genonet = algoritmoGenetico()
"""
indiv = genonet.generarIndividuos(10,6)
genoin = genonet.crearFenotipos(indiv)
print(indiv)
print(genoin)
"""

prueba = genonet.generarIndividuo(6)
pruu = genonet.generarIndividuo(6)
print(prueba, pruu)
hijo, hija = genonet.cruzaEnUnPunto(prueba, pruu)
print(hijo)
hijos = [hijo, hija]
hijos = np.array(hijos)
print(hijos)
hijos = genonet.crearFenotipos(hijos)
print(hijos)
hijo = hijos[0]
hija = hijos[1]
print(hijo)
