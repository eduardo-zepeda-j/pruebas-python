"""
def divide():
    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print('La division es: '+str(op1/op2))
    except ValueError:
        print('El valor introducido es erroneo')
    except ZeroDivisionError:
        print('No puede dividir entre cero')
    finally:
        print('calculo finalizado')

divide()
"""

#Lanzamiento de Excepciones de forma intensionada
#instruccion RAISE // creacion de excepciones propias (mas adelante)

"""
def evaluaEdad(edad):
    if edad<0:
        raise TypeError('No se permiten edades negativas')
    
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."

    
print(evaluaEdad(-15))
"""
import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError('El numero no puede ser negativo')
    else:
        return math.sqrt(num1)

op1 = int(input('Ingrese un numero: '))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")