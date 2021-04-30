from Modelo.Jugador import Jugador 
from Modelo.Cortina import Cortina
from Modelo.Terraplén import Terraplén
from Modelo.Ladrillo import Ladrillo
from Modelo.Dinero import Dinero
from Modelo.Precio import Precio
from Modelo.Nivel import Nivel

from Vista.Tortuga import Tortuga

from threading import Thread
from time import sleep

def recogeDinero(jugador,cantidad):
    while True:
        jugador.recogeDinero(cantidad)
        print(jugador.toString())
        sleep(1)

tortuga=Tortuga(3,100)
tortuga.hideturtle()
#tortuga.speed(0)
#tortuga.pinta()
dinero=Dinero(10)
nivel1=Nivel(1)
mejoras=[]
jugador=Jugador(mejoras,dinero,nivel1,tortuga)
material=Ladrillo()
precioCortina=Precio(10)
precioTerraplén=Precio(20)
cortina=Cortina(material,precioCortina) #cuidado con Precio
terraplén=Terraplén(precioTerraplén) #log

jugador.compra(cortina)
jugador.compra(terraplén)

jugador.subeA_Nivel(2)

#print(jugador.toString())
#Thread(target=recogeDinero,args=[jugador,1]).start()


