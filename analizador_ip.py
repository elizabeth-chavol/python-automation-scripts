print("=== ANALIZANDO LOG DE ATAQUES ===")

archivo = open("ataques.log", "r")

for linea in archivo:
    linea = linea.strip()

    if "Ronda" in linea:
        partes = linea.split("|")
        info_ronda = partes[0]
        info_ip = partes[1]

        intentos = int(info_ronda.split(":")[1].split("intentos")[0])
        ip = info_ip.split(":")[1].strip()

        if intentos > 12:
            print(f"!!! ALERTA!!! {ip} hizo {intentos} intentos. Posible fuerza bruta.")
        else:
            print(f"{ip}: {intentos} intentos. Normal.")

archivo.close()
print("=== FIN DEL ANALISIS ===")
