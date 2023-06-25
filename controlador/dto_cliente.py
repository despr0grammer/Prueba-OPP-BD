from modelo.cliente import Cliente
from dao.dao_cliente import daoCliente

class ClienteDTO:
    
        def addCliente(self, cliente):
            daocliente = daoCliente()
            return daocliente.addCliente(cliente)
        
        def updateCliente(self, cliente):
            daocliente = daoCliente()
            return daocliente.updateCliente(cliente)
        
        def deleteCliente(self, cliente):
            daocliente = daoCliente()
            return daocliente.deleteCliente(cliente)
        
        def getAllClientes(self):
            daocliente = daoCliente()
            return daocliente.getAllClientes()
        
        def getCliente(self, cliente):
            daocliente = daoCliente()
            return daocliente.getCliente(cliente)
        
        def getClienteByDni(self, cliente):
            daocliente = daoCliente()
            return daocliente.getClienteByDni(cliente)
        
        
