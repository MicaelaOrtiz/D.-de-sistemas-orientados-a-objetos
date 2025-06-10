from persona import Persona

class Empleado(Persona):
    """
    Clase que representa un empleado, hereda de Persona.
    """

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def descripcion(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"

class EmpleadoTemporal(Empleado):
    """
    Empleado temporal con duración de contrato.
    """

    def __init__(self, nombre, edad, salario, duracion_contrato):
        super().__init__(nombre, edad, salario)
        self.duracion_contrato = duracion_contrato

    def descripcion(self):
        return (super().descripcion() +
                f", Contrato por: {self.duracion_contrato} meses")

class EmpleadoFijo(Empleado):
    """
    Empleado fijo con beneficios.
    """

    def __init__(self, nombre, edad, salario, beneficios):
        super().__init__(nombre, edad, salario)
        self.beneficios = beneficios

    def descripcion(self):
        return (super().descripcion() +
                f", Beneficios: {self.beneficios}")
