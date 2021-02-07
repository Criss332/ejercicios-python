nombres={"cristian": "acosta ", "eduard":"acosta", "emily": "acosta"}

#con este podemos agregar un nuevo caracter a la lista "nombres".
nombres["yuliana"]="acosta navarro"

#con este puedes hacer q al ingresar la palabra "eduard" imprima o muestre en pantalla "acosta".
print(nombres["eduard"])

#con este "del" podemos borrar algun caracter q este en la bariable nombres.
del nombres["cristian"]

#con este se puede hacer q muestre solo los nombres o las las claves con la palabra "keys".
print(nombres.keys())

#con este es lo inverso a keys en este no muestra las claves si no los q van al lado delas claves
#y la palabra q se usa es values.
print(nombres.values())

#con esta se puede saber cuantos valores hay en el vector nombres y la palabra es len.
print(len(nombres))
 
print(nombres)

