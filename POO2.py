class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo =modelo
        self.enmarcha =False
        self.acelera = False
        self.frena=False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena =True
        
    def estado(self):
        print('Marca: ',self.marca,"\nModelo: ",self.modelo,'\nEn Marcha: ',
        self.enmarcha,'\nAcelerando: ',self.acelera,'\nFrenando: ',self.frena)   


#Herencia
class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La Furgoneta esta cargada"
        else:
            return 'La Furgoneta no esta cargada'

    def estado(self):
        print('Marca: ',self.marca,"\nModelo: ",self.modelo,'\nEn Marcha: ',
        self.enmarcha,'\nAcelerando: ',self.acelera,'\nFrenando: ',self.frena,'\n')   

class Moto(Vehiculo):
    hCaballito = ''
    def caballito(self):
        self.hCaballito = 'Voy haciendo el caballito'

    def estado(self):
        print('Marca: ',self.marca,"\nModelo: ",self.modelo,'\nEn Marcha: ',
        self.enmarcha,'\nAcelerando: ',self.acelera,'\nFrenando: ',self.frena,'\n',self.hCaballito)   


class VElectrico(Vehiculo):
    def  __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

#La herencia multiple da prioridad al constructor de la primer clase
class BicicletaElectrica(VElectrico,Vehiculo):
    pass



miMoto = Moto('Honda','CBR')

miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta('Renault','Kangoo')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


miBici = BicicletaElectrica("Honda","kangoo")