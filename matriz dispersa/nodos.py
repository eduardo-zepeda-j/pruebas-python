class Nodo:
    def __init__(self,fila, columna,data):
        self.fila = fila
        self.columna = columna
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None

class NodoEncabezado:
    def __init__(self,id):
        self.id = id
        self.next = None
        self.prev = None
        self.accesoNodo = None
