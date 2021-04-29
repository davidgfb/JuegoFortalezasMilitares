class Mejora: #@abstractmethod #coste
    def __init__(self,precio):
        self.setPrecio(precio)

    def setPrecio(self,precio):
        self.precio=precio

    def getPrecio(self):
        return self.precio

    def toString(self):
        return "{Mejora: precio="+\
               str(self.getPrecio())+"}"

'''
#PROBADOR
mejora=Mejora(10)
print(mejora.toString())
'''
