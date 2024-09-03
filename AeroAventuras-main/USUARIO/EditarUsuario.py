"""Lista temporal para agregar usuarios"""
usuariosAdd = []

# Función para editar usuarios
def EditarU(usuariosAdd):
    """Se imprime la lista actual y se pide al usuario ingresar la cedula que desea editar"""
    print ("Esta es la lista actual", usuariosAdd)
    cedula = int(input("Ingrese la cédula del usuario a editar: "))
    """Recorre la lista de usuarios actual y verifica si la cedula existe para actualizar los datos"""
    for i in usuariosAdd:
        if i["cedula"] == cedula:
            nueva_cedula = int(input("Ingrese nueva cc: "))
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_contraseña = int(input("Ingrese nueva contraseña: "))
            if nueva_cedula:
                i["cedula"] = nueva_cedula
            if nuevo_nombre:
                i["nombre"] = nuevo_nombre  
            if nueva_contraseña:
                i["contraseña"] = nueva_contraseña
            
            print("lista actualizada:", usuariosAdd)
            break     
        return usuariosAdd
    else:
        print("Usuario no encontrado.")