import os

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
 
 
     
#Definicion de variables a nivel global en la app  
#-------------------#
usuario = ""
nombre_usuario = ""
contraseña = ""
can_entrada = 0
valor_total = 0
#-------------------#
registro_usuario = ["",""]

#Funcion para procesar las ventas y almacenado en informe
def proceso_venta():    
    valor_total = can_entrada * valor_entrada
    print("\nCantidad de entradas: ", can_entrada,"\nValor total: ", valor_total)
    usuario = input("\nElija una de las siguientes opciones\n[1] comprar mas entradas \n[2] Volver \n[3] Salir de la app\n  ")
    if usuario == "1":
        clean()
        venta()
    elif usuario == "2":
        clean()
        menu_venta()
    elif usuario == "3":
        clean()
        salir()

#Funcion, venta de entradas
def venta():
    global can_entrada, valor_total, valor_entrada
    #--------------------#
    usuario = ""
    valor_entrada = 7200
    #--------------------#
    can_entrada = int(input("Escriba el numero de entradas ")) #Construccion
    confirmacion = input("Ejila una de las siguientes opciones\n [1] confirmar\n [2] cancelar\n  ")
    while confirmacion != "1" and confirmacion != "2":
        confirmacion = input("Opcion no valida, para confirmar entrada seleccion [1] de lo contrario seleccione [2]: ")
        if confirmacion == "1":
            clean()
            proceso_venta()
            break
        elif confirmacion == "2":
            clean()
            salir()
            break
    proceso_venta()
    
#Funcion para ver el informe de las ventas en la app
def informe(): #Construccion
    print("La cantidad total de entradas vendidas es de:", can_entrada,"\n\nLa cantidad de dinero recaudado es de:", valor_total)
    usuario = input("\nElija una de las siguientes opciones\n[1] Volver \n[2] Salir de la app \n  ")
    while usuario != "1" and usuario != "2":
        if usuario == ["1"]:
            clean()
            menu_venta()
        elif usuario == ["2"]:
            clean()
            salir()
#Menu para realizar ventas o ver el informe        
def menu_venta():
    global usuario
    print("¡Cine Ya!")
    usuario = input("\nElija una las siguientes opciones\n\n[1] Vender entradas\n[2] ver informe\n[3] Salir\n  ")
    if usuario == "1":
        clean()
        venta()
    elif usuario == "2":
        clean()
        informe()   
    elif usuario == "3":
        clean()
        salir()
        
#Registro del usuario en la app
def registrarse():
    usuario = input("\nSi desea registrarse oprima Enter o si desea salir seleccione [1]: ")
    if usuario == "1":
        clean()
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
        clean()
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
        clean()
        salir()
                
    else:
        #Verificamos que el nombre del usuario y la contraseña sean los mismos que registro el usuario
        while verificacion_usuario != nombre_usuario and verificacion_contraseña != contraseña:
            usuario = input("Su usuario es incorrecto, elija una opcion\n\n[1] Reestablecer nombre de usuario\n[2] Reestablecer contraseña\n[3] Salir\n  ")
            while usuario != "1" and usuario != "2" and usuario != "3":
                usuario = input("Opcion no valida: ")
            if usuario == "1":
                nombre_usuario = input("Escriba un nuevo nombre de usuario: ")
                clean()
                iniciar_sesion()
                break
            elif usuario == "2":
                contraseña = input("Escriba una nueva contraseña")
                clean()
                iniciar_sesion()
                break
            elif usuario == "3":
                clean()
                salir()  
                break
    clean()
    menu_venta()
              
        
#Boton de salida para cerra la app
def salir():
    print("ha salido de la app con exito")
#Menu de usuario   
def menu(): 
    usuario = input("\nEliga una las siguientes opciones\n\n [1] iniciar sesion\n [2] registrarse\n [3] salir\n  ")

    #Verificacion de usuario
    while usuario != "1" and usuario != "2" and usuario != "3":
        usuario = input("Opcion no valida, si deseas regresar al menu de inicio oprima 2 o si desea salir oprima 2: ")
    if usuario == "1":
        clean()
        iniciar_sesion()
    elif usuario == "2":
        clean()
        registrarse()
    elif usuario == "3":
        clean()
        salir()

#Bienvenida (se ejecuta primero)

#Usuario para verificacion
print("Bienvenido a la app Cine Ya\n")
input("Oprima enter para continuar\n")
clean()
menu()