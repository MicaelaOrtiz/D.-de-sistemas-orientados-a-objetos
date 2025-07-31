FROM python:3.11-slim

WORKDIR /app

COPY src/ ./src
COPY web.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Puerto 5000 para Flask
EXPOSE 5000

# Entorno para que Flask sepa dónde está la app
ENV FLASK_APP=web.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para ejecutar la app Flask
CMD ["flask", "run"]
