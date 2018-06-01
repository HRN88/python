"""5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:"""

numeros = [1, 3, 6, 9]



while True:
	numero = int(input("Ingresa un valor entero entre 0 y 9: "))
	if numero >= 0 and numero <= 9:
		if numero in numeros:
			print("El numero existe en la lista: ")
		else:
			print("Numero inexistente")
	else:
		continue
			
	