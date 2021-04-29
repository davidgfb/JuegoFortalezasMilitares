from Mejora import Mejora

class Terraplén(Mejora):
    def __init__(self,precio):
        Mejora.__init__(self,precio)
        
    def toString(self):
        return "{Terraplén: precio="+str(self.getPrecio())+"}"

'''
#PROBADOR
terraplén=Terraplén(20)
print(terraplén.toString())
'''
