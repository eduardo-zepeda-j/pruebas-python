"""
diccionarios  son estructuras de dato
clave:valor el orden en que se guardan 
los datos no es relevante

midiccionario ={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Guatemala":"Guatemala"}
midiccionario["Italia"] ="Lisboa"
print(midiccionario)

midiccionario["Italia"] = "Roma"
print(midiccionario)

del midiccionario["Reino Unido"]

print(midiccionario)


midiccionario = {"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}

print(midiccionario)


mitupla=["Guatemala","Francia","Reino Unido","Alemania"]

midiccionario={mitupla[0]:"Guatemala",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}

print(midiccionario["Francia"])
"""


midiccionario = {23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario["anillos"])
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

if "Jordan" in midiccionario.values():
    print('si se encuentra')