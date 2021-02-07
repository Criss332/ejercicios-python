from tkinter import*
                        #RAIZ=ES LA VENTANA
#este funciona para abrir una ventana.
raiz=Tk()
#esta palabra title funciona para agregar un titulo.
raiz.title("Ventana de pruebas")
raiz.config(cursor="mouse")
#este sirve para colocar una medida que no se puede cambiar cuando se ejecute  a los marcos.
# este sirve para q si quieres q solo se pueda estirar de ancho o de alto con 1 o 0, raiz.resizable(TRUE,TRUE)
#con este sirve para agregar una imagen ico.
raiz.iconbitmap()
#con este le agregamos la altura y el ancho de los marcos. esto es odsional
    #raiz.geometry("650x350")
# con esto puedes agregar un color.
raiz.config(bg="gray")


                    #FRAME= MARCO DE LA VENTANA

#este es el segundo cuadro q esta dentro de la raiz.
miframe=Frame()
#esta es para activar el frame dentro de la raiz.
miframe.pack(side="top")
miframe.config(bg="blue")
#esta es para asignarle un tamaño al frame.
miframe.config(width="550", height="300")
#esta es para agregrar un borde
miframe.config(bd=15)
miframe.config(relief="groove")
#con este puedes cambiar el cursor de forma diferente.
miframe.config(cursor="pirate")


                    #LABEL= ETIQUETA

#bg="red" es el color de fondo que quieras agregar.
#fg="white" con este es el color de letra q le quieras agregar.
#font=("Clarendon", 18) con esto agregamos un tipo de letra y el tamaño que quieres.
#PhotoImage(file="") con esto puedes agregar una imagen.
milabel= Label(miframe, text="hola mucho gusto", bg="red", fg="white", font=("Clarendon", 18))
#con este se ingresa la posicion donde quieres ver el texto.
milabel.place(x=1, y=1)
milabel.config(cursor="hand2")

                    #ENTRY= ENTRADA 

entexto=Entry(miframe)
entexto.grid(row=1, colum=40)
enlabel= Label(miframe, text="nombre:")
enlabel.grid(row=1, colum=40)

raiz.mainloop()