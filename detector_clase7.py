import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from datetime import datetime
import subprocess
import re

load_dotenv()

def guardar_log(ip, intentos):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha}] ALERTA: {intentos} intentos desde {ip}\n"

    with open("alertas.log", "a") as f:
        f.write(linea)
        print(f"Evidencia guardada: {linea.strip()}")

        try:
            subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            accion = f"[{fecha}[ ACCION: IP {ip} bloqueada\n"
            f.write(accion)
            print(f"ACCION: IP {ip} bloqueada")
        except:
            accion = f"[{fecha}] ACCION: No se pudo bloquear {ip}. Falta permiso root\n"
            f.write(accion)
            print("SIMULACION: No se pudo bloquear. Falta permiso root")

def enviar_alerta(asunto, cuerpo):
    msg = EmailMessage()
    msg.set_content(cuerpo)
    msg["Subject"] = asunto
    msg["From"] = os.getenv("EMAIL")
    msg["To"] =os.getenv("EMAIL")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        smtp.send_message(msg)
    print("Alerta enviada")

def extraer_ip(linea_log):
    match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', linea_log)
    if match:
        return match.group(1)
    return "IP_DESCONOCIDA"

try:
    with open("ataques.log", "r") as f:
        lineas = f.readlines()

    for linea in lineas:
        if "ATAQUE" in linea:
            ip_atacante = extraer_ip(linea)
            guardar_log(ip_atacante, 5)
            enviar_alerta("URGENTE: Ataque detectado", f"Se detectaron 5 intentos desde la IP: {ip_atacante}")
            break

except FileNotFoundError:
    print("No existe ataques.log")
