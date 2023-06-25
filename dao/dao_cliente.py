from conex import conn
import traceback

class daoCliente:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "admin", "", "mydb")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    print(conn)


    def addCliente(self,cliente):
        sql = "insert into cliente (NOMBRE, DNI, TELEFONO, EMAIL) values (%s, %s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getNombreCliente(),cliente.getDniCliente(),cliente.getTelefonoCliente(),cliente.getEmailCliente()))
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def updateCliente(self,cliente):
        sql = "update cliente set NOMBRE = %s, DNI = %s, TELEFONO = %s, EMAIL = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getNombreCliente(),cliente.getDniCliente(),cliente.getTelefonoCliente(),cliente.getEmailCliente()))
            c.getConex().commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def deleteCliente(self,cliente):
        #Esta función se encarga de eliminar un cliente de la base de datos buscando por su dni
        sql = "delete from cliente where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getDniCliente()))
            c.getConex().commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def getAllClientes(self):
        sql = "select * from cliente"
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
    
    def getCliente(self,cliente):
        #esta función se encarga de buscar un cliente por su dni
        sql = "select * from cliente where DNI = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getDniCliente()))
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    
    
