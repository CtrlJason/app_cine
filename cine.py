import os

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
 
 
     
#Definicion de variables a nivel global en la app  
#
usuario = ""
nombre_usuario = ""
contraseña = ""
global can_entrada
#
registro_usuario = ["",""]

#Funcion, venta de entradas
def venta():
    #--------------------#
    usuario = ""
    valor_entrada = 7200
    #--------------------#
    can_entrada = input("Escriba el numero de entradas ") #Construccion
    confirmacion = input("Ejila una de las siguientes opciones\n [1] confirmar\n [2] cancelar\n  ")
    while can_entrada != "1" and confirmacion != "2":
        if usuario == "1":
            usuario = input("Opcion no valida, para confirmar entrada seleccion [1] de lo contrario seleccione [2]: ")
        elif usuario == "2":
            salir()
            break
    valor_total = int(can_entrada) * valor_entrada
    print("Cantidad de entradas: ", can_entrada,"\n\nValor total: ", valor_total)
    usuario = input("\nElija una de las siguientes opciones\n comprar mas entradas [1]\n Volver [2]\n Salir de la app [3]\n  ")
    if usuario == "1":
        venta()
    elif usuario == "2":
        menu_venta()
    elif usuario == "3":
        salir()
        
    
#Funcion para ver el informe de las ventas en la app
def informe(): #Construccion
    print("La cantidad total de entradas vendidas es de: ", can_entrada,"\n\nLa cantidad de dinero readado es de: " ,valor_total)
    usuario = input("\nElija una de las siguientes opciones\n Volver [1]\n Salir de la app [2]")
    while usuario != "1" and usuario != "2":
        if usuario == ["1"]:
            menu_venta()
        elif usuario == ["2"]:
            salir()
#Menu para realizar ventas o ver el informe        
def menu_venta():
    print("¡Cine Ya!")
    usuario = input("\nElija una las siguientes opciones\n\n [1] Vender entradas\n [2] ver informe\n [3] Salir\n  ")
    if usuario == "1":
        venta()
    elif usuario == "2":
        informe()   
    elif usuario == "3":
        salir()
        
#Registro del usuario en la app
def registrarse():
    usuario = input("\nSi desea registrarse oprima Enter o si desea salir seleccione [1]: ")
    if usuario == "1":
        salir()
    else:    
        nombre_usuario = input("Escriba su nombre de usuario: ")
        contraseña = input("Escriba su contraseña: ")
        registro_usuario.insert(0, nombre_usuario)
        registro_usuario.insert(1, contraseña)
        
        while nombre_usuario == "":
            input("Tiene que escribir un nombre de usuario: ")
        while contraseña == "":
            input("Tiene que escribir una contraseña: ")
        menu()

#Inicio de sesion de la app
def iniciar_sesion():
    global nombre_usuario, contraseña, usuario
    if nombre_usuario == registro_usuario[0] and contraseña == registro_usuario[1]:
        input("\nOprima Enter para registrese en la app: ")
        registrarse()
    else:
        print("\nIniciar sesion\n\n")
        #Verificaciones para el inicio de sesion
        verificacion_usuario = input("Escriba su usuario: ")    
        verificacion_contraseña = input("Escriba su contraseña: ")
        
    if usuario == "3":
                salir()
                
    else:
        #Verificamos que el nombre del usuario y la contraseña sean los mismos que registro el usuario
        while verificacion_usuario == nombre_usuario and verificacion_contraseña == contraseña:
            usuario = input("Su usuario es incorrecto, elija una opcion\n\n[1] Reestablecer nombre de usuario [2]\n Reestablecer contraseña\n  [3] Salir\n  ")
            while usuario != "1" and usuario != "2" and usuario != "3":
                usuario = input("Opcion no valida: ")
            if usuario == "1":
                nombre_usuario = input("Escriba un nuevo nombre de usuario: ")
                iniciar_sesion()
                break
            elif usuario == "2":
                contraseña = input("Escriba una nueva contraseña")
                iniciar_sesion()
                break
            elif usuario == "3":
                salir()  
                break
    clean()
    menu_venta()
              
        
#Boton de salida para cerra la app
def salir():
    print("ha salido de la app con exito")
    breakpoint
#Menu de usuario   
def menu(): 
    usuario = input("\nEliga una las siguientes opciones\n\n [1] iniciar sesion\n [2] registrarse\n [3] salir\n  ")

    #Verificacion de usuario
    while usuario != "1" and usuario != "2" and usuario != "3":
        usuario = input("Opcion no valida, si deseas regresar al menu de inicio oprima 2 o si desea salir oprima 2: ")
    if usuario == "1":
        iniciar_sesion()
    elif usuario == "2":
        registrarse()
    elif usuario == "3":
        salir()

#Bienvenida (se ejecuta primero)

#Usuario para verificacion
print("Bienvenido a la app Cine Ya\n")
input("Oprima enter para continuar\n")
menu()