#Listas son estructuras de datos para guardar diferentes tipos de datos


# #Definicion de listas de diferentes tipos
# lista1 = ["est","es", "una", "lista", "de", "strings"]
# lista2 = [1, 2, 3]
# lista3 = ["Mito", "Code", 2]
# lista4 = [];
# lista5 = list();
#
# #Para imprimir elementos de una lista (recorriendo uno por uno)
# #observar la diferencia con C++ al usar in
# for x in lista1:
# 	print(x)
#
# #Para agregar elementos a una lista se usa el metodo append()
#
# lista1.append(", esto se agrego con append()")
#
# #observar que esto imprime toda la lista en una linea
# print(lista1)
#
# #las listas tambien pueden tener otras listas
#
# lista1.append(["lista", "anexada"])
# print(lista1)
#
# #el metodo extend sirve tambien para agregar elementos a una lista, pero a diferencia de append estos se agregan
# #de uno en uno
# lista1.extend(["lista", "anexada"])
# print(lista1)
#
# #de esta forma se imprime el ultimo elemento de la lista, -2 el penultimo y asi sucesivamente
# print(lista1[-1])
#
# #De esta forma se altera un elemento de la lista
# lista1[0] = "alteracion"
# print(lista1)
# #o varios elementos
# lista1[0:2] = ["Peru", "Mexico"]
# print(lista1)
#
# #para imprimir en reversa delemento por elemento se usa el metodo reversed()
#
# for x in reversed(lista1):
# 	print(x)
#
# #imprimir en reversa en forma de lista
# print(list(reversed(lista1)))
#
# #Con el metodo split se puede convertir un texto a una lista, usando un comodin para separar, en este caso
# #yo uso el espacio en blanco " "
# texto = "Esto es un texto que partire con split de texto split que esta split"
# lista1 = texto.split(" ")
# print(lista1)
#
# #para eliminar elementos de la lista se usa el metodo remove,  solo se elimina la primera coincidencia
# #de la lista
#
# lista1.remove("split")
# print(lista1)
#
# #para eliminar la palabra repetida en toda la lista se usa lo siguiente
#
# lista1= [x for x in lista1 if x != "split"]
# print(lista1)




