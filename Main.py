from Jugador import Jugador
from Cortina import Cortina
from Terraplén import Terraplén
from Ladrillo import Ladrillo
from Dinero import Dinero
from threading import Thread
from time import sleep

def recogeDinero(jugador,cantidad):
    while True:
        jugador.recogeDinero(cantidad)
        print(jugador.toString())
        sleep(1)

dinero=Dinero(0)
jugador=Jugador(dinero)
material=Ladrillo()
cortina=Cortina(material)
terraplén=Terraplén()

jugador.compra(cortina)
jugador.compra(terraplén)

Thread(target=recogeDinero,args=[jugador,1]).start()


