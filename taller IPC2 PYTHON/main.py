from canasta import Canasta,Abarroteria
from fruta import Fruta 

canastita = Canasta('Mi canasta')
abarro = Abarroteria('KZ')
abarro.nombrarPropietario('Kevin')
pera = Fruta('Pera')
manzana = Fruta('Manzana')
limon = Fruta('Limon')
fresa = Fruta('Fresa')
papaya = Fruta('papaya')
higo = Fruta('higo')



if __name__ == '__main__':
    canastita.agregarFruta(pera)
    canastita.agregarFruta(manzana)
    canastita.agregarFruta(limon)
    canastita.agregarFruta(fresa)
    canastita.agregarFruta(papaya)
    
    canastita.mostrarFruta()
    canastita.agregarFruta(higo)
    canastita.mostrarFruta()