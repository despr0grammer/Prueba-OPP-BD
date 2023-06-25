from modelo.persona import Persona

class Empleado(Persona):
    def __init__(self, claveEmpleado="", nombreEmpleado="", dniEmpleado="", emailEmpleado="", estadoEmpleado=""):
        self.claveEmpleado = claveEmpleado
        self.nombreEmpleado = nombreEmpleado
        self.dniEmpleado = dniEmpleado
        self.emailEmpleado = emailEmpleado
        self.estadoEmpleado = estadoEmpleado
        super().__init__(nombreEmpleado, dniEmpleado, emailEmpleado)
    
    def __str__(self):
        return "Clave: " + self.claveEmpleado + " - Nombre: " + self.nombreEmpleado + " - Dni: " + self.dniEmpleado + " - Email: " + self.emailEmpleado + " - Estado: " + self.estadoEmpleado
    
    def getClaveEmpleado(self):
        return self.claveEmpleado
    
    def setClaveEmpleado(self, claveEmpleado):  
        self.claveEmpleado = claveEmpleado  

    def getNombreEmpleado(self):
        return self.nombreEmpleado
    
    def setNombreEmpleado(self, nombreEmpleado):
        self.nombreEmpleado = nombreEmpleado

    def getDniEmpleado(self):
        return self.dniEmpleado
    
    def setDniEmpleado(self, dniEmpleado):
        self.dniEmpleado = dniEmpleado

    def getEmailEmpleado(self):
        return self.emailEmpleado
    
    def setEmailEmpleado(self, emailEmpleado):
        self.emailEmpleado = emailEmpleado

    def getEstadoEmpleado(self):
        return self.estadoEmpleado

    def setEstadoEmpleado(self, estadoEmpleado):
        self.estadoEmpleado = estadoEmpleado


    
    