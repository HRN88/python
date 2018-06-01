"""Realiza un programa que lea un número impar por teclado. Si el usuario no 
introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente."""


while True:
	numero = int(input("Introduce un numero impar: "))
	esimpar = numero % 2
	if esimpar != 1:
		continue
	else:
		break
	
	