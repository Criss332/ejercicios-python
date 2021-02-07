def sumar(n1, n2):
    return n1+n2

def restar(n1, n2):
    return n1-n2

def multiplicar(n1, n2):
    return n1*n2

def dividir(n1, n2):
    # try es intentar, q quiere decir q intente hacer la operacion  return n1/n2 y si no lo logra.
    try:
        return n1/n2

    #si no logra hacer la operacion q muestre except, ZeroDivisionError es el tipo de error q muestra
    # cuando se divide un numero entre zero
    except ZeroDivisionError:
        print("no se puede dividir entre 0 ")
        return "error de sintaxys"

    return n1/n2

n1=int(input("ingrese primer numero "))
n2=int(input("ingrese segundo numero "))
operacion_n=input("ingrese operacion a escoger (sumar, restar, multiplicar, dividir) ")

if operacion_n=="sumar":
    print(sumar(n1, n2))

elif operacion_n=="restar":
    print(restar(n1, n2))

elif operacion_n=="multiplicar":
    print(multiplicar(n1, n2))

elif operacion_n=="dividir":
    print(dividir(n1, n2))

else:
    print("operacion ingresada no esta en la listaass ")