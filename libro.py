class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self._disponible = True
#meodos
    def esta_disponible(self):
        return self._disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def devolver(self):
        self._disponible = True

