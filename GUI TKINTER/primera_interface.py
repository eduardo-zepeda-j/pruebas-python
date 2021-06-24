from tkinter import *

raiz = Tk()
raiz.title('Ventana de Pruebas')
#Es como poner false false, x,y
#raiz.resizable(0,0)
raiz.geometry('900x700')
raiz.config(bg='gray')
raiz.iconbitmap('icono.ico')
#-------> Main Loop debe ser lo ultimo 

miFrame = Frame()
#Fill para hacer fill = 'x' si usamos fill y usamos fill='y', expand = True
miFrame.pack(side = 'left',anchor='s')
miFrame.config(bg = 'red')
miFrame.config(width='650',height ='350')
miFrame.config(bd=35)
#groove , sunken 
miFrame.config(relief = 'groove')
miFrame.config(cursor = 'hand2')



raiz.mainloop()