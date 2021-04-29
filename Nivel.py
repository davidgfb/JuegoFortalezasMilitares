class Nivel: #experiencia, edad...
    def __init__(self,nNivel):
        self.setN_Nivel(nNivel)

    def setN_Nivel(self,nNivel):
        self.nNivel=nNivel

    def getN_Nivel(self):
        return self.nNivel

    def toString(self):
        return "{Nivel: nNivel="+str(self.getN_Nivel())+"}"

'''
#PROBADOR
nivel1=Nivel(1)
print(nivel1.toString())
''' 
