print("suma de dos numeros")
print("cuantas veces desea sumar? ")
cant_veves= int(input())
for i in range(cant_veves):
    suma1=int(input("ingrese primer numero "))
    suma2=int(input("ingrese segundo numero a sumar "))
    suma=suma1+suma2
    #la "f" se usa para q python reconozca q se muestre un texto q ingreses y muestre lo q estaba 
    #guardado en la varible "{suma}".
    print(f"el resultado es: {suma}")

#range(2, x, x) con esto pasa lo siguiente 2 es de donde va a comenzar a contar.
#range(x, 20, x) 20 es hasta donde va a terminar .
#range(x, x, 2) y este ultimo dos es q va a contar de dos en dos.
for i in range(2, 20, 2):
    print(i)

print("ingrese nombre ")
nombre=input()
for i in range(1):
    print(len(nombre))