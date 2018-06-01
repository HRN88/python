'''Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene 
una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):'''


cadena = input("Ingresa una cadena: ")

print('Si una cadena de texto introducida por el usuario \ntiene una longitud mayor o igual que 3 y a su vez es menor que 10 ')

print(len(cadena) >= 3 and len(cadena) < 10)