import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
from dotenv import load_dotenv
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

# Cargar variables del archivo .env
load_dotenv()

print("=== ENVIADOR AUTOMATICO DE REPORTES SOC ===")

#CONFIGURACION 
EMAIL_REMITENTE = "elizabeth.chavol.infosec@gmail.com"
EMAIL_DESTINO = "elizabeth.chavol.infosec@gmail.com"
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
ARCHIVO_REPORTE = os.path.join(RUTA_BASE,f"reporte_{fecha_hoy}.txt")
ASUNTO = f"REPORTE SOC - {fecha_hoy}"

def enviar_reporte():
    try:
        with open(ARCHIVO_REPORTE, 'r', encoding='utf-8') as f:
            cuerpo = f.read()
    except FileNotFoundError:
        print("ERROR: No se encontro {ARCHIVO_REPORTE}")
        return

    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL_REMITENTE
    mensaje['To'] = EMAIL_DESTINO
    mensaje['Subject'] = ASUNTO
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_REMITENTE, PASSWORD)
        server.sendmail(EMAIL_REMITENTE, EMAIL_DESTINO, mensaje.as_string())
        server.quit()
        print("=== REPORTE ENVIADO CON EXITO ===")
    except Exception as e:
        print(f"Error al enviar: {e}")

if __name__ == "__main__":
    enviar_reporte()

