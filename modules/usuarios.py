import os
import modules.mensajes as mm

def usuarios ():
    try:
        print(mm.tituloMenuTableros)
        print(mm.menuTableros)
        gTableros = int(input('Ingrese que gestion desea realizar'))

    except:
        pass