from Neurona import Neurona
from NeuralNet import Red_Neurona
from math import exp,sqrt
import random
import numpy as np


class Trainer():
    def __init__(self):
        self.addNeurona()
        self.TrainIt()

    def TrainIt(self):
        pass

    def addNeurona(self):
        while True:
            neuralNumber = int(input("Ingrese Cuantas neuronas posee la red:\n"))
            weights = np.zeros()
