from conex import conn
import traceback

class daoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "admin", "", "mydb")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    print(conn)

#la función validarLogin() es la que se encarga de validar el usuario y la contraseña del empleado, donde el usuario es el correo electrónico
#y la contraseña es la contraseña del empleado
    def validarLogin(self, empleado):
        sql = "select * from empleado where EMAIL = %s and CONTRASENA = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getCorreo(),empleado.getContraseña()))
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def addEmpleado(self,empleado):
        #esta función se encarga de añadir un empleado a la base de datos con los datos que se le pasan por parámetro los cuáles son nombre, dni, email y contraseña
        sql = "insert into empleado (NOMBRE, DNI, EMAIL, CONTRASENA) values (%s, %s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getNombre(),empleado.getDni(),empleado.getCorreo(),empleado.getContraseña()))
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def updateEmpleado(self,empleado):
        #esta función se encarga de actualizar los datos de un empleado en la base de datos, buscando por su dni, Este método debe permitir modificar solo nombre, correo y contraseña de la tabla vendedor. Antes de realizar la modificación, se debe validar que el vendedor se encuentre (utilizar el método findVendedor() para la búsqueda del vendedor). De NO existir, se debe enviar mensaje respectivo y no permitir la modificación. 
        sql = "update empleado set NOMBRE = %s, EMAIL = %s, CONTRASENA = %s where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getNombre(),empleado.getCorreo(),empleado.getContraseña(),empleado.getDni()))
            c.getConex().commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def activateEmpleado(self,empleado):
        #Esta función se encarga de activar un empleado en la base de datos, buscando por su dni
        sql = "update empleado set ESTADO = %s where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getEstado(),empleado.getDni()))
            c.getConex().commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def deleteEmpleado(self,empleado):
        #Este método debe permitir eliminar un vendedor de la tabla vendedor, según rut del vendedor (la eliminación solo será un cambio en el estado del vendedor True=activado, False=eliminado). Además, se debe realizar una pregunta de confirmación de eliminación, para proceder con la baja del vendedor.  Antes de realizar la eliminación, se debe validar que el vendedor se encuentra (utilizar el método findVendedor() para la búsqueda). De NO existir, se debe enviar mensaje respectivo y no realizar eliminación.
        sql = "update empleado set ESTADO = %s where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getEstado(),empleado.getDni()))
            c.getConex().commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def findEmpleado(self,empleado):
        #Esta función se encarga de buscar un empleado en la base de datos por su dni
        sql = "select * from empleado where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getDni(),))
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    #Esta función mostrará todos los empleados
    def findAllEmpleado(self):
        sql = "select * from empleado"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    #Esta función mostrará todos los empleados que estén activos
    def findAllEmpleadoActivos(self):
        sql = "select * from empleado where ESTADO = 1"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    #Esta función mostrará todos los empleados que estén inactivos
    def findAllEmpleadoInactivos(self):
        sql = "select * from empleado where ESTADO = 0"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

