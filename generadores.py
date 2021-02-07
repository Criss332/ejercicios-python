def generapares(limite):
    num=1
    
    while num<limite:
        yield num*nume
        num+=1

nume=int(input("ingrese numero que quiere que inicie el contador "))
limite=int(input("ingrese numero "))
devuelve=generapares(limite)
print(next(devuelve)) 
print("aqui podria ir mas codigo..")
print(next(devuelve))
print("aqui podria ir mas codigo..")
print(next(devuelve))

print("....")
for i in devuelve:
    print(i)
