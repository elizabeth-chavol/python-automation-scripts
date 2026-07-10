print("=== ANALIZANDO LOG DE ATAQUES ===")

archivo = open("ataques.log" , "r")

for linea in archivo:
    linea = linea.strip()

    if "Ronda" in linea:
        partes = linea.split(":")
        ronda = partes[0]
        intentos = int(partes[1])

        if intentos > 12:
            print(f"!!! ALERTA!!! {ronda} tuvo {intentos} intentos. Posible fuerza bruta.")
        else:
            print(f"{ronda}: {intentos} intentos. Normal")

archivo.close()
print("=== FIN DEL ANALISIS ===")

