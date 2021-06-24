from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Juego Proyecto 1')
root.iconbitmap('icono.ico')
# ---------------> ventana emergente


def infoAdicional():
    messagebox.showinfo('Juego Proyecto', 'Eduardo Zepeda - 201612386')


def avisoLicencia():
    messagebox.showwarning('Licencia', 'Producto Bajo Licencia GNU')


def salirAplicacion():
    #valor = messagebox.askquestion('Salir', 'Deseas salir?')

    valor = messagebox.askokcancel('Salir', 'Deseas salir?')

    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel('Reintentar', 'No es posible cerrar')
    if valor == False:
        root.destroy()
    
    else:
        print(valor)
# ----------------------------


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# --------> Esto agrega los elementos a cada menu de la barra
archivoMenu = Menu(barraMenu, tearoff=False)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar Como')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar',command=cerrarDocumento)
archivoMenu.add_command(label='Salir', command=salirAplicacion)


archivoEdicion = Menu(barraMenu, tearoff=False)
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')


archivoHerramientas = Menu(barraMenu, tearoff=False)
archivoAyuda = Menu(barraMenu, tearoff=False)
archivoAyuda.add_command(label='Licencia', command=avisoLicencia)
archivoAyuda.add_command(label='Acerca de', command=infoAdicional)


# -------> esto agrega los botones a la barra
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edicion', menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas', menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)


root.mainloop()
