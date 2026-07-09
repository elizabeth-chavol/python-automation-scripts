#EJEMPLO 1

def saludar():
    print("Sistema iniciado. SOC activo.")

def mostrar_estado(servidor):
    print(f"Escaneando servidor: {servidor}")


#ACA USAMOS LAS FUNCIONES
saludar()
mostrar_estado("Servidor Web")
mostrar_estado("Base de Datos")
mostrar_estado("Firewall")


#EJEMPLO 2

def analizar_ataque(numero):
    if numero > 10:
        return "CRITICO"
    else:
        return "NORMAL"

#PROBAMOS LA FUNCION
resultado1 = analizar_ataque(15)
resultado2 = analizar_ataque(5)

print("Ataque 1:" , resultado1)
print("Ataque 2:" , resultado2)


#DESAFIO NIVEL SOC JR

def contar_fallidos():
    import random
    fallidos = 0
    for i in range(20):
        if random.random() < 0.6:
            fallidos = fallidos + 1
    return fallidos

total = contar_fallidos()
print("Fallidos en esta ronda:" , total)
