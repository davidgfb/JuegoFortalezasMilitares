from Jugador import Jugador
from Cortina import Cortina
from Terraplén import Terraplén
from Ladrillo import Ladrillo
from Dinero import Dinero
from Precio import Precio
from threading import Thread
from time import sleep

def recogeDinero(jugador,cantidad):
    while True:
        jugador.recogeDinero(cantidad)
        print(jugador.toString())
        sleep(1)

dinero=Dinero(10)
#dinero=Dinero(0)
jugador=Jugador(dinero)
material=Ladrillo()
precio=Precio(10)
cortina=Cortina(material,precio)
terraplén=Terraplén()

jugador.compra(cortina)
#jugador.compra(terraplén)

print(jugador.toString())
#Thread(target=recogeDinero,args=[jugador,1]).start()


