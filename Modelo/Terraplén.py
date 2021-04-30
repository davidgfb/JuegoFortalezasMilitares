from Mejora import Mejora

class Terraplén(Mejora):
    def __init__(self,precio):
        Mejora.__init__(self,precio)
        
    def toString(self):
        return "{Terraplén: precio="+str(self.getPrecio().getCoste())+"}"

'''
#PROBADOR
from Precio import Precio
precio=Precio(20)
terraplén=Terraplén(precio)
print(terraplén.toString())
'''
