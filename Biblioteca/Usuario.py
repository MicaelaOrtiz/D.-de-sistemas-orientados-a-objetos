# Clase Usuario que hereda de Persona
class Usuario(Persona): 
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self._libros_prestados = []
#metodos
    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, titulo):
        for libro in self._libros_prestados:
            if libro.titulo.lower() == titulo.lower():
                libro.devolver()
                self._libros_prestados.remove(libro)
                return

    def mostrar_libros(self):
        return [libro.titulo for libro in self._libros_prestados]
