import os 
import modules.usuarios as mu
import modules.mensajes as mm

if (__name__ == "__main__"):

    def tableros():
        try:
            menu = input('=>')
            print(mm.tituloMenuTableros())
            print(mm.menutarjetas())
            os.system('clear')

            match menu():
                case 1:
                    print(mu.usuarios())
                case _ :
                    print('Ingrese una opcion valida.')



        
        except:
            pass