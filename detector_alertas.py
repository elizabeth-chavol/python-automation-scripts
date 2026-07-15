import os
import time
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from datetime import datetime

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LOG_FILE = "logs/ataques.log"

def guardar_log(ip, intentos):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea =  f"[{fecha}] ALERTA: {intentos} intentos fallidos desde IP {ip}\n"

    with open("alertas.log", "a") as f:
        f.write(linea)
    print(f"Evidencia guardada en alertas.log")

def enviar_alerta(mensaje):
    msg = EmailMessage()
    msg['Subject'] = 'ALERTA SOC - Ataque Detectado'
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content(mensaje)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    print("Correo de alerta enviado")

def vigilar():
    print("Guardia iniciando...")
    while True:
        with open(LOG_FILE, 'r') as f:
            contenido = f.read()
            if "ATAQUE" in contenido or "ERROR" in contenido:
                guardar_log("LOGSERVER", 5)
                enviar_alerta(f"Se detectó esto en el log:\n{contenido}")
        time.sleep(60) # espera 60 seg

if __name__ == "__main__":
    vigilar()
