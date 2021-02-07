
print("verificando acceso")

edad=(int(input("ingrese su edad por favor")))

if edad<18:
	print("usted es menor de edad. ")
	print("por lo tanto no puede ingresar")
elif edad>100:
	print("su edad es incorrecta")
else:
	print("usted es mayor de edad.")
	print(" puede ingresar")

#este se puede hacer q imprima el nombre y el valor asignado usando la palabra "str"
nombre_alumno=int(input("ingrese edad del alumno"))
print("edad del alumno " + str(nombre_alumno))
