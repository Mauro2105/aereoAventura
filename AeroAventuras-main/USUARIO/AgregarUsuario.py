"""Lista donde se almancen los usuarios"""
usuariosAdd = []

#funcion agregar
def AgregarU (usuariosAdd):
    """N es igual a la cantidad de personas que se van agregar"""
    N=1
    """Cree el usuario y lo agrega a la lista usuariosAdd"""
    if N == 1:
        nombre=str(input("Ingrese nombre: "))
        cedula= int(input("Ingrese cedula: "))
        contraseña= int(input("Ingrese contraseña: "))
        usuario= {"nombre" :nombre, "cedula" : cedula, "contraseña": contraseña}
        usuariosAdd.append(usuario)
        return usuariosAdd
    else:
        print ("Usuario Agregado")