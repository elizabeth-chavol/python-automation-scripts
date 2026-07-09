import random
import time

def contar_fallidos():
    fallidos = 0
    for i in range(20):
        if random.random() < 0.6:
            fallidos = fallidos + 1
    return fallidos

#ABRIMOS ARCHIVO PARA GUARDAR

archivo = open("ataques.log", "w")

for ronda in range(1, 6):
    resultado = contar_fallidos()
    print(f"Ronda {ronda}: {resultado} intentos")

    #GUARDAMOS EN EL ARCHIVO
    archivo.write(f"Ronda {ronda}: {resultado}\n")
    time.sleep(1)

archivo.close() #CERRAMOS EL ARCHIVO
print("Log guardado en ataques.log")
