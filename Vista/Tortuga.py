from turtle import Turtle

class Tortuga(Turtle):
    def __init__(self,nLados,longLado):
        Turtle.__init__(self)
        self.setN_Lados(nLados)
        self.setLongLado(longLado)

    def setN_Lados(self,nLados):
        self.nLados=nLados

    def setLongLado(self,longLado):
        self.longLado=longLado

    def getN_Lados(self):
        return self.nLados

    def getLongLado(self):
        return self.longLado
    
    def pinta(self):
        nLados=self.getN_Lados()
        angulo=360/nLados
        for figura in range(nLados):
            self.forward(self.getLongLado())
            self.left(angulo)

    def toString(self):
        return "{Tortuga: nLados="+\
               str(self.getN_Lados())+\
               ", longLado="+\
               str(self.getLongLado())+"}"

'''
#PROBADOR    
tortuga = Tortuga(3,100)
print(tortuga.toString())
tortuga.hideturtle()
tortuga.speed(0)
tortuga.pinta()
'''
