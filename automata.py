def automata(cadena):
    estado = 0
    esAceptada = False
    
    cadena +='#'
    
    for c in cadena:
        
        if estado == 0:
            if c == '0':
                
                estado = 1
            else:
                break
        elif estado ==1:
            if c == '1':
                
                estado =2
            else:
                break
        elif estado ==2:
            if c == '1':
                
                estado = 3
            else:
                break
        elif estado ==3:
            if c == '#':
                
                esAceptada = True
            elif c =='0' or c =='1':
               
                estado =3
            else:
                break
            
    return esAceptada
  
'''
automata que acepte numeros enteros con 
o sin signo y que separe con comas
'''

def esEntero(cadena):
    cadena +='#' # a este car final se la llama centinela
    estado = 0
    esAceptada = False
    
    for c in cadena:
        if estado == 0:
            if c == '+' or c == '-':
                estado = 1
            elif c.isdigit():
                estado =2
            else:
                break
        elif estado ==1:
            if c.isdigit():
                estado = 2
            else:
                break
        elif estado ==2:
            if c == '#':
                esAceptada = True
            elif c.isdigit():
                estado = 3
            elif c == ',':
                estado = 5
            else:
                break
        elif estado ==3:
            if c == '#':
                esAceptada = True
            elif c.isdigit():
                estado = 4
            elif c == ',':
                estado = 5
            else:
                break
        elif estado ==4:
            if c == '#':
                esAceptada = True
            
            elif c == ',':
                estado = 5
            else:
                break
        elif estado ==5:
            if c.isdigit():
                estado = 6
            else:
                break
        elif estado ==6:
            if c.isdigit():
                estado = 7
            else:
                break
        elif estado ==7:
            if c.isdigit():
                estado = 4
            else:
                break
    return esAceptada
if __name__ == '__main__':
    c1 = '011'
    c2 = '0123'
    c3 = '011'
    c4 = '123,567,555,430'
    
    
    print('cadena 1',esEntero(c1))
    print('cadena 2',esEntero(c2))
    print('cadena 3',esEntero(c3))
    print('cadena 4',esEntero(c4))
    