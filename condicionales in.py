print("asignatura a escoger son: " ), print("ingles, matematicas, software" )
opcion=input("escriba asignatura a estudiar: ")

#con la opcion "lower" pasa lo q ingresastes en opcion a minusculas.
asignaturas=opcion.lower()

#con la variable "in" se comparan.

if asignaturas in ("ingles", "matematicas", "software" ):
	print("asignatura escogida: " + asignaturas )
else:
	print("vuelva a escoger la asignatura, la que a ingresado no esta en la lista ofrecida")

