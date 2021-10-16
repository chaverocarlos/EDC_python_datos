# Las listas en Python son variables que almacenan arreglos,
# pueden almacenar datos de distintos tipos, pueden almacenar
# otras listas, los datos de las listas son mutables, pueden modificarse
estudiantes = ["Carlos", "Elizabeth", "Abigail", 1001, 1002]
print(estudiantes)
print(estudiantes[2])
print(estudiantes[0:2])
print(estudiantes[-1])
print(len(estudiantes))
estudiantes[3] = "Hector"
print(estudiantes)

# Métodos con listas
# Agregar un elemento al final de la lista: append()
estudiantes.append("Viridiana")
print(estudiantes)
#Concatenación de Listas
estudiantes = estudiantes + ["Abraham"]
print(estudiantes)
estudiantes = ["Daniela"] + estudiantes
print(estudiantes)
#insert(1, x) i el indice, x el elemento
estudiantes.insert(5, "Frida")
print(estudiantes)
estudiantes.append("Daniela")
print(estudiantes)
# Método count() cuanta la cantidad de veces que aparece un elemento en la lista
print(estudiantes.count("Daniela"))
print(estudiantes.count(1002))
#index() devuelve el indice de un elemento en lista
print(estudiantes.index("Abraham"))
print(estudiantes.index("Daniela"))
#print(estudiantes.index("Pedro"))
#pop(), devuelce un elemento de lista, y lo borra de la misma
print(estudiantes.pop(6))
print(estudiantes)
print(estudiantes.pop())
print(estudiantes)
estudiantes.append("Daniela")
print(estudiantes)
# sort(), ordena los elementos de lista en forma ascendente
estudiantes.sort()
print(estudiantes)
# Orden descendente
estudiantes.sort(reverse=True)
print(estudiantes)

colores = "azul rojo amarillo"
print(colores)
lista_colores = colores.split()
print(lista_colores)

equipos = "Chicago Bulls, Golden State, Raptors"
lista_equipos = equipos.split(", ")
print(lista_equipos)

universidades = "UNAM;IPN;UAM;LaSalle"
lista_universidades = universidades.split(";")
print(lista_universidades)
