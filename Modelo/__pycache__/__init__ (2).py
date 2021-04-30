import sys,os;
ruta=os.path.dirname(os.path.dirname(\
                     os.path.realpath(__file__)))
sys.path.append(ruta)
print(ruta)
