email=False
correo=input("ingrese correo ")
for i in correo :
#al ingresar    if(i=="@"): lo que hace es verificar si existe dicho caracter en "cristian33244@gmail.com".
      
    if(i=="@"):
        email=True

if email==True:
    print("el email es correcto")
else:
    print("el email es incorrecto")
