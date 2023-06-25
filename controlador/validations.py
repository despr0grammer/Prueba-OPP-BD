from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_cliente import ClienteDTO
from utils.encoder import Encoder
#validarLogin
#addEmpleado
#updateEmpleado
#deleteEmpleado
#activateEmpleado
#getAllEmpleados
#getEmpleado
#addCliente
#updateCliente
#deleteCliente
#getAllClientes
#getCliente

#Esta funcion validarLogin se encarga de validar el login validando la contraseña de la base de datos con la contraseña ingresada por el usuario, si la contraseña es correcta, se le dará acceso al usuario, si la contraseña es incorrecta, se le pedirá al usuario que ingrese nuevamente la contraseña.

def validarLogin():
    claveEmpleado = input("Ingrese contraseña: ")
    return EmpleadoDTO().validarLogin(EmpleadoDTO(claveEmpleado=Encoder().encode(claveEmpleado)))

    

def addEmpleado():
    claveEmpleado = input("Ingrese contraseña: ")
    if len(claveEmpleado) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        return None
    nombreEmpleado = input("Ingrese nombre: ")
    if len(nombreEmpleado) < 3:
        print("El nombre debe tener al menos 3 caracteres")
        return None
    dniEmpleado = input("Ingrese dni: ")
    if len(dniEmpleado) != 8:
        print("El dni debe tener 8 caracteres")
        return None
    emailEmpleado = input("Ingrese email: ")
    if len(emailEmpleado) < 10:
        print("El email debe tener al menos 10 caracteres")
        return None
    return EmpleadoDTO().addEmpleado(EmpleadoDTO(claveEmpleado=Encoder().encode(claveEmpleado), nombreEmpleado=nombreEmpleado,dniEmpleado=dniEmpleado, emailEmpleado=emailEmpleado))


#Esta función modifica los datos del empleado, se le pide al usuario que ingrese los datos que desea modificar. Debe ingresar el dni del empleado que desea modificar. Y debe verificar que el dni ingresado sea correcto y que exista en la base de datos.

def updateEmpleado():
    dniEmpleado = input("Ingrese dni: ")
    if len(dniEmpleado) != 8:
        print("El dni debe tener 8 caracteres")
        return None
    nombreEmpleado = input("Ingrese nombre: ")
    if len(nombreEmpleado) < 3:
        print("El nombre debe tener al menos 3 caracteres")
        return None
    emailEmpleado = input("Ingrese email: ")
    if len(emailEmpleado) < 10:
        print("El email debe tener al menos 10 caracteres")
        return None
    return EmpleadoDTO().updateEmpleado(EmpleadoDTO(dniEmpleado=dniEmpleado, nombreEmpleado=nombreEmpleado, emailEmpleado=emailEmpleado))

def deleteEmpleado():
    #Esta funcion pide el dni para poder eliminar el empleado, no se elimina de la base de datos, se le cambia el estado de True a False en la base de datos.
    dniEmpleado = input("Ingrese dni: ")
    if len(dniEmpleado) != 8:
        print("El dni debe tener 8 caracteres")
        return None
    return EmpleadoDTO().deleteEmpleado(EmpleadoDTO(dniEmpleado=dniEmpleado))

#La función activateEmpleado se encarga de activar un empleado, para esto se pide el dni del empleado, si el dni no existe en la base de datos, se le pedirá al usuario que ingrese otro dni, si el dni existe, se activará el empleado.
#En caso de existir cambiara su estado de False a True.
#Esta función necesita validaciones

def activateEmpleado():
    dniEmpleado = input("Ingrese dni: ")
    if len(dniEmpleado) != 8:
        print("El dni debe tener 8 caracteres")
        return None
    return EmpleadoDTO().activateEmpleado(EmpleadoDTO(dniEmpleado=dniEmpleado))


def getAllEmpleados():
    return EmpleadoDTO().getAllEmpleados()

def getEmpleado():
    claveEmpleado = input("Ingrese contraseña: ")
    return EmpleadoDTO().getEmpleado(EmpleadoDTO(claveEmpleado=Encoder().encode(claveEmpleado)))
#La función addCliente se encarga de agregar un cliente a la base de datos, para esto se pide el nombre, dni, telefono y email del cliente, si el dni ya existe en la base de datos, se le pedirá al usuario que ingrese otro dni, si el dni no existe, se agregará el cliente a la base de datos.
#Cada función necesita validaciones, por lo que podemos usar este archivo para validar los datos de entrada y luego llamar a la función del archivo dto
def addCliente():
    nombreCliente = input("Ingrese nombre: ")
    if len(nombreCliente) < 3:
        print("El nombre debe tener al menos 3 caracteres")
        return None
    apellidoCliente = input("Ingrese apellido: ")
    if len(apellidoCliente) < 3:
        print("El apellido debe tener al menos 3 caracteres")
        return None
    dniCliente = input("Ingrese dni: ")
    if len(dniCliente) != 8:
        print("El dni debe tener 8 caracteres")
        return None
    telefonoCliente = input("Ingrese telefono: ")
    if len(telefonoCliente) != 9:
        print("El telefono debe tener 9 caracteres")
        return None
    emailCliente = input("Ingrese email: ")
    if len(emailCliente) < 10:
        print("El email debe tener al menos 10 caracteres")
        return None
    return ClienteDTO().addCliente(ClienteDTO(nombreCliente=nombreCliente, apellidoCliente=apellidoCliente, dniCliente=dniCliente, telefonoCliente=telefonoCliente, emailCliente=emailCliente))



def updateCliente():
    nombreCliente = input("Ingrese nombre: ")
    apellidoCliente = input("Ingrese apellido: ")
    dniCliente = input("Ingrese dni: ")
    telefonoCliente = input("Ingrese telefono: ")
    emailCliente = input("Ingrese email: ")
    return ClienteDTO().updateCliente(ClienteDTO(nombreCliente=nombreCliente, apellidoCliente=apellidoCliente, dniCliente=dniCliente, telefonoCliente=telefonoCliente, emailCliente=emailCliente))

def deleteCliente():
    dniCliente = input("Ingrese dni: ")
    return ClienteDTO().deleteCliente(ClienteDTO(dniCliente=dniCliente))

def getAllClientes():
    return ClienteDTO().getAllClientes()

def getCliente():
    dniCliente = input("Ingrese dni: ")
    return ClienteDTO().getCliente(ClienteDTO(dniCliente=dniCliente))




def menu():
    
    print("1. CRUD Empleados")
    print("2. CRUD Clientes")
    print("3. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc

def crudEmpleados():
    print("1. Ingresar Vendedor")
    print("2. Modificar Vendedor")
    print("3. Eliminar Vendedor")
    print("4. Activar Vendedor")
    print("5. Mostrar todos los Vendedores")
    print("6. Volver al menú principal")
    opc = int( input("Ingrese una opción : "))
    return opc

def crudClientes():
    print("1. Ingresar Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Mostrar todos los Clientes")
    print("5. Volver al menú principal")
    opc = int( input("Ingrese una opción : "))
    return opc
#Esta funcion define el menú principal, se le pide al usuario que ingrese una opción, si la opción es 1, se llama a la función crudEmpleados, si la opción es 2, se llama a la función crudClientes, si la opción es 3, se sale del programa.
def inicial():
    opc = menu()
    while opc != 3:
        if opc == 1:
            opc = crudEmpleados()
            while opc != 6:
                if opc == 1:
                    addEmpleado()
                elif opc == 2:
                    updateEmpleado()
                elif opc == 3:
                    deleteEmpleado()
                elif opc == 4:
                    activateEmpleado()
                elif opc == 5:
                    print(getAllEmpleados())
                else:
                    print("Opción no válida")
                opc = crudEmpleados()
        elif opc == 2:
            opc = crudClientes()
            while opc != 5:
                if opc == 1:
                    addCliente()
                elif opc == 2:
                    updateCliente()
                elif opc == 3:
                    deleteCliente()
                elif opc == 4:
                    print(getAllClientes())
                else:
                    print("Opción no válida")
                opc = crudClientes()
        else:
            print("Opción no válida")
        opc = menu()
