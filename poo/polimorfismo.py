class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas ")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando en 2 ruedas")
        
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando en 6 ruedas")


def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

Mivehiculo = Camion()
desplazamiento_vehiculo(Mivehiculo) #El polimorfismo se encarga de usar un solo metodo para llamar a otras clases.
