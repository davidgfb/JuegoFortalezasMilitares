class Dinero:
    def __init__(self,cantidad):
        self.setCantidad(cantidad)

    def setCantidad(self,cantidad):
        self.cantidad=cantidad

    def getCantidad(self):
        return self.cantidad

    def toString(self):
        return "{Dinero: cantidad="+\
               str(self.getCantidad())+"}"

'''
#PROBADOR
dinero=Dinero(0)
print(dinero.toString())
'''
