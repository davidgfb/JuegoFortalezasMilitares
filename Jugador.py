#from Mejora import Mejora

class Jugador:
    def __init__(self):
        self.setMejoras([])

    def compra(self,mejora): #Mejora string
        self.setMejora(mejora)

    def setMejoras(self,mejoras):
        self.mejoras=mejoras

    def setMejora(self,mejora):
        self.mejoras.append(mejora)
        
    def getMejoras(self):
        return self.mejoras

    def toString(self):
        sMejoras=[]
        for mejora in self.getMejoras():
            sMejoras.append(mejora.toString())
        return "Jugador: mejoras="+str(sMejoras)

'''
#PROBADOR
jugador=Jugador()
jugador.compra("cortina")
jugador.compra("terraplén")
print(jugador.toString())
'''
