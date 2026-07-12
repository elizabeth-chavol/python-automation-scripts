import random
import time
ataques = []
for ronda in range(1, 6):
    fallidos = 0
    for i in range(20):
        if random.random() < 0.6:
           fallidos = fallidos + 1
    ataques.append(fallidos)
    print(f"Ronda {ronda}: {fallidos} intentos fallidos")
    time.sleep(1)

print("================")
print("HISTORIAL COMPLETO:" , ataques)
print("ATAQUE MAS GRANDE:" , max(ataques))
