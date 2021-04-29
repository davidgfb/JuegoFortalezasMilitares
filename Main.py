from Jugador import Jugador
from Cortina import Cortina
from Terraplén import Terraplén
from Ladrillo import Ladrillo
from Dinero import Dinero
from Precio import Precio
from Nivel import Nivel

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


