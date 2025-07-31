from models.reservation import Reservation

class BookingService:
    def __init__(self, room_repo, user_repo, reservation_repo):
        self.room_repo = room_repo
        self.user_repo = user_repo
        self.reservation_repo = reservation_repo

    def realizar_reserva(self, nombre_usuario, nombre_sala, inicio, fin):
        usuario = self.user_repo.get_by_name(nombre_usuario)
        sala = self.room_repo.get_by_name(nombre_sala)

        if not usuario or not sala:
            raise ValueError("Usuario o sala no encontrados.")

        # Validar que no se superponga con reservas existentes
        for reserva_existente in self.reservation_repo.get_by_room(sala.id):
            if not (fin <= reserva_existente.start_time or inicio >= reserva_existente.end_time):
                raise ValueError("Conflicto de horario con otra reserva.")

        nueva_reserva = Reservation(user_id=usuario.id, room_id=sala.id, start_time=inicio, end_time=fin)
        self.reservation_repo.add(nueva_reserva)
