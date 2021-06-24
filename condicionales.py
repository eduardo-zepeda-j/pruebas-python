"""
El condicional if es una condicional de flujo

print('-'*20)
print("Programa de Evaluacion de Notas de alumnos")

nota_alumno =int(input('Introduce la nota del alumno:\n'))

def evaluacion(nota):
    valoracion ="aprobado"

    if nota<5:
        valoracion = "suspenso"
    
    return valoracion

print(evaluacion(nota_alumno))

evaluacion(nota_alumno)
edad = 99

if 0<edad<100:
    print("Edad es Correcta")
else:
    print("Edad es incorrecta")
    salario_presidente = int(input('Introduce salario presidente\n'))
print('Salarios Presidente:', salario_presidente)

salario_director = int(input('Introduce salario director\n'))
print('Salarios Presidente:', salario_director)

salario_jefe_area = int(input('Introduce salario Jefe de Area\n'))
print('Salarios Presidente:', salario_jefe_area)

salario_administrativo = int(input('Introduce salario administrativo\n'))
print('Salarios Presidente:', salario_administrativo)

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('Todo funciona correctamente')
else:
    print('alfo falla en esta empresa')
"""
