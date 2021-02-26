class vehiculos(): 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def Arrancar(self):
        self.enmarcha = True

    def Acelerar(self):
        self.acelerar = True
    
    def Frenar(self):
        self.frenar = True
    
    def estado_objeto(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
            self.enmarcha, "\nAcelerar: ", self.acelerar, "\nFrenar: ", self.frenar)

class Furgoneta(vehiculos):

    def Cargar(self, cargas):
        self.cargado = cargas
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta caragada" 

class Moto(vehiculos): #al colocarle dentro de la clase moto la clase vehiculo esta heredando todo lo que tiene la clase vehiculo 
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "estoy haciendo caballito"
    
    def estado_objeto(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
            self.enmarcha, "\nAcelerar: ", self.acelerar, "\nFrenar: ", self.frenar, "\n", self.hcaballito)
         
class VeElectricos(vehiculos):
    
    def __init__(self, marca_Velectrico, modelo_Velectrico):
        super().__init__(marca_Velectrico, modelo_Velectrico)
        self.autonomia = 100 

    def Carga_energia(self):
        self.cargando = True


miMoto = Moto("honda", "cbr")

#miMoto.caballito( )
miMoto.estado_objeto()



Furgon = Furgoneta("renault", "kangoo")
Furgon.Arrancar()
Furgon.estado_objeto()
print(Furgon.Cargar(True))
print("----------------------")

class Bicicleta_electrica(VeElectricos, vehiculos): # este es herencia multiple puedes agregar mas de una clase para otra clase
    pass                                          #cuando se usa la herencia multiple se le da mas preferencial al que este a la izquierda                                

Micicla = Bicicleta_electrica("Mw", "MW2")

Micicla.estado_objeto()
Micicla.Carga_energia()