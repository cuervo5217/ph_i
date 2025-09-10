# 10/09/2025 clase de 2 a 4 programacion aplicada

#################LISTAS####################
###########################################

# Crean una lista con varios colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Imprime la lista completa
print(my_lista)

# Ver el tipo de la variable (en este caso una lista)
print(type(my_lista))

# Acceder al tercer elemento de la lista (índice 2)
print(my_lista[2])

# Obtener la longitud de la lista (cuántos elementos tiene)
print("my_lista size: ", len(my_lista))

# Obtener un subrango de la lista (elementos desde el índice 0 hasta el 2, excluyendo el 2)
print(my_lista[0:2])

# Otra forma de acceder a un subrango, en este caso los primeros 2 elementos
print(my_lista[:2])

# Agregar un elemento al final de la lista
my_lista.append('Blanco')     
print(my_lista)

# Insertar un nuevo elemento en una posición específica de la lista (índice 3)
my_lista.insert(3, 'Negro')
print(my_lista)

# Concatenar dos listas. Se agregan 'Marron' y 'Gris' al final de 'my_lista'
my_lista.extend(['Marron', 'Gris'])  
print(my_lista)

# Encontrar el índice de un elemento en la lista
print(my_lista.index('Negro'))

# Eliminar el primer elemento que coincida con el valor 'Marron'
my_lista.remove('Marron')
print(my_lista)

# Insertar 'Marron' de nuevo en la posición 8
my_lista.insert(8, 'Marron')
print(my_lista)

# Eliminar y devolver el último elemento de la lista. 
# Si no se pasa índice, .pop() elimina el último elemento por defecto.
print(my_lista.pop())

# Obtener el tamaño de la lista
size = len(my_lista)
print("size = ", size)

# Multiplicar la lista por 3. Esto genera una nueva lista con los mismos elementos repetidos 3 veces
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

# Ordenar la lista (esto afecta la lista original)
print("Sort:")
print()

# .sort() ordena la lista en su lugar (es decir, modifica la lista original). No retorna ningún valor.
my_listaSort = my_lista.sort()
my_listaSort = my_lista
print(my_listaSort)
print()

# Lista de números desordenada
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]

# Ordenar la lista de números en orden ascendente
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)

# Ordenar la lista de números de mayor a menor
my_NumList.sort(reverse=True)
print("De mayor a menor: ", my_NumList)

#################TUPLAS####################
###########################################

# Las tuplas son estructuras similares a las listas, pero son inmutables (no se pueden modificar una vez creadas)

# Convertir una lista a tupla. La función tuple() toma una lista y la convierte en una tupla
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print("my_tuple: ", my_tupla)

# Acceder al primer y tercer elemento de la tupla
print(my_tupla[0])
print(my_tupla[2])

# Evaluar si un elemento está contenido en la tupla (devuelve True o False)
print('Rojo' in my_tupla)

# Contar cuántas veces aparece un elemento en la tupla
print(my_tupla.count('Rojo'))

# Tupla con un solo elemento. Esto es importante porque si solo hay un elemento, 
# necesitas una coma después del valor para que Python lo reconozca como tupla
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)  # Esto no es una tupla aún, sería solo una variable

# Si pones una coma, ahora sí es una tupla de un solo valor
my_tupla_unitaria = ('Blanco',)
print(my_tupla_unitaria)  # Ahora es una tupla de un solo valor

# Empaquetado de tupla: Crear una tupla sin necesidad de paréntesis explícitos
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado de tupla: Asignar los valores de la tupla a varias variables en orden
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

# Imprimir los valores desempacados
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertir una tupla en una lista usando la función list()
my_lista2 = list(my_tupla)
print(my_lista2)

"""
resumen comandos

.append(): Añade un elemento al final de la lista.

.insert(): Inserta un elemento en una posición específica.

.extend(): Añade varios elementos al final de la lista.

.remove(): Elimina el primer elemento con el valor especificado.

.pop(): Elimina el último elemento de la lista o el índice proporcionado.

.sort(): Ordena la lista (modifica la lista original).

.count(): Cuenta cuántas veces aparece un elemento en la lista o tupla.

.index(): Devuelve el índice del primer elemento encontrado.

.tuple(): Convierte una lista en tupla.

.list(): Convierte una tupla en lista.
"""
