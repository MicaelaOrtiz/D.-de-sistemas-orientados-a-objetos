from models.reservation import Reservation

class ReservationRepository:
    def __init__(self):
        self.reservations = []

    def add(self, reservation: Reservation):
        self.reservations.append(reservation)

    def get_by_user(self, user_id: str):
        return [r for r in self.reservations if r.user_id == user_id]

    def get_by_room(self, room_id: str):
        return [r for r in self.reservations if r.room_id == room_id]
  
    def get_by_id(self, reservation_id: str):
        for r in self.reservations:
            if r.id == reservation_id:
                return r
        return None

    def get_all(self):
        return self.reservations
