# Definición del diccionario con alturas de edificios
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Acceso directo a los valores mediante claves
print(building_heights["Burj Khalifa"])  # Imprime 828
print(building_heights["Ping An"])  # Imprime 599

# Diccionario con elementos del zodiaco por elemento
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Acceso a una clave que no existe de forma segura
key_to_check = "Landmark 81"
if key_to_check in building_heights:
   print(building_heights["Landmark 81"])

# Añadir una nueva clave al diccionario
zodiac_elements["energy"] = "Not a Zodiac element"

# Verificación de existencia antes de acceso
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

# Acceso seguro a los valores usando el método `.get()`
print(building_heights.get("Shanghai Tower"))  # Imprime 632
print(building_heights.get("My House"))  # Imprime None porque no existe la clave

# Obtener los IDs de los usuarios
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Obtener ID de un usuario específico, o asignar un valor por defecto si no existe
tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)  # Imprime 100019 si "teraCoder" existe, o 1000 si no existe

# Obtener un valor para una clave que no existe (asignando un valor por defecto)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)  # Imprime 100000 porque "superStackSmash" no está en el diccionario

# Eliminar un elemento de un diccionario con el método `.pop()`
raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}

# Eliminar un ítem y mostrar el valor eliminado
print(raffle.pop(320291, "No Prize"))  # Imprime "Gift Basket"
print(raffle)  # Muestra el diccionario sin el ítem con clave 320291

# Si intentamos eliminar una clave que no existe, se puede definir un valor predeterminado
print(raffle.pop(100000, "No Prize"))  # Imprime "No Prize" porque no existe la clave

# Eliminamos otro elemento
print(raffle.pop(872921, "No Prize"))  # Imprime "Concert Tickets"
print(raffle)  # Muestra el diccionario sin el ítem con clave 872921

# Operaciones de actualización en el diccionario utilizando `.pop()`
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}
health_points = 20

# Añadir el valor de los elementos "stamina grains" y "power stew" a los puntos de salud
health_points += available_items.pop("stamina grains", 0)  # Añade 15
health_points += available_items.pop("power stew", 0)  # Añade 30
health_points += available_items.pop("mystic bread", 0)  # No existe, así que añade 0

print(available_items)  # Muestra el diccionario sin los ítems eliminados
print(health_points)  # Imprime el total de puntos de salud, 20 + 15 + 30 = 65

# Obtener todas las claves del diccionario `test_scores`
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}
print(list(test_scores))  # Convierte las claves en una lista y las imprime

# Iterar sobre las claves con `.keys()`
for student in test_scores.keys():
    print(student)  # Imprime cada nombre de estudiante

# Obtener todas las claves de otro diccionario
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Obtener las claves y los valores de los diccionarios
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)  # Imprime todas las claves de `user_ids`
print(lessons)  # Imprime todas las claves de `num_exercises`

# Obtener los valores del diccionario `test_scores` con `.values()`
for score_list in test_scores.values():
    print(score_list)  # Imprime la lista de calificaciones de cada estudiante

# Calcular el total de ejercicios
total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # Imprime la suma total de ejercicios

# Obtener todos los elementos (pares clave-valor) con `.items()`
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")

# Porcentaje de mujeres en diversas ocupaciones
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
