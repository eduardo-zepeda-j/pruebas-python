class NodoCabecera():
    def __init__(self,data):
        self.posY = data
        self.next = None
        self.right = None

class NodoLista:
    def __init__(self,data):
        self.data = data
        self.right = None

class ListaCabecera:
    def __init__(self):
        self.head = None
        self.right = None
    
    def insertar(self,nuevoNodo):
        if self.head:
            ultimo = self.head
            while ultimo.next!= None:
                ultimo = ultimo.next
            ultimo.next = nuevoNodo
        else:
            self.head = nuevoNodo

    
    def mostrar(self):
        temp = self.head
        while temp!=None:
            print(temp.posY,end='\n||\n\/\n')
            temp = temp.next
        print('Null')

class ListaEnLista:
    def __init__(self):
        self.head = None
        self.right = None
    
    def insertar(self,posY,lista,nuevoNodo):
        listaTemporal = lista.head
        while listaTemporal.posY!=int(posY):
            listaTemporal = listaTemporal.next
        
        listaY = listaTemporal
        while listaY.right !=None:
            listaY = listaY.right
        
        if listaY:
            tempUltimo = listaY
            while tempUltimo.right != None:
                tempUltimo = tempUltimo.right
            tempUltimo.right = nuevoNodo
        else:
            listaY = nuevoNodo
            listaY.right = nuevoNodo

    def mostrar(self,lista,posY):
        ListaCabecera = lista.head
        while ListaCabecera.posY!=int(posY):
            ListaCabecera = ListaCabecera.next
        print('La cabecera es ',ListaCabecera.posY)
        temp = ListaCabecera.right
        while temp!=None:
            print(temp.data,end='->')
            temp = temp.right
        print('Null')

if __name__ == '__main__':
    lCabecera = ListaCabecera()
    lLista = ListaEnLista()
    cantidadCabecera = input('Cantidad de Nodos Cabecera: ')
    for i in range(int(cantidadCabecera)):
        lCabecera.insertar(NodoCabecera(i))
    lCabecera.mostrar()
    
    posY = input('Ingresar valor de la posicion Y: ')
    val = input('Ingresar el valor para guardar: ')
    lLista.insertar(posY,lCabecera,NodoLista(val))

    impY = input('Ingrese el valor para imprimir de la posicion Y')
    lLista.mostrar(lCabecera,impY)

