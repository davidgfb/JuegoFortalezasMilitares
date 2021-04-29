from Mejora import Mejora

class Cortina(Mejora):
    def __init__(self,material,precio):
        self.setMaterial(material)
        self.setPrecio(precio)

    def setMaterial(self,material): #Material
        self.material=material

    def setPrecio(self,precio):
        self.precio=precio

    def getPrecio(self):
        return self.precio

    def getMaterial(self):
        return self.material
    
    def toString(self):
        return "{Cortina: material="+\
               self.getMaterial().toString()+\
               ", precio="+self.getPrecio().toString()+\
               "}"

'''
#PROBADOR
from Ladrillo import Ladrillo
from Precio import Precio
precio=Precio(10)
material=Ladrillo()
cortina=Cortina(material,precio)
print(cortina.toString())
'''
