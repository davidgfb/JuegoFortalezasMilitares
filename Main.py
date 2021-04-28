from Jugador import Jugador
from Cortina import Cortina
from Terraplén import Terraplén
from Ladrillo import Ladrillo

jugador=Jugador()
material=Ladrillo()
cortina=Cortina(material)
terraplén=Terraplén()

jugador.compra(cortina)
jugador.compra(terraplén)

print(jugador.toString())
