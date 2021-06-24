from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    
    fichero = filedialog.askopenfilename(title = 'Abrir',initialdir='c:Desktop',filetypes=(('Ficheros de Excel','*.xlsx'),
    ('Ficheros de texto','*.txt'),('Todos los ficheros','*.*')))
    file = open(fichero,'r')
    print(fichero)
    for i in file:
        print(i)

Button(root,text='abrir fichero',command = abreFichero).pack()

root.mainloop()