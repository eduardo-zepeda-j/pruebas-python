"""
Recorriendo strings
tipo range
notaciones especiales con print

for i in ["primavera","verano","otogno","invierno"]:
    print(i)

para imprimir definiendo como termina el print agregamos end
    print('Hola',end="")
email = False

for i in 'juan@pildorasinformaticas.es':
    
    if(i =="@"):
        email = True

if email == True:
    print('Email correcto')
else:
    print('Email no es correcto')
valido = False
email = input('Introduce tu email: ')

for i in range(len(email)):
    if email[i]=="@":
        valido = True

if valido:
    print('Email Correcto')

else:
    print('email incorrecto')

for i in range(5,50,3):
    inicio, final y pasos    

    for i in range(5,50,3):
    la f nos permite jugar con formatos y poner entre llaves la variable toma el valor
    print(f'valor de la variable {i}')

contador = 10
while contador>0:
    print('hola mundo')
    contador-=1

continue se salta el ciclo

for letra in 'Python':
    if letra == 'h':
        continue

    print('Viendo la letra: '+letra)
nombre = "Pildoras Informaticas"
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador+=1
    
print(contador)

"""
class MiClase:
    pass #para implementar mas tarde

email = input('introduce tu email, por favor:')
for i in email:
    if i=='@':
        arroba = True
        break

else: #este else se ejecuta  si el for no se completa
    arroba = False

print(arroba)