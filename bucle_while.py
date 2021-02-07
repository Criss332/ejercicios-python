i=1
cant=int(input("ingrese cuantas veces quiere q muestre en pantalla "))
while i<=cant:
    print("el resultado es: " + str(i))
    i=i+1

print("fin")

edad=int(input("ingrese edad "))
while edad<0 or edad>100:
    print("edad incorrecta")
    edad=int(input("ingrese edad "))
