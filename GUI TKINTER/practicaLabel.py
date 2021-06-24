from tkinter import *

root = Tk()

miFrame = Frame(root,width = 500,height = 500)
root.iconbitmap('icono.ico')
miFrame.pack()

miImagen = PhotoImage(file='icono.png')

#miLabel = Label(miFrame,text='Hola Mundo',fg='red',font=('Fira Code',18)).place(x=100,y=50)
#--> agregando imagen
Label(miFrame,image=miImagen).place(x=100,y=50)
root.mainloop()