class Persona():
    def __init__(self, nombre="", dni="", email=""):
        self.nombre = nombre
        self.dni = dni
        self.email = email
    
    def __str__(self):
        return "Nombre: " + self.nombre + " - Dni: " + self.dni + " - Email: " + self.email
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDni(self):
        return self.dni
    
    def setDni(self, dni):
        self.dni = dni

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email