# ==============================
# Diccionarios en Python
# ==============================

# Creamos dos listas: nombres de canciones y número de veces reproducidas
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# zip(songs, playcounts) combina ambas listas en pares (canción, reproducciones)
# dict comprehension {clave: valor for clave, valor in zip(...)}
# genera un diccionario a partir de esos pares
plays = {key:value for key, value in zip(songs, playcounts)}
# Mostramos el diccionario plays creado
print("diccionario inicial de plays:"plays)
# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44,
#  'What's Going On': 21, 'Respect': 89, 'Good Vibrations': 5}

# ======================================
# Agregar elementos a un diccionario
# ======================================

# El método .update() permite agregar un nuevo par clave:valor
plays.update({"Purple Haze": 1})
# Ahora el diccionario plays tiene una nueva canción con 1 reproducción
# {'Purple Haze': 1} fue agregado
# plays ahora tiene 7 canciones

# ======================================
# Modificar valores existentes
# ======================================

# Si usamos update() con una clave que ya existe, se sobrescribe su valor
plays.update({"Respect": 94})

# Antes 'Respect': 89
# Después 'Respect': 94
print("Despues de agregar y modificar: ", plays)
# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44,
#  'What's Going On': 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}

# ======================================
# Diccionarios anidados
# ======================================

# Podemos guardar un diccionario dentro de otro
library = {"The Best Songs": plays, # Diccionario con todas las canciones y sus reproducciones
           "Sunday Feelings": {}}   # Diccionario vacío (puede llenarse más adelante)
print("Diccionario anidado (library):"library)

# ==============================
# Resumen de métodos usados
# ==============================
# 1. zip(lista1, lista2) -> une elementos en pares.
# 2. {k:v for k,v in zip(...)} -> dict comprehension para crear diccionarios.
# 3. dict.update({clave: valor}) -> agrega o modifica pares clave:valor.
# 4. Diccionarios anidados -> estructuras más complejas con diccionarios dentro de otros.
