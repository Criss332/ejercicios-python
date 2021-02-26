class Coche():
    def __init__(self): #esto es un constructor donde se agregan como un estado inicial 
        self.__largochasis=250
        self.__anchochasis=120
        self.__ruedas=4 #para que no se pueda editar el valor establecido se le hace un encapsulamiento con: "__" 
        self.__enmarcha=False

    #self,arrancar la variable arrancar es un paramentro 

    def arrancar (self,arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__Chequeo_interno()

        if (self.__enmarcha and chequeo ):
            return "El coche esta en movimiento"
        elif (self.__enmarcha and chequeo ==False):
            return "algo a fallado en el chequeo, no podemos arrancar"
        else:
            return "El coche no esta en movimiento"
    
    def estado(self):
        print("EL coche tiene ", self.__ruedas, " ruedas, largo de ", self.__largochasis, ", ancho  ", self.__anchochasis )
    #self es como la propiedad "This"

    def __Chequeo_interno(self): #para encapsular la definiciones es igual que las variables para que sea inaccesible
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
    
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
            

miCoche=Coche() #le asignamos un nombre a la clase coche() 
print("----------- Primer objeto: --------")

print(miCoche.arrancar(False)) #es necesarios agregar un valor bool dentro del objeto arrancar para que se agregue a la bariable ,arrancamos):
miCoche.estado()

print("----------- Segundo objeto: --------")

Coche2=Coche()

print(miCoche.arrancar(True))
Coche2.__ruedas=2 # encapsulamiento no deja que cambien los valores desde fuera de la clase.
Coche2.estado() #no es necesario que se le coloque la opcion de print porque en la def estado devuelve un print
