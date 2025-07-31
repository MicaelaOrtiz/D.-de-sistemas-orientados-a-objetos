import uuid
from datetime import datetime

class Reservation:
    def __init__(self, user_id: str, room_id: str, start_time: datetime, end_time: datetime):
        if start_time >= end_time:
            raise ValueError("La hora de inicio debe ser anterior a la hora de fin.")
        
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Reserva ID: {self.id}, Sala: {self.room_id}, Usuario: {self.user_id}, " \
               f"De: {self.start_time} a {self.end_time}"
