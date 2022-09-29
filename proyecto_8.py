def validar(year):
    if year%4 == 2020%4:
        return True
    else:
        return False

year = int(input('Ingrese un año para indicar si es o no bisiesto: (yyyy)'))
if validar(year):
    print(f'El {year} es bisiesto')
else:
    print(f'El {year} no es bisiesto')