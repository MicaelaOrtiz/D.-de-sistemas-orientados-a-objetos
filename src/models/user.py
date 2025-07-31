import uuid

class User:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        
        self.id = str(uuid.uuid4())
        self.name = name

    def __str__(self):
        return f"Usuario {self.name} (ID: {self.id})"

def main():
    user = User("Juan Perez")
    print(user)
