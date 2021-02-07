print("becas 2020")

cantidad_recorrida=int(input("ingrese cantidad de km que recorre hasta la unveridad "))
print(cantidad_recorrida)

cant_hermanos=int(input("ingrese numero de hermanos "))
print(cant_hermanos)

salario=int(input("ingrese salario de su hogar "))
print(salario)

# con este para comparar barios se usa el metodo "and" q es "y".
if cantidad_recorrida>7 and cant_hermanos>=3 and salario<=800000:
	print("usted a cumplido los requisitos exigidos")
else:
	print("usted no a cumplido los requisitos exigidos")

print("........")

# con este se usa si una no cumple, con el "or" q es "o" es diferente del "and"
if cantidad_recorrida>7 and cant_hermanos>=3 or salario<=800000:
	print("usted a cumplido los requisitos exigidos")
else:
	print("usted no a cumplido los requisitos exigidos")