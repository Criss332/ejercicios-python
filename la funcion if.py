print("programas de evaluacion de notas de alumnos")

nota_alumno=input()

def evaluaion(nota):
 	valoracion="aprobado"
 	if nota<5:
 		valoracion="gano"
 	return valoracion

print(evaluaion(int(nota_alumno)))