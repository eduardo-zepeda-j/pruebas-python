propietario = ''

class Canasta:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.estaLlena = False
        self.MiLista = []
        
        
    def agregarFruta(self,fruta):
        
        
        if self.dimension() == False: 
            self.MiLista.append(fruta)
        
        else:
            print(f'La Canasta esta llena y {fruta.nombre} no se agrego')
        
        
    def dimension(self):
        if len(self.MiLista)==5:
            self.estaLlena = True
        return self.estaLlena
    
    def mostrarFruta(self):
        global propietario
        print('Hola yo soy el propietario',propietario)
        for i in self.MiLista:
            print(f'La Fruta es: {i.nombre}')
            
        

class Abarroteria:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def nombrarPropietario(self,prop):
        global propietario
        propietario = prop