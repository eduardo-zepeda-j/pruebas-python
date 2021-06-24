file = open(input(('Inserte ruta de archivo a leer\n')),'r')
for line in file:
    print(line)

file.close()
