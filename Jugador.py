class Jugador:
    def __init__(self,dinero):
        self.setMejoras([])
        self.setDinero(dinero)

    def compra(self,mejora): 
        coste=mejora.getPrecio().getCoste()
        cantidad=self.getDinero().getCantidad()

        if coste>cantidad:
            print("No puedes hacer la compra.\n\
                  Tienes",cantidad,\
                  ", necesitas:",coste,\
                  "te faltan",coste-cantidad)            
        else:
            cantidad-=coste
            self.getDinero().setCantidad(cantidad)
            self.setMejora(mejora)
            print("Puedes hacer la compra. Te quedan",
                  self.getDinero().getCantidad()) 
                              
    def setDinero(self,dinero):
        self.dinero=dinero

    def setMejoras(self,mejoras):
        self.mejoras=mejoras

    def setMejora(self,mejora):
        self.mejoras.append(mejora)
        
    def getMejoras(self):
        return self.mejoras

    def getDinero(self):
        return self.dinero

    def recogeDinero(self,cantidad):
        dinero=self.getDinero()
        dinero.setCantidad(dinero.getCantidad()+cantidad)        

    def toString(self):
        sMejoras=[]

        for mejora in self.getMejoras():
            sMejoras.append(mejora.toString())

        return "Jugador: mejoras="+str(sMejoras)+\
               ", dinero="+self.getDinero().toString()

'''
#PROBADOR
from Cortina import Cortina
from Terraplén import Terraplén
from Dinero import Dinero
from Ladrillo import Ladrillo
material=Ladrillo()
dinero=Dinero(0)
jugador=Jugador(dinero)
cortina=Cortina(material)
terraplén=Terraplén()
jugador.compra(cortina)
jugador.compra(terraplén)
print(jugador.toString())
'''
