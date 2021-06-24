class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.up = None
        self.down = None

class lista_ortogonal:
    def __init__(self):
        self.head = Node(None)

    def create(self,n,m):
        p =Node()
        q =Node()
        r =Node()
        for i in range(n):
            
            for j in range(m):
                
                p.data = input('Inserte dato')
                
                p.next = None
                p.down = None
                if j==0:
                    p.prev == None
                    if self.head == None:
                        self.head = p
                    q = p
                
                else:
                    p.prev = q
                    q.next = p
                    q=p
                if i == 0:
                    p.up = None
                    q = p
                else:
                    p.up = r
                    r.down = p
                    r = r.next

            r = self.head
            while r.down != None:
                r = r.down    

    def mostrar(self):
        if self.head != None:
            p = self.head
            while p!=None:
                q = p
                while q!=None:
                    print(q.data)
                    q = q.next
                p = p.down
        else:
            print('Lista Vacia')


prueba = lista_ortogonal()

prueba.create(2,2)

prueba.mostrar()