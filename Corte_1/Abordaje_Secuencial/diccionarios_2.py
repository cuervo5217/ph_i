# ========================================
# Acceder a valores en un diccionario (Get a Key)
# ========================================

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Al usar [clave] accedemos directamente al valor
print(building_heights["Burj Khalifa"])   # 828
print(building_heights["Ping An"])        # 599


zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}
print(zodiac_elements["earth"])  # ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])   # ['Aries', 'Leo', 'Sagittarius']


# ========================================
# Manejar claves inválidas (Get an Invalid Key)
# ========================================

# Esto genera un ERROR (KeyError) porque la clave no existe:
# print(building_heights["Landmark 81"])

# Solución: verificar si la clave existe antes de usarla
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])  # solo se ejecuta si la clave existe

# Ejemplo con un diccionario de elementos del zodiaco
zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])   # Imprime "Not a Zodiac element"


# ========================================
# Método .get() para acceder de forma segura
# ========================================

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Si existe, devuelve el valor:
print(building_heights.get("Shanghai Tower"))  # 632

# Si NO existe, devuelve None en vez de error:
print(building_heights.get("My House"))        # None


# Otro ejemplo
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Acceder con get()
print(user_ids.get("teraCoder"))  # 100019

# Si la clave existe, guardamos el valor; si no, guardamos un valor por defecto
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")
print(tc_id)  # 100019

# Si la clave no existe, podemos asignar un valor predeterminado
if user_ids.get("superStackSmash") == None:
    stack_id = 100000
print(stack_id)  # 100000


# ========================================
# Eliminar claves con .pop()
# ========================================

raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}

# .pop(clave, valor_predeterminado)
# Si la clave existe → la elimina y devuelve su valor
print(raffle.pop(320291, "No Prize"))  # Gift Basket
print(raffle)  # ahora sin 320291

# Si la clave NO existe → devuelve el valor por defecto
print(raffle.pop(100000, "No Prize"))  # No Prize
print(raffle)

# Eliminamos otro elemento
print(raffle.pop(872921, "No Prize"))  # Concert Tickets
print(raffle)


# Otro ejemplo: sumar puntos con .pop()
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}
health_points = 20

# Cada .pop() devuelve un valor y además lo quita del diccionario
health_points += available_items.pop("stamina grains", 0)  # +15
health_points += available_items.pop("power stew", 0)      # +30
health_points += available_items.pop("mystic bread", 0)    # +0 (no existe)

print(available_items)  # diccionario modificado
print(health_points)    # 65


# ========================================
# Obtener todas las CLAVES (keys)
# ========================================

test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

print(list(test_scores))  # ['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Dina']

# Recorrer claves con un bucle
for student in test_scores.keys():
    print(student)


# Ejemplo práctico: acceder a claves
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)


# ========================================
# Obtener todos los VALORES (values)
# ========================================

# Recorremos solo valores (listas de notas en este caso)
for score_list in test_scores.values():
    print(score_list)

# Ejemplo: sumar todos los valores de un diccionario
total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # 115


# ========================================
# Obtener claves y valores juntos (items)
# ========================================

biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
