from tkinter import *


root = Tk()

root.title('Ejemplo')

playa = IntVar()
ciudad = IntVar()
campo = IntVar()

def opcionesViaje():
    opcionEscogida = ''
    
    if(playa.get()==1):
        opcionEscogida+=' playa'
    if(ciudad.get()==1):
        opcionEscogida+=' ciudad'
    if(campo.get()==1):
        opcionEscogida+=' campo'

    textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file='icono.png')
Label(root,image=foto).pack()

frame = Frame(root)
frame.pack()
textoFinal = Label(frame)
Label(frame,text='Elige Destinos',width=50).pack()



Checkbutton(frame,text='Playa',variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text='Ciudad',variable=ciudad,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text='Campo',variable=campo,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()


root.mainloop()