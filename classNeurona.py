from math import exp

class Neurona():
    def __init__(self):
        self.a = float(input("Ingrese valor de alpha:\n"))
        self.x = input("Ingrese los valores de entradas con una coma despues de cada dato: \n")
        self.w = input("Ingrese los valores de peso con una coma despues de cada dato: \n")
        
    def suma(self, x, w):
        Vrx = 0
        for elemento in range(0, len(x)):
            Vrx = Vrx + w[elemento]*x[elemento]
        return Vrx

    def sigmoide(self, a, suma):
        sigmo = 1/(1+exp(-a*suma))
        return sigmo
    
    def lineal(self, a, suma):
        line = suma*a
        return line

    def stepFunction(self, a, suma):
        if suma<a:
            return 0
        else:
            return 1


neurona = Neurona()
v = neurona.suma(neurona.x,neurona.w)
print("Sumatoria: %.2f" %v)
sigmo = neurona.sigmoide(neurona.a, v)
print("Resultando de aplicar a Sigmoide: %.4f" %sigmo)
line = neurona.lineal(neurona.a, v)
print("Resultado de aplicar a Lineal: %.4f" %line)
step = neurona.stepFunction(neurona.a, v)
print("Resultado de aplicar a Escalon Unitario: %.4f" %step)