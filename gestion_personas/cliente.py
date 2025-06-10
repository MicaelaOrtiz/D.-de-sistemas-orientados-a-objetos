from persona import Persona

class Cliente(Persona):
    """
    Clase que representa un cliente, hereda de Persona.
    """

    def __init__(self, nombre, edad, email):
        super().__init__(nombre, edad)
        self.email = email

    def descripcion(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Email: {self.email}"
