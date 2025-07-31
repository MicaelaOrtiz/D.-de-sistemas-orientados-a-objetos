from flask import Flask, render_template, request, redirect, url_for, flash
from repositories.room_repository import RoomRepository
from repositories.reservation_repository import ReservationRepository
from models.room import Room
from models.reservation import Reservation
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para usar flash messages

room_repo = RoomRepository()
reservation_repo = ReservationRepository()

# Agregamos salas de prueba
room_repo.add(Room("Sala 1", 10))
room_repo.add(Room("Sala 2", 5))

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/salas')
def mostrar_salas():
    salas = room_repo.get_all()
    return render_template("salas.html", salas=salas)

@app.route('/reservas')
def listar_reservas():
    reservas = reservation_repo.get_all()
    return render_template("reservas.html", reservas=reservas)

@app.route('/reservas/nueva', methods=['GET', 'POST'])
def nueva_reserva():
    if request.method == 'POST':
        user_name = request.form.get('user_name') or ''
        room_name = request.form.get('room_name') or ''
        start_time_str = request.form.get('start_time') or ''
        end_time_str = request.form.get('end_time') or ''

        # Validar datos básicos
        if not all([user_name.strip(), room_name.strip(), start_time_str.strip(), end_time_str.strip()]):
            flash("Todos los campos son obligatorios.")
            return redirect(url_for('nueva_reserva'))

        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M")
            if end_time <= start_time:
                flash("La hora de fin debe ser posterior a la hora de inicio.")
                return redirect(url_for('nueva_reserva'))
        except ValueError:
            flash("Formato de fecha/hora inválido.")
            return redirect(url_for('nueva_reserva'))

        # Buscar sala por nombre
        sala = next((s for s in room_repo.get_all() if s.name == room_name), None)
        if not sala:
            flash("Sala no encontrada.")
            return redirect(url_for('nueva_reserva'))

        # Crear y guardar reserva
        nueva = Reservation(user_name, sala, start_time, end_time)
        reservation_repo.add(nueva)

        flash("Reserva creada con éxito.")
        return redirect(url_for('listar_reservas'))

    # Método GET: mostrar formulario de nueva reserva
    salas = room_repo.get_all()
    return render_template("nueva_reserva.html", salas=salas)

if __name__ == "__main__":
    app.run(debug=True)
