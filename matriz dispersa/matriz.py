from nodos import Nodo,NodoEncabezado
from encabezado import ListaEncabezado

class matriz:
    def __init__(self):
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()
    
    def insertar(self,fila,columna,data):
        nuevo = Nodo(fila,columna,data)

        eFila = self.filas.getEncabezado(fila)
        if eFila ==None:
            eFila = NodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.filas.setEncabezado(eFila)
        
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.right = eFila.accesoNodo
                eFila.accesoNodo.left = nuevo
                eFila.accesoNodo = nuevo
            
            else:
                actual = eFila.accesoNodo
                while actual.right != None:
                    if nuevo.columna < actual.right.columna:
                        nuevo.right = actual.right
                        actual.right.left = nuevo
                        nuevo.left = actual
                        actual.right = nuevo
                        break
                    actual = actual.right
                if actual.right == None:
                    actual.right = nuevo
                    nuevo.left = actual

        #---------------------------------------------------
        eColumna = self.columnas.getEncabezado(columna)
        if eColumna ==None:
            eColumna = NodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.columnas.setEncabezado(eColumna)
        
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.down = eColumna.accesoNodo
                eColumna.accesoNodo.up = nuevo
                eColumna.accesoNodo = nuevo
            
            else:
                actual = eColumna.accesoNodo
                while actual.down != None:
                    if nuevo.fila < actual.down.fila:
                        nuevo.down = actual.down
                        actual.down.up = nuevo
                        nuevo.up = actual
                        actual.down = nuevo
                        break
                    actual = actual.down
                if actual.down == None:
                    actual.down = nuevo
                    nuevo.up = actual

    def mostrarFilas(self):
        eFila = self.filas.primero
        print('--------FILAS---------')
        while eFila != None:
            actual = eFila.accesoNodo
            print('\n Fila ',actual.fila)
            print('Columna      Valor')
            
            while actual !=None:
                print(actual.columna,'          ',actual.data)
                actual = actual.right

            eFila = eFila.next
        print('---------FIN----------')

    def mostrarColumnas(self):
        eColumna = self.columnas.primero

        while eColumna != None:
            actual = eColumna.accesoNodo
            print('\n Columna ',actual.columna)
            print('Fila      Valor')
            while(actual != None):
                print(actual.fila, '        ',actual.data)
                actual = actual.down
            eColumna = eColumna.next
        print('---------FIN----------')

if __name__ == '__main__':
    m = matriz()


    m.insertar(1, 0, "adolfo")
    m.insertar(2, 1, "brandon")
    m.insertar(0, 1, "daniel")
    m.insertar(1, 2, "eduardo")
    m.insertar(0, 2, "diego")
    m.insertar(0, 0, "javier")
    m.mostrarColumnas()
    m.mostrarFilas()