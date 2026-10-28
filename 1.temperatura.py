
def temp(temperatura):
   
    if temperatura>34:
        print("T. alta")
    elif temperatura<26:
        print("T. baja")
    else:
        print("T. Normal")

temperatura=int(input("Ingrese la temperatura en grados celsius: "))
temp(temperatura)



