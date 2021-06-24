from nodos import Nodo, NodoEncabezado

class ListaEncabezado:
    def __init__(self,primero=None):
        self.primero = primero
    
    def setEncabezado(self,nuevo):
        if self.primero == None:
            self.primero = nuevo
        
        elif nuevo.id < self.primero.id:
            nuevo.next = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

        else:
            actual = self.primero
            while actual.next != None:
                if nuevo.id< actual.next.id:
                    nuevo.next = actual.next
                    actual.next.prev = nuevo
                    nuevo.prev = actual
                    actual.next = nuevo
                    break
                actual = actual.next

            if actual.next == None:
                actual.next = nuevo
                nuevo.anterior = actual

    def getEncabezado(self,id):
        actual = self.primero
        while actual!=None:
            if actual.id == id:
                return actual
            actual = actual.next

        return None
                    