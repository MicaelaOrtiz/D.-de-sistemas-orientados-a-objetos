from abc import ABC, abstractmethod

class Persona(ABC):
    """
    Clase abstracta que define el concepto básico de una persona.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def descripcion(self):
        """
        Método abstracto que debe ser implementado por las clases hijas.
        Describe la persona.
        """
        pass
