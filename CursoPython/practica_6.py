"""Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100"""

sumador = 0
for i in range(0, 100):
	if (i % 2) == 0:
		sumador += i 
print("La suma de los pares entre el 0 y el 100 es: ", sumador)

