A = "si"

while (A == "si"): 


    Nombre = input("Ingrese nombre del Alumno")
    Nota1 = int(input("Ingrese nota 50% "))
    Nota2 = int(input("Ingrese nota 20%"))
    Nota3 = int(input("Ingresa nota 30%"))

    Result_N1 = (50 * Nota1) / 100
    Result_N2 = (20 * Nota2) / 100
    Result_N3 = (30 * Nota3) / 100
        
    Resultado = int(Result_N1 + Result_N2 + Result_N3)
    
    if Resultado > 10.0 :  
        print("error: Vuelva a intentarlo ")
        A = "si"
    else:
        print("La nota final del alumno :", Nombre, " es de ", Resultado)   
        A = input("¿Desea continuar ? SI o NO ")

    

    
    

