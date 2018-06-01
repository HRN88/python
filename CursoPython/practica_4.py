"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""


numero1 = input("Ingrese un numero: ")
numero2 = input ("Ingrese otro numero: ")
numero1 = int(numero1)
numero2= int(numero2)

opcion = input("Que quieres hacer: ")

if opcion == '1':
	print("La suma de los numeros es: ", numero1 + numero2)

elif opcion == '2':
	print("La resta de los numeros es: ", numero1 - numero2)
	
elif opcion == '3':
	print("El producto de los numeros es: ", numero1 * numero2)

else:
	print("Opción no válida, el programa informará de que no es correcta...")
