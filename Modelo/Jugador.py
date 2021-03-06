class Jugador:
    def __init__(self,mejoras,dinero,nivel,
                 tortuga):
        self.setMejoras(mejoras)#[]) 
        self.setDinero(dinero)
        self.setNivel(nivel)
        self.setTortuga(tortuga)

    def dibujaMejoras(self):
        tortuga=self.getTortuga()
        nLadosCortina=self.getNivel().\
                      getN_Nivel()+2

        tortuga.clear()
        
        for mejora in self.getMejoras():                
            tortuga.setN_Lados(nLadosCortina) 
            tortuga.pinta()

    def subeA_Nivel(self,nivelAumentado):
        self.getNivel().setN_Nivel(nivelAumentado)
        self.dibujaMejoras()
        print(self.toString()+" ha subido a nivel "+\
              str(self.getNivel().getN_Nivel())+\
              "\n"+10*"-")

    def compra(self,mejora): 
        coste=mejora.getPrecio().getCoste()
        cantidad=self.getDinero().getCantidad()

        if coste>cantidad:
            print(self.toString()+\
                  " no puede hacer la compra de "+\
                  str(mejora.toString())+"\n"+\
                  "Tiene "+str(cantidad)+"\n"+\
                  "Necesita "+str(coste)+"\n"+\
                  "Le faltan "+str(coste-cantidad)+"\n"+\
                  10*"-") #es str
        else:
            cantidad-=coste
            self.getDinero().setCantidad(cantidad)
            self.setMejora(mejora)

            self.dibujaMejoras()

            print(self.toString()+\
                  " ha comprado "+\
                  str(mejora.toString())+"\n"+\
                  "Le quedan "+\
                  str(self.getDinero().getCantidad())+\
                  "\n"+10*"-")
                  #+"\n"+\
                  #self.toString()+"\n"+10*"-")

    def recogeDinero(self,cantidad):
        dinero=self.getDinero()
        dinero.setCantidad(dinero.getCantidad()+cantidad)        

    ####### setters #######
    def setTortuga(self,tortuga):
        self.tortuga=tortuga
        tortuga.hideturtle()
        tortuga.speed(0)

    def setNivel(self,nivel):
        self.nivel=nivel
                             
    def setDinero(self,dinero):
        self.dinero=dinero

    def setMejoras(self,mejoras):
        self.mejoras=mejoras

    def setMejora(self,mejora):
        self.mejoras.append(mejora)
    #####################

    ###### getters #####
    def getNivel(self):
        return self.nivel

    def getTortuga(self):
        return self.tortuga
        
    def getMejoras(self):
        return self.mejoras

    def getDinero(self):
        return self.dinero
    #####################

    def toString(self):
        sMejoras=[]

        for mejora in self.getMejoras():
            sMejoras.append(mejora.toString())

        return "{Jugador: mejoras="+str(sMejoras)+\
               ", dinero="+\
               self.getDinero().toString()+\
               ", nivel="+\
               self.getNivel().toString()+\
               ", tortuga="+\
               self.getTortuga().toString()+\
               "}"

'''
#PROBADOR
import sys,os;
ruta=os.path.dirname(os.path.dirname(\
                     os.path.realpath(__file__)))
                    #en tiempo de ejecucion volatil
sys.path.append(ruta)
print(ruta)

from Cortina import Cortina
from Terrapl??n import Terrapl??n
from Dinero import Dinero
from Ladrillo import Ladrillo
from Nivel import Nivel
from Precio import Precio

from Vista.Tortuga import Tortuga

tortuga=Tortuga(3,100)
tortuga.hideturtle()
precioCortina=Precio(10)
precioTerrapl??n=Precio(20)
nivel1=Nivel(1)
material=Ladrillo()
dinero=Dinero(10)
mejoras=[]
jugador=Jugador(mejoras,dinero,nivel1,tortuga)
cortina=Cortina(material,precioCortina) #no precioCantidad
terrapl??n=Terrapl??n(precioTerrapl??n)

jugador.compra(cortina)
jugador.compra(terrapl??n)
#print(jugador.toString())
'''
