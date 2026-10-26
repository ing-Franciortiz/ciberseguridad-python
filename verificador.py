import json

with open("comunes.json", encoding="utf-8") as archivo:
    comunes = json.load(archivo)

while True:
    password = input("Escribe una contrasena:")
    

    problemas = []
    tiene_numero = False
    tiene_mayuscula = False
    tiene_caracter_especial = False
    tiene_minuscula = False
    
    for caracter in password:
        if caracter.isdigit():
            tiene_numero = True
            
        if caracter.isupper():
            tiene_mayuscula = True
            
        if caracter in "!@#$%^&*()-+":
            tiene_caracter_especial = True
            
        if caracter.islower():
            tiene_minuscula = True
    
    if len(password) < 8:
        problemas.append("es muy corta")
    if not tiene_numero:
        problemas.append("no tiene un numero")
    if not tiene_mayuscula:
        problemas.append("no tiene una mayuscula")
    if not tiene_caracter_especial:
        problemas.append("no tiene un caracter especial")
    if not tiene_minuscula:
        problemas.append("no tiene una minuscula")
    if password.lower() in comunes:
        problemas.append("es muy comun")

    if len(problemas) == 0:
        print("La contrasena es valida")
        break
    else:
        print("La contrasena es debil:")
        for problema in problemas:
            print("-",problema)