

def perfecto(n):
    suma=0
    for i in range(1,n):
        if n % i ==0:
            suma = suma+i
        else:
            suma = suma
    return suma

n=int(input("Ingrese un numero:  "))

while n>=0:
    if n>2:
        if perfecto(n)== n:
            print("El numero es perfecto")
        else:
            print("El numero NO es perfecto")
    else:
        print("El numero debe ser mayor que 2")

    n = int(input("Ingrese otro numero: "))
    
print("Programa finalizado")



