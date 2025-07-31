from datetime import datetime
from services.booking_service import BookingService
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from repositories.reservation_repository import ReservationRepository

def parse_datetime(dt_str):
    try:
        return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return None

def crear_sala(booking_service):
    name = input("Nombre de la sala: ").strip()
    if not name:
        print("El nombre de la sala no puede estar vacío.")
        return
    while True:
        try:
            capacity = int(input("Capacidad: "))
            if capacity <= 0:
                print("La capacidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido para la capacidad.")
    room = booking_service.create_room(name, capacity)
    print(f"Sala creada con ID: {room.id}")

def crear_usuario(booking_service):
    name = input("Nombre del usuario: ").strip()
    if not name:
        print("El nombre del usuario no puede estar vacío.")
        return
    user = booking_service.create_user(name)
    print(f"Usuario creado con ID: {user.id}")

def reservar_sala(booking_service, user_repo, room_repo):
    user_id = input("ID del usuario: ").strip()
    if not user_repo.get_by_id(user_id):
        print("Usuario no encontrado.")
        return

    room_id = input("ID de la sala: ").strip()
    if not room_repo.get_by_id(room_id):
        print("Sala no encontrada.")
        return

    start_time_str = input("Hora inicio (YYYY-MM-DD HH:MM): ").strip()
    end_time_str = input("Hora fin (YYYY-MM-DD HH:MM): ").strip()

    start_time = parse_datetime(start_time_str)
    end_time = parse_datetime(end_time_str)
    if not start_time or not end_time:
        print("Formato de fecha inválido. Usa YYYY-MM-DD HH:MM.")
        return
    if end_time <= start_time:
        print("La hora de fin debe ser posterior a la hora de inicio.")
        return

    success = booking_service.book_room(user_id, room_id, start_time, end_time)
    if success:
        print("Reserva exitosa.")
    else:
        print("No se pudo reservar. Puede que la sala esté ocupada en ese horario.")

def ver_reservas_por_usuario(booking_service, user_repo):
    user_id = input("ID del usuario: ").strip()
    if not user_repo.get_by_id(user_id):
        print("Usuario no encontrado.")
        return

    bookings = booking_service.get_reservations_by_user(user_id)
    if not bookings:
        print("No hay reservas para este usuario.")
    else:
        for b in bookings:
            print(f"Reserva ID: {b.id} | Sala: {b.room.name} | Inicio: {b.start_time.strftime('%Y-%m-%d %H:%M')} | Fin: {b.end_time.strftime('%Y-%m-%d %H:%M')}")

def ver_reservas_por_sala(booking_service, room_repo):
    room_id = input("ID de la sala: ").strip()
    if not room_repo.get_by_id(room_id):
        print("Sala no encontrada.")
        return

    bookings = booking_service.get_reservations_by_room(room_id)
    if not bookings:
        print("No hay reservas para esta sala.")
    else:
        for b in bookings:
            print(f"Reserva ID: {b.id} | Usuario: {b.user.name} | Inicio: {b.start_time.strftime('%Y-%m-%d %H:%M')} | Fin: {b.end_time.strftime('%Y-%m-%d %H:%M')}")

def main():
    room_repo = RoomRepository()
    user_repo = UserRepository()
    reservation_repo = ReservationRepository()
    booking_service = BookingService(room_repo, user_repo, reservation_repo)

    try:
        while True:
            print("\nGestor de Reservas de Salas de Reunión")
            print("1. Crear sala")
            print("2. Crear usuario")
            print("3. Reservar sala")
            print("4. Ver reservas por usuario")
            print("5. Ver reservas por sala")
            print("6. Salir")

            choice = input("Selecciona una opción: ").strip()

            if choice == '1':
                crear_sala(booking_service)
            elif choice == '2':
                crear_usuario(booking_service)
            elif choice == '3':
                reservar_sala(booking_service, user_repo, room_repo)
            elif choice == '4':
                ver_reservas_por_usuario(booking_service, user_repo)
            elif choice == '5':
                ver_reservas_por_sala(booking_service, room_repo)
            elif choice == '6':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. Saliendo...")

if __name__ == "__main__":
    main()
