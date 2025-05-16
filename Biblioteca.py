class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
#metodos
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro.esta_disponible():
                print(f"{libro.titulo} - {libro.autor}")

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and libro.esta_disponible():
                if libro.prestar():
                    usuario.prestar_libro(libro)
                    return

    def devolver_libro(self, titulo, usuario):
        usuario.devolver_libro(titulo)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.mostrar_datos(), "Libros:", usuario.mostrar_libros())


if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "123456")
    libro2 = Libro("1984", "George Orwell", "654321")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Crear y registrar usuario
    usuario1 = Usuario("María", "12345678")
    biblioteca.registrar_usuario(usuario1)

    # Mostrar libros disponibles
    biblioteca.mostrar_libros_disponibles()

    # Prestar un libro
    biblioteca.prestar_libro("El Principito", usuario1)

    # Mostrar libros del usuario
    print(f"\nLibros prestados a {usuario1._nombre}: {usuario1.mostrar_libros()}")

    # Devolver libro
    biblioteca.devolver_libro("El Principito", usuario1)

    # Mostrar estado final
    biblioteca.mostrar_libros_disponibles()
    biblioteca.mostrar_usuarios()


