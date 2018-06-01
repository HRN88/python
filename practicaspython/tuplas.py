#Las tuplas son un tipo de dato secuencial, sirven para agrupar, como si fueran un unico valor, varios valores.
#Es inmutable, es decir. una tupla no puede ser modificada una vez creada.
#Se pueden anidar tuplas, es decir, tener tuplas cuyo argumento sea otra tupla.
#se deben especificar sus elementos durante su creacion

#En Python las tuplas se definen entre parentesis

fecha_nac = (8, "abril", 1991)
mitupla_persona = ("Gustavo", "26", fecha_nac)

#Imprimir las tuplas
print(fecha_nac)
print(mitupla_persona)

#Para crear una tupla con un unico elemento se debe poner una coma

tuplaone = ("only",)

#Accediendo a los elementos de las tuplas se usa []

print(mitupla_persona[0])
print(tuplaone)
print(len(mitupla_persona))
