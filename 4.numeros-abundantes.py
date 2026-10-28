

def numabund(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma = suma + i
    return suma


rangoini = int(input("Numero inicial: "))
rangofinal = int(input("Numero final: "))

lista = ""

for num in range(rangoini, rangofinal + 1):
    if numabund(num) > num:
        if lista != "":
            lista = lista + ", "
        lista = lista + str(num)

print("Los numeros abundantes entre", rangoini, "y", rangofinal, "son:", lista)
