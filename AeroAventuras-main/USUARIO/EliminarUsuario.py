"""Lista temporal donde almacenamos la lista actualizada despues de eliminar un usuario"""
lista= []
"""Funcion eliminar usuario"""
def EliminarU (lista):
    """Se crea eliminar donde se almacena el valor ingresado por el usuario para eliminarlo de la lista, se crea una nueva lista donde se itera 
    y almacena todos los usuarios con son diferentes a la cedula ingresada por el usuario."""
    eliminar= int(input("Ingrese cedula para eliminar: "))
    lista= [usuario for usuario in lista if usuario['cedula'] != eliminar]   
    return lista