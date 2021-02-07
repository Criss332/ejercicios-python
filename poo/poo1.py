class Coche():
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False


    def arrancar (self,):
        self.enmarcha=True
    
    def estado(self,):
        if (self.arrancar):
            return "el coche esta en movimiento"
        else:
            return "el coche no esta en movimiento" 
        

miCoche=Coche()

print("el largo del chasis es de", miCoche.largochasis)
print("tiene", miCoche.ruedas, "ruedas")
miCoche.arrancar()

print(miCoche.estado())