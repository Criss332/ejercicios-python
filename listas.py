nombres=["juan", "carlos", "lucas" ]

#si quieres agregar un nuevo caracter o nombre. lo pudes hacer con la palabra append.
nombres.append("rosa")

#si quieres agregar el caracter o nombre en cualquier ubicacion en los vectores lo puedes hacer con 
#la palabra insert y agregando la coordenada donde lo deseas colocar.
nombres.insert(1,"jorge ")

#con este puedes agregar una lista mas despues de ["juan", "carlos", "lucas" ] y con este se usa la
#la palabra extend 
nombres.extend(["1", "2", "3" ])

#si queremos saber la ubicacion "espacio donde se guardo dcho valor o caracter" donde se encuentra algun numero o caracter lo usamos con la palabra 
#index
print(nombres.index("2"))

#con este podemos mirar si dicho carater, numero o letra estan en el vector "numeros" y se usa la
#sintaxis print("caracter o numero" in nombres ) y analizara y te dira (si esta=true) o 
#(no esta=false)
print("juan" in nombres)

#con esta podemos quitar y q no muestre en pantalla con la palabra remove.
nombres.remove("2")

#con esta funcion sirve para quitar el ultimo caracter o numero q se le agregue en un vector y es
#pop
nombres.pop()

#este es para mostrar e pantalla lo que hay en el vector.
print(nombres[:])

#puedes imprimir "si quieres " un nombre en especifico.
# por ejemplo 2 que es el lugar donde se encuentra el nombre de lucas ya que aqui el vector comienza desde 0 en adelante.
print(nombres[2])

#tambien puedes ordenar hasta donde desea q muestre.
print(nombres[:2])


