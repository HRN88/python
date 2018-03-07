#Tipos de variables en python, es un lenguaje no tipado, es decir no se indica el tipo de dato a la variable.
#Por otra parte es un lenguaje dinamicamente tipado

#Se puede alternar entre el tipo de dato para la misma variable
numero = 3
print(numero)

numero = "Tres"
print(numero)

#Se pueden sumar numeros representados como texto al convertirlos a entero
numero1 = "50"
numero2 = "20"
#aqui se suman, pero al ser texto se muestra una concatenacion
print(numero1 + numero2)

#Para convertir a entero se hace un casteo (casting)

numero1 = int(numero1)
numero2 = int(numero2)

#Aqui ya realiza la suma como numeros
print(numero1 + numero2)

#De igual manera se puede hacer casting para float, string, ejemplo

print(float(numero1))
print(str(numero1) + " " + numero)




