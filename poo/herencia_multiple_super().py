#la clase super se encarga de llamar el metodo de la clase padre.
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    
    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # con esto agregamos los valores de la herencia padre

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion() #con la variable super() sirve tambien para agregar cualquier metodo de la clase padre
        print("salario: ", self.salario, "Tiempo laboral (mes):", self.antiguedad)

Juan = Empleado(900000, 12, "Juan", 27, "colombia")

Juan.descripcion()

print(isinstance(Juan, Empleado)) #isinstance sirve para saber que objeto juan es de la clase empleado o visebersa