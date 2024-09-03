"""Se crea variable temporal"""
viajesDelete = []
# Función para eliminar viajes
def EliminarViaje(viajesDelete):
    # Si lista de viajes esta vacia imprimir un mensaje
    if not viajesDelete:
        print("No hay viajes para eliminar.")
        return viajesDelete
    # Solicita id del paquete a eliminar
    id_paquete = int(input("Ingrese el ID del paquete que desea eliminar: "))
    """Itera la lista viajes buscando el id proporcionado por el usuario y 
    se elimina el que cumpla la condición y sino imprime una mensaje de que no se encuentra"""
    for viaje in viajesDelete:
        if viaje["id"] == id_paquete:
            viajesDelete.remove(viaje)
            print(f"El viaje con ID {id_paquete} ha sido eliminado.")
            return viajesDelete
        else:
            print(f"No se encontró ningún viaje con el ID {id_paquete}.")
            return viajesDelete