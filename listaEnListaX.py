class NodoCabecera():
    def __init__(self,posX):
        self.posX = posX
        self.next = None
        self.down = None
    
class NodoLista:
    def __init__(self,data):
        self.data = data
        self.down = None
    
class ListaCabecera:
    def __init__(self):
        self.head = None
        self.down = None

    def insert(self,nuevoNodo):
        if self.head!=None:
            ultimo = self.head
            while ultimo.next !=None:
                ultimo = ultimo.next
            ultimo.next = nuevoNodo
        
        else:
            self.head = nuevoNodo

    def mostrar(self):
        temp = self.head
        while temp !=None:
            print(temp.posX,end = '->')
            temp = temp.next
        print('Null')

class ListaEnLista:
    def __init__(self):
        self.head = None
        self.down = None
        
    def insert(self,posX,lista,nuevoNodo):
        listaTemporal = lista.head
        
        
        while listaTemporal.posX != int(posX):
            listaTemporal = listaTemporal.next

        listaX = listaTemporal

        if listaX!=None:
            tempUltimo = listaX
            while tempUltimo.down !=None:
                tempUltimo = tempUltimo.down
            tempUltimo.down = nuevoNodo
        
        else:
            listaX = nuevoNodo
            listaX.down = nuevoNodo
    
    def mostrar(self,lista,posX):
        ListaCabecera = lista.head
        while ListaCabecera.posX !=int(posX):
            ListaCabecera = ListaCabecera.next
        print('La Cabecera es ',ListaCabecera.posX)
        temp = ListaCabecera.down
        while temp != None:
            print(temp.data,end= '\n|\n\/\n')
            temp = temp.down
        print('Null')

if __name__ == '__main__':
    lCabecera = ListaCabecera()
    lLista = ListaEnLista()
    cantidadCabecera = 6
    for i in range(cantidadCabecera):
        lCabecera.insert(NodoCabecera(i))
    lCabecera.mostrar()

    posX = 3
    val = 'A'
    lLista.insert(posX,lCabecera,NodoLista(val))
    lLista.insert(1,lCabecera,NodoLista(2))
    lLista.insert(1,lCabecera,NodoLista('B'))
    lLista.insert(1,lCabecera,NodoLista('D'))
    lLista.mostrar(lCabecera,3)
    