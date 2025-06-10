class Gestion:
    """
    Clase singleton que administra las personas (empleados y clientes).
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Gestion, cls).__new__(cls)
            cls.__instance.personas = []
        return cls.__instance

    def agregar_persona(self, persona):
        """
        Agrega una persona a la lista de gestión.
        """
        self.personas.append(persona)

    def mostrar_personas(self):
        """
        Muestra la descripción de todas las personas almacenadas.
        """
        if not self.personas:
            print("No hay personas registradas.")
        for p in self.personas:
            print(p.descripcion())
