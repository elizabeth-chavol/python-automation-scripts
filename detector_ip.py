import random
print("=== SIMULADOR DE ATAQUES CON IP ===")

archivo = open("ataques.log" , "w")

def contar_fallidos():
    return random.randint(10, 15)

for ronda in range(1, 6):
    intentos = contar_fallidos()
    # Generamos una IP falsa para simular
    ip = f"192.168.1.{random.randint(50, 60)}"

    linea = f"Ronda {ronda}: {intentos} intentos | IP: {ip}\n"
    archivo.write(linea)
    print(f"Guardado: {linea.strip()}")

archivo.close()
print("=== LOG GENERADO ===")


