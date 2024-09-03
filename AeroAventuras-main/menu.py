from USUARIO.AgregarUsuario import AgregarU
from USUARIO.EditarUsuario import EditarU
from USUARIO.EliminarUsuario import EliminarU
from VIAJE.AgregarViaje import AgregarViaje
from VIAJE.EditarViaje import EditarViaje
from VIAJE.EliminarViaje import EliminarViaje

usuarios = []
viajes = []

"""mostrar_menu() esta función me trae el menú de opciones para interactuar con la plataforma"""
def mostrar_menu():
    print("==========menu==========")
    print("Escriba el número de la opción que desea")
    print("1) Agregar usuario")
    print("2) Eliminar usuario")
    print("3) Editar usuario")
    print("4) Agregar viaje")
    print("5) Cambiar viaje")
    print("6) Eliminar viaje")
    print("7) Salir")
    print("========================")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        usuarios = AgregarU(usuarios)
        print("Lista de usuarios: ", usuarios)
        print("========================")
    elif opcion == "2":
        usuarios = EliminarU(usuarios)
        print("Lista de usuarios actualizada: ", usuarios)
        print("========================")
    elif opcion == "3":
        usuarios = EditarU(usuarios)
        print("========================")
    elif opcion == "4":
        viajes = AgregarViaje(viajes)  
        print("Lista de viajes: ", viajes)
        print("========================")
    elif opcion == "5":
        viajes = EditarViaje(viajes)  
        print("Lista actualizada de viajes: ", viajes)
        print("========================")    
    elif opcion == "6":
        viajes = EliminarViaje(viajes)  
        print("Lista actualizada de viajes: ", viajes)
        print("========================")
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
