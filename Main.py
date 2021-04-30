from Modelo.Jugador import Jugador 
from Modelo.Cortina import Cortina
from Modelo.Terraplén import Terraplén
from Modelo.Ladrillo import Ladrillo
from Modelo.Dinero import Dinero
from Modelo.Precio import Precio
from Modelo.Nivel import Nivel

from threading import Thread
from time import sleep

def recogeDinero(jugador,cantidad):
    while True:
        jugador.recogeDinero(cantidad)
        print(jugador.toString())
        sleep(1)

dinero=Dinero(10)
nivel1=Nivel(1)
mejoras=[]
jugador=Jugador(mejoras,dinero,nivel1)
material=Ladrillo()
precioCortina=Precio(10)
precioTerraplén=Precio(20)
cortina=Cortina(material,precioCortina) #cuidado con Precio
terraplén=Terraplén(precioTerraplén) #log

jugador.compra(cortina)
jugador.compra(terraplén)

print(jugador.toString())
#Thread(target=recogeDinero,args=[jugador,1]).start()


