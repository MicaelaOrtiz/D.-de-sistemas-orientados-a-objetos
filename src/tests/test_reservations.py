import unittest
from datetime import datetime
from services.booking_service import BookingService
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from repositories.reservation_repository import ReservationRepository
from models.user import User
from models.room import Room

class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.room_repo = RoomRepository()
        self.user_repo = UserRepository()
        self.reservation_repo = ReservationRepository()
        self.booking_service = BookingService(self.room_repo, self.user_repo, self.reservation_repo)

        self.room_repo.add(Room("Sala 1", 6))
        self.user_repo.add(User("Ana"))

    def test_successful_reservation(self):
        inicio = datetime(2025, 7, 23, 10, 0)
        fin = datetime(2025, 7, 23, 11, 0)
        self.booking_service.realizar_reserva("Ana", "Sala 1", inicio, fin)

        reservas = self.reservation_repo.get_by_user(self.user_repo.get_by_name("Ana").id)
        self.assertEqual(len(reservas), 1)

    def test_conflict_reservation(self):
        inicio_1 = datetime(2025, 7, 23, 10, 0)
        fin_1 = datetime(2025, 7, 23, 11, 0)
        inicio_2 = datetime(2025, 7, 23, 10, 30)
        fin_2 = datetime(2025, 7, 23, 11, 30)

        self.booking_service.realizar_reserva("Ana", "Sala 1", inicio_1, fin_1)

        with self.assertRaises(ValueError) as context:
            self.booking_service.realizar_reserva("Ana", "Sala 1", inicio_2, fin_2)
        
        self.assertIn("Conflicto de horario", str(context.exception))

if __name__ == '__main__':
    unittest.main()
