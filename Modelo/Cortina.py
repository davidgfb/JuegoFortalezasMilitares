from Mejora import Mejora

class Cortina(Mejora):
    def __init__(self,material,precio):
        Mejora.__init__(self,precio)
        self.setMaterial(material)

    def setMaterial(self,material): 
        self.material=material

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

'''
#from .Mejora import Mejora

if __name__ == '__main__':
    from mymodule import as_int
else:
    from .mymodule import as_int
'''
