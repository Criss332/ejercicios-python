from tkinter import*

#este funciona para abrir una ventana.
raiz=Tk()

#esta palabra title funciona para agregar un titulo.
raiz.title("Ventana de pruebas")

#este sirve para colocar una medida que no se puede cambiar cuando se ejecute  a los marcos.
# este sirve para q si quieres q solo se pueda estirar de ancho o de alto con 1 o 0, 
raiz.resizable(0,0)

raiz.iconbitmap("tepp.ico")

raiz.mainloop()