import datetime 
import random
fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")

print("=== ANALIZADOR + REPORTE AUTOMATICO ===")

# 1. Primero generamos log nuevo para esta clase
with open(f"ataques_{fecha_hoy}.log", "w") as log:
    for ronda in range(1, 6):
        intentos = random.randint(8, 16)
        ip = f"10.0.0.{random.randint(100, 110)}"
        log.write(f"Ronda {ronda}: {intentos} intentos | IP: {ip}\n")

# 2. Ahora lo leemos y generamos reporte
lineas_reporte = []
lineas_reporte.append("=== REPORTE DE SEGURIDAD SOC ===\n")
lineas_reporte.append(f"Fecha: {datetime.datetime.now()}\n")
lineas_reporte.append("Analista: Elizabeth\n")

with open(f"ataques_{fecha_hoy}.log", "r") as log_lectura:
    for linea in log_lectura:
        linea = linea.strip()
        if "Ronda" in linea:
            partes = linea.split("|")
            info_ronda = partes[0]
            info_ip = partes[1]
            intentos = int(info_ronda.split(":")[1].split("intentos")[0])
            ip = info_ip.split(":")[1].strip()

        if intentos > 12:
            alerta = f"[ALERTA CRITICA] IP {ip} - {intentos} intentos - FUERZA BRUTA\n"
            print("!!! " + alerta.strip())
            lineas_reporte.append(alerta)
        else:
            normal = f"[OK] IP {ip} - {intentos} intentos\n"
            print(normal.strip())
            lineas_reporte.append(normal)

#Guardar todo de una
from datetime import datetime
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

with open(f"reporte_{fecha_hoy}.txt", "w") as reporte:
    reporte.writelines(lineas_reporte)

print(f"\n=== REPORTE GUARDADO EN reporte_{fecha_hoy}.txt ===")
