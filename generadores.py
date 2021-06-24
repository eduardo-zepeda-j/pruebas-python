"""
son estructuras que extraen valores de una funcion 
y se almacenan en objetos iterables(que se pueden recorrer)

los valores se almacenan de uno en uno

cada vez que un generador almacena un valor, se mantiene
en pausa

con generadores los valores se van devolviendo de uno en uno

son mas eficientes que las funciones tradicionales
muy utiles con listas de valores infinitos
bajo determinados escenarios sera muy util que un generador devuelva
los valores de uno en uno
"""

def generaPares(limite):
    num = 1
    
    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares(10)

"""
for i in devuelvePares:
    print(i)

next sirve para ir entregando valor por valor
entre llamada y llamada el generador se mantiene en pausa
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
"""

#nueva instruccion yield from
#se usa para simplificar codigo si hubieran bucles anidados

def devuelve_ciudades(*ciudades):
    #el asterisco indica que no sabe cuantos argumentos va recibir y que son tuplas
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas= devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
