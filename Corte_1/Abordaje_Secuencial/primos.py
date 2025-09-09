#09/09/2025 programacion aplicada clase de las 8 am

#poner decima en primer corte

a = 1

while a == 1:
    value = int(input('Ingrese un numero: '))
    conta = 0

    for n in range(1, value + 1):
        residue = value % n
        if residue == 0:
            conta = conta + 1

    if conta == 2:
        print(f'{value} es un primo\n')
    else:
        print(f'{value} NO es un primo\n')

    print('¿Quieres continuar? Presiona 1 para continuar o cualquier otro número para salir')
    a = int(input())
