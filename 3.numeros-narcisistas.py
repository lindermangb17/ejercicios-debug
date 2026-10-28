

def narcisista(n):
    digitos = str(n)
    potencia = 0
    suma = 0
    operacion = ""

    for i in digitos:
        potencia = potencia + 1

    for i in digitos:
        numero = int(i)
        suma = suma + numero ** potencia

        if operacion != "":
            operacion = operacion + " + "

        operacion = operacion + i + "^" + str(potencia)

    return suma, operacion


n = int(input("Ingrese un numero: "))

while n > 0:
    suma, operacion = narcisista(n)

    print(operacion, "=", suma)

    if suma == n:
        print("El numero es narcisista")
    else:
        print("El numero NO es narcisista")

    n = int(input("Ingrese otro numero: "))

print("Programa finalizado")
