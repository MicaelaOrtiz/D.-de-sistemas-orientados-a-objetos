# Clase base Persona
class Persona:
    def __init__(self, nombre, dni):
        self._nombre = nombre  # Encapsulado con _
        self._dni = dni

#metodo
    def mostrar_datos(self):
        return f"Nombre: {self._nombre}, DNI: {self._dni}"
