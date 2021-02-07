#bucle CONTINUE
nombre=input("ingrese nombre ")
quitar=input("ingrese letra que desea quitar en el nombre ingresado ")
for letra in nombre :
    if letra==quitar:
        #esto hace q se salte la letra ingresada anteriormente.
        continue
    print(letra )

#bucle ELSE
email=input("ingrese su email ")
for i in email:
    if i=="@":
        arroba=True
        break;

else:
    arroba=False

print(arroba)