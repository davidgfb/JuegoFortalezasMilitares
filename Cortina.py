from Mejora import Mejora

class Cortina(Mejora):
    def __init__(self,material):
        self.setMaterial(material)

    def setMaterial(self,material): #Material
        self.material=material

    def getMaterial(self):
        return self.material
    
    def toString(self):
        return "Cortina: material="+self.getMaterial().toString()

'''
#PROBADOR
from Ladrillo import Ladrillo
material=Ladrillo()
cortina=Cortina(material)
print(cortina.toString())
'''
