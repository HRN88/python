#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
'''
Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero'''


num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

print('Si los dos números son iguales', num1 == num2)
print('Si los dos números son diferentes', num1 != num2)
print('Si el primero es mayor que el segundo', num1 > num2)
print('Si el segundo es mayor o igual que el primero', num1 <= num2)
