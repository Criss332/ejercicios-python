print("ingrese nombre ")
nombre=input()
print("ingrese cantidad de veces que desee repetir")
cant_veces=int(input())

#con la palabra "range()" cuenta la cantidad de numeros e imprime el valor.
for i in range(cant_veces):
	print(nombre)


#con la palabra "end=""" se usa para q imprima lo ingresado sin saltar linea.
#usando la "cant_veces=10 carcateres" con comillas muestra en pantalla la cantidad de caracteres.
for i in range(cant_veces):
	print(nombre, end=" ")

