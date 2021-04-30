class Jugador:
    def __init__(self,mejoras,dinero,nivel):
        self.setMejoras(mejoras)#[]) 
        self.setDinero(dinero)
        self.setNivel(nivel)

    def setNivel(self,nivel):
        self.nivel=nivel

    def getNivel(self):
        return self.nivel

    def compra(self,mejora): 
        coste=mejora.getPrecio().getCoste()
        cantidad=self.getDinero().getCantidad()

        if coste>cantidad:
            print("No puedes hacer la compra de "+\
                  str(mejora.toString())+"\n"+\
                  "Tienes "+str(cantidad)+"\n"+\
                  "Necesitas "+str(coste)+"\n"+\
                  "Te faltan "+str(coste-cantidad)+"\n"+\
                  10*"-") #es str
        else:
            cantidad-=coste
            self.getDinero().setCantidad(cantidad)
            self.setMejora(mejora)
            print("Has comprado "+\
                  str(mejora.toString())+"\n"+\
                  "Te quedan "+\
                  str(self.getDinero().getCantidad())) 
                              
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

        return "{Jugador: mejoras="+str(sMejoras)+\
               ", dinero="+\
               self.getDinero().toString()+\
               ", nivel="+\
               self.getNivel().toString()+\
               "}"

'''
#PROBADOR
from Cortina import Cortina
from Terraplén import Terraplén
from Dinero import Dinero
from Ladrillo import Ladrillo
from Nivel import Nivel
from Precio import Precio

precioCortina=Precio(10)
precioTerraplén=Precio(20)
nivel1=Nivel(1)
material=Ladrillo()
dinero=Dinero(0)
mejoras=[]
jugador=Jugador(mejoras,dinero,nivel1)
cortina=Cortina(material,precioCortina) #no precioCantidad
terraplén=Terraplén(precioTerraplén)

jugador.compra(cortina)
jugador.compra(terraplén)
print(jugador.toString())
'''
