from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from repositories.reservation_repository import ReservationRepository

class RepositoryFactory:
    @staticmethod
    def create_room_repository():
        """Crea una instancia del repositorio de salas."""
        return RoomRepository()

    @staticmethod
    def create_user_repository():
        """Crea una instancia del repositorio de usuarios."""
        return UserRepository()

    @staticmethod
    def create_reservation_repository():
        """Crea una instancia del repositorio de reservas."""
        return ReservationRepository()

def main():
    room_repo = RepositoryFactory.create_room_repository()
    user_repo = RepositoryFactory.create_user_repository()
    reservation_repo = RepositoryFactory.create_reservation_repository()
    booking_service = BookingService(room_repo, user_repo, reservation_repo)