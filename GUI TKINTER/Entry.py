from tkinter import *

raiz = Tk()
raiz.iconbitmap('icono.ico')
miFrame = Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()#esto dice que es un string
                                #textvariable asigna la variable al entry
cuadroNombre = Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row = 0,column=1,padx=6,pady=15)
cuadroNombre.config(fg = 'red',justify='center')

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 1,column=1,padx=6,pady=15)
cuadroPass.config(fg = 'red',justify='center',show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 2,column=1,padx=6,pady=15)
cuadroApellido.config(fg = 'red',justify='center')

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 3,column=1,padx=6,pady=15)
cuadroDireccion.config(fg = 'red',justify='center')

textoComentario = Text(miFrame,width=16,height=5)
textoComentario.grid(row = 4,column=1,padx=6,pady=15)
textoComentario.config(fg = 'red')

scrollVert = Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky='nsew')

#--> esto agrega el comportamiento de seguir el scroll
textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame,text='Nombre: ')
nombreLabel.grid(row=0,column =0,sticky='w')

apellidoLabel = Label(miFrame,text='Apellido: ')
apellidoLabel.grid(row=2,column =0,sticky='w')

direccionLabel = Label(miFrame,text='Direccion: ')
direccionLabel.grid(row=3,column =0,sticky='w')

passLabel = Label(miFrame,text='Password: ')
passLabel.grid(row=1,column =0,sticky='w')



comentariosLabel = Label(miFrame,text='Comentarios: ')
comentariosLabel.grid(row=4,column =0,sticky='w')


#========| GRID |============

def codigoBoton():
    minombre.set('Eduardo')
                                            #command dice la funcion
botonEnvio = Button(miFrame,text='Enviar',command=codigoBoton)
botonEnvio.grid(row=5,column =1)

raiz.mainloop()