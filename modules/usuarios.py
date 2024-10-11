import os
import modules.mensajes as mm

def usuarios ():
    try:
        gTableros = int(input('Ingrese que gestion desea realizar'))
        match gTableros():
            case 1 :
                print(mm.tituloMenuTableros())
                print(mm.menuTableros())
            case _ :
                print('Ingrese una opcion valida.')

    except:
        pass