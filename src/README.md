# Gestor de Reservas de Salas de Reunión

Aplicación para gestionar salas, usuarios y reservas usando Programación Orientada a Objetos en Python.

---

## Características

- Crear salas de reunión con capacidad.  
- Crear usuarios.  
- Reservar salas por rangos horarios.  
- Consultar reservas por usuario o sala.  
- Validación de conflictos de horarios.

## Requisitos

- Python 3.10 o superior  
- Docker (opcional)  
- Git  

## Ejecución sin Docker

1. Clonar el repositorio:

   git clone https://github.com/tuusuario/meeting-room-booking.git
   cd meeting-room-booking

# 2. Crear y activar un entorno virtual (opcional):
 En Linux/macOS: 
  python3 -m venv venv 
  source venv/bin/activate
 En Windows (PowerShell):
  python -m venv venv 
  .\venv\Scripts\activate

# 3. Instalar dependencias:  
 pip install -r requirements.txt 

# 4. Ejecutar la aplicación de consola: 
 python main.py

## Ejecución con Docker
1. Construir la imagen Docker:
 docker build -t meeting-room-booking .
2. Ejecutar el contenedor:
 docker run -it --rm -p 5000:5000 meeting-room-booking
3. Acceder a la aplicación web: 
 Abrí en tu navegador: 
  http://localhost:5000

## Modos de uso
Este proyecto ofrece dos formas principales de interactuar con el sistema de reservas:

# 1. Interfaz Web (con Flask)
La aplicación web está implementada en web.py usando Flask.
Se puede ejecutar localmente con:
flask run o python -m flask run

- En el contenedor Docker, la imagen ya está configurada para iniciar esta aplicación automáticamente.
- El servidor web escucha en el puerto 5000, accesible desde el navegador.

## Rutas disponibles:
— Página principal
/salas — Listado de salas disponibles
/reservas — Listado de reservas
/reservas/nueva — Formulario para crear reservas

# 2. Interfaz de Consola
- Para gestionar salas, usuarios y reservas desde la consola, está la aplicación main.py.
- Para usarla, ejecutá directamente:
python main.py

- El contenedor Docker está configurado para levantar la app web con Flask (las rutas y formularios mencionados arriba).
- Si querés usar la consola (main.py), debés ejecutarla localmente en Python.