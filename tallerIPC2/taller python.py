from fruta import Fruta

class Canasta:
    def __init__(self,nombre):
        self.nombre = nombre
        self.estaLlena = False
        self.MiLista = []
        
    def agregarFruta(self,fruta):
        self.MiLista.append(fruta)
        
    
    def mostrarFrutas(self):
        #print(self.MiLista)
        for i in self.MiLista:
            print(i.nombre)
'''


miCanasta = Canasta('prueba')

pera = Fruta('Pera')
banano = Fruta('Banano')
manzana = Fruta('Manzana')
limon = Fruta('Limon')

miCanasta.agregarFruta(pera)
miCanasta.agregarFruta(banano)
miCanasta.agregarFruta(manzana)
miCanasta.agregarFruta(limon)

miCanasta.mostrarFrutas()
'''
#-------------------------------------------------
nombre = ''

def asignarNombre(n):
    global nombre
    nombre = n

def mostrarNombre():
    global nombre
    print('-'*30)
    print('Hola, mi nombre es:',nombre)
    print('-'*30)

asignarNombre('Paco')
mostrarNombre()
    