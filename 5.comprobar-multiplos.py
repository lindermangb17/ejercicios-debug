
def multiplo(numero, divisor):
    if divisor == 0:
        return False
    if numero % divisor == 0:
        return True
    else:
        return False


a = int(input("primer numero: "))
b = int(input("segundo numero: "))

if multiplo(a, b):
    print(a, "multiplo de", b, ": verdadero")
else:
    print(a, "multiplo de", b, ": falso")

if multiplo(b, a):
    print(b, "multiplo de", a, ": verdadero")
else:
    print(b, "multiplo de", a, ": falso")
