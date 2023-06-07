import math
class Esfera:

    def __init__ (self, cor, raio):
        self.cor=cor
        self.raio=raio

    def volume(self):
        vol=(4/3)*math.pi*(self.raio**3)
        return vol
    
    def area(self):
        ar=4*math.pi*(self.raio**2)
        return ar
    
    