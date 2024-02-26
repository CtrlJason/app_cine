
#Inicio donde el usuario inicia la interaccion 
correo = ""
print("Bienvenido ala app cine Bogota")
inicio_cine()

#Menu del cine donde el usuario elige 3 opciones: Iniciar sesion, Registro y Salir
def inicio_cine():
    print("Oprima una de las siguientes opciones para interactuar con la plataforma")
    usuario = input("1 Iniciar sesion\n2 Registrarse\n3 Salir de la app")
    if usuario == 1:
        iniciar_sesion_cine()
    elif usuario == 2:
        registro_cine()
    elif usuario == 3:
        salir_cine()
        
#Inicio de sesion en la app (El usuario debe registrarse previamente)  
def iniciar_sesion_cine():
    print("Ha iniciado sesion satisfactoriamente")
    if correo != "" and cotraseña != "":
        menu_usuario()
    else:
        print("Usted aun no se ha registrado")
        iniciar_sesion_cine()
        
#Registro del usuario en la app (al finalizar el usuario debe regresar al menu de inicio)
def registro_cine():
    correo = input("Correo electronico: ")
    contraseña = input("Contraseña: ")
    inicio_cine()
#Menu del usuario que ya ha iniciado sesion con exito
def menu_usuario():
    print("Eliga alguna de las siguientes opciones para vender una entrada\n")
    usuario = input("1 Vender entradas\n2 Ver informe\n3 Volver \n4 Salir de la app")
    if usuario == 1:
        venta_entrada()
    elif usuario == 2:
        
        
def venta_entrada():
    print("ha comprado entradas")
        
def salir_cine():
    print("Ha salido de la app cine Bogota")