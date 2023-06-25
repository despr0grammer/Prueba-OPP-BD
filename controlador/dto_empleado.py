from modelo.empleado import Empleado
from utils.encoder import Encoder
from dao.dao_empleado import daoEmpleado
from dao.dao_cliente import daoCliente

class EmpleadoDTO:
        
        def validarLogin(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.validarLogin(empleado)
        
        def addEmpleado(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.addEmpleado(empleado)
        
        def updateEmpleado(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.updateEmpleado(empleado)
        
        def deleteEmpleado(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.deleteEmpleado(empleado)
        
        def activateEmpleado(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.activateEmpleado(empleado)
        
        def getAllEmpleados(self):
            daoempleado = daoEmpleado()
            return daoempleado.getAllEmpleados()
        
        def getEmpleado(self, empleado):
            daoempleado = daoEmpleado()
            return daoempleado.getEmpleado(empleado)
        
        
        

