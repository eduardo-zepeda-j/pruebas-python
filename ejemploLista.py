class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class listaEnlazada:
    def __init__(self):
        self.head=None

    def insertar(self,nuevoNodo):
        if self.head:
            
            ultimo = self.head
            while ultimo.next !=None:
                ultimo=ultimo.next
            ultimo.next=nuevoNodo
        else:
            self.head =nuevoNodo

    def mostrar(self):
        temp =self.head

        while temp !=None:
            print(temp.data,end='->')
            temp = temp.next
        print('Null')

# Esto indica que aqui inicia todo
if __name__=='__main__':
    lEnlazada = listaEnlazada()
    lEnlazada.insertar(Node(1))
    lEnlazada.insertar(Node(2))
    lEnlazada.insertar(Node(3))
    lEnlazada.insertar(Node(4))
    lEnlazada.insertar(Node(5))
    lEnlazada.insertar(Node(6))
    lEnlazada.insertar(Node(7))

    lEnlazada.mostrar()