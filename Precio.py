class Precio:
    def __init__(self,coste):
        self.setCoste(coste)

    def setCoste(self,coste):
        self.coste=coste

    def getCoste(self):
        return self.coste
        
    def toString(self):
        return "Precio:"+str(self.getCoste())

'''
#PROBADOR
precio=Precio(10)
print(precio.toString())
'''
