#Definicion de variables a nivel global en la app  
usuario = ""
nombre_usuario = ""
contraseña = ""
#Funcion, venta de entradas
def venta():
    can_entrada = input("Escriba el numero de entradas ") #Construccion
    confirmacion = input("Ejila de las siguientes opciones\n [1] confirmar\n [2] cancelar")
    
    valor_total = int(can_entrada) * int(valor_entrada)

#Funcion para ver el informe de las ventas en la app
def informe(): #Construccion
    print(valor_total)
    
def menu_venta():
    usuario = input("Elija una las siguientes opciones\n\n [1] Vender entradas\n [2] ver informe\n [3] Salir")
    if usuario == "1":
        venta()
    elif usuario == "2":
        informe()   
        
#Registro del usuario en la app
def registrarse():
    usuario = input("Si desea registrarse oprima Enter o si desea salir seleccione [1]: ")
    if usuario == "1":
        salir()
        
    nombre_usuario = input("Escriba su nombre de usuario: ")
    contraseña = input("Escriba su contraseña: ")
    
    while nombre_usuario == "":
        print("Tiene que escribir un nombre de usuario")
    while contraseña == "":
        print("Tiene que escribir una contraseña")
    menu()

#Inicio de sesion de la app
def iniciar_sesion():
    global nombre_usuario, contraseña, usuario
    if nombre_usuario == "" and contraseña == "":
        input("Oprima Enter para registrese en la app: ")
        registrarse()
    print("Iniciar sesion\n\n")
    #Verificaciones para el inicio de sesion
    verificacion_usuario = input("Escriba su usuario: ")    
    verificacion_contraseña = input("Escriba su contraseña: ")
    
    #Verificamos que el nombre del usuario y la contraseña sean los mismos que registro el usuario
    while verificacion_usuario != nombre_usuario and verificacion_contraseña != contraseña and usuario != "3":
        if usuario == "3":
            salir()
            break
        usuario = input("Su usuario es incorrecto, elija una opcion\n\n [1] Reestablecer contraseña\n [2] Reestablecer nombre de usuario\n [3] Salir\n  ")
        while usuario != "1" and usuario != "2" and usuario != "3":
            usuario = input("Opcion no valida: ")
        if usuario == "1":
                nombre_usuario = input("Escriba un nuevo nombre de usuario: ")
                iniciar_sesion()
        elif usuario == "2":
                contraseña = input("Escriba una nueva contraseña")
                iniciar_sesion()
        elif usuario == "3":
            salir()        
        
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
#Valor de entradas
valor_entrada = 7200
#Usuario para verificacion
print("Bienvenido a la app Cine Ya")
input("Oprima enter para continuar")
menu()