from modelo.persona import Persona


class Cliente(Persona):
    def __init__(self, claveCliente="", nombreCliente="", dniCliente="", emailCliente="", estadoCliente=""):
        self.claveCliente = claveCliente
        self.nombreCliente = nombreCliente
        self.dniCliente = dniCliente
        self.emailCliente = emailCliente
        self.estadoCliente = estadoCliente
        super().__init__(nombreCliente, dniCliente, emailCliente)
    
    def __str__(self):
        return "Clave: " + self.claveCliente + " - Nombre: " + self.nombreCliente + " - Dni: " + self.dniCliente + " - Email: " + self.emailCliente + " - Estado: " + self.estadoCliente
    
    def getClaveCliente(self):
        return self.claveCliente
    
    def setClaveCliente(self, claveCliente):  
        self.claveCliente = claveCliente  

    def getNombreCliente(self):
        return self.nombreCliente
    
    def setNombreCliente(self, nombreCliente):
        self.nombreCliente = nombreCliente

    def getDniCliente(self):
        return self.dniCliente
    
    def setDniCliente(self, dniCliente):
        self.dniCliente = dniCliente

    def getEmailCliente(self):
        return self.emailCliente
    
    def setEmailCliente(self, emailCliente):
        self.emailCliente = emailCliente

    def getEstadoCliente(self):
        return self.estadoCliente

    def setEstadoCliente(self, estadoCliente):
        self.estadoCliente = estadoCliente

    def addCliente(self, clienteDTO):
        return clienteDTO.addCliente(clienteDTO)
    
    def updateCliente(self, clienteDTO):
        return clienteDTO.updateCliente(clienteDTO)
    
    def deleteCliente(self, clienteDTO):
        return clienteDTO.deleteCliente(clienteDTO)
