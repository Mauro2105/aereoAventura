"""Se crea lista temportal y un diccionario con las opciones de los hoteles"""
viajesAdd = []
hoteles = {"1": "hotel 5 estrellas", "2": "hotel 3 estrellas", "3": "hotel 1 estrella"}

def AgregarViaje(viajesAdd):
    """N es igual a la cantidad de personas que se van agregar"""
    N = 1 
    
    """Se crea el viaje, se ingresa el destino y el id del paquete, 
    luego se llama la funcion mostrarOpciones, 
    se da el valor del hotel y los dias que va hospedarse
    y lo agrega a la lista viajesAdd"""
    if N == 1:
        destino = input("Ingrese cuidad de destino: ")
        id = int (input ("Ingrese un nuemero de id para su paquete:"))
        """Se convierte las llaves del diccionario en una lista"""
        hotel = mostrarOpciones(list(hoteles.keys()), "escoja hotel")
    
        if hotel == "1":
            Valor_hotel = 1000000
        elif hotel == "2":
            Valor_hotel = 500000
        elif hotel == "3":
            Valor_hotel = 250000
        else:
            print("Opción de hotel no válida")
            return 
        
        dias = int(input("Ingrese días a quedarse: "))
        valor_dia = dias * 100000
        total = Valor_hotel + valor_dia
        
        viaje = {"id": id, "destino": destino, "hotel": hoteles[hotel], "dias": dias, "total": total}
        viajesAdd.append(viaje)
        
        return viajesAdd
    else:
        print("Error, vuelva a intentarlo")
"""Esta función se utiliza para mostrar las opciones de una lista, y se le pide al usuario 
que ingrese una opción según el indice y el tamaño de la lista iniciando desde uno"""
def mostrarOpciones(lista, tipo):
    print(f"Seleccione su {tipo}: ")
    for indice, valor in enumerate(lista, 1):
        print(f"{indice}. {hoteles[valor]}")
    opcion = int(input(f"Seleccione una opción (1-{len(lista)}): "))
    return lista[opcion - 1]