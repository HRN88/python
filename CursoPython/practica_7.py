"""Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:"""

sumador = 0
numero = int(input("Cuantos numeros quieres introducir: "))

for i in range(0, numero):
	val = int(input("Ingresa el valor: "))
	sumador += val

media = sumador/numero
print("La media es: ", media)
	