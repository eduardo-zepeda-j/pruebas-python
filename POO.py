class Coche():
    """
    los objetos tienen estados, propiedades y comportamientos
    las caracteristicas comunes son parte de un estado inicial (constructor)
    """
   
    #son 4 propiedades
    #init es el constructor
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas = 4 #se encapsula con 2 guiones bajos antes de la variable __
        self.__enMarcha = False


    def arrancar(self,arrancamos):
        
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enMarcha and chequeo):
            return 'El coche esta en marcha'
        
        elif(self.__enMarcha and chequeo ==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"

        else:
            return 'El coche esta parado'
        
    def estado(self):
        print('El coche tiene ',self.__ruedas,' ruedas. Un ancho de ',self.__anchoChasis,' y un largo de ',
            self.__largoChasis)
  
    def __chequeo_interno(self):
        print('Realizando chequeo interno')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas ='cerradas'

        if (self.gasolina =='ok' and self.aceite=='ok' and self.puertas=='cerradas'):
            return True
        else:
            return False
 #----------------------------------------------------------------------------------------------------------- 
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print('-------------A continuacion creamos el segundo objeto---------')

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas = 2

miCoche2.estado()
