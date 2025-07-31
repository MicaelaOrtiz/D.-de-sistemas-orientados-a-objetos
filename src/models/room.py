import uuid

class Room:
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValueError("La capacidad debe ser un número positivo.")
        
        self.id = str(uuid.uuid4())
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"Sala {self.name} (Capacidad: {self.capacity}, ID: {self.id})"
