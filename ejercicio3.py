p1 = input("Ingresa una película: ")
p2 = input("Ingresa otra película: ")
p3 = input("Ingresa una tercera película: ")
peliculas = [p1, p2, p3]

s1 = input("Ingresa una sala: ")
s2 = input("Ingresa otra sala: ")
s3 = input("Ingresa una tercera sala: ")
salas = [s1, s2, s3]

if "Interestelar" in peliculas:
    peliculas.append("Duna")
else:
    print("este string no esta en la lista")
    

if "Sala 3" in salas:
    salas.append("Sala VIP")
else:
    print("este string no esta en la lista")
    

if "Titanic" in peliculas:
    peliculas.remove("Titanic")
else:
    print("este string no esta en la lista")
    
if len(salas) > 3:
    salas.pop(0)
else:
    print("la lista no tiene mas de 3 elementos")
    
if "Avatar" in peliculas:
    peliculas.remove("Avatar")
    peliculas.append("Avatar 2")
else:
    print("este string no esta en la lista")
    
estrenos = peliculas[:2]
salas_disponibles = salas[-2:]

if "Sala VIP" in salas_disponibles:
    funcion_especial = ("Duna", "Sala VIP")
else:
    print("este string no esta en la lista")

if "Avatar 2" in estrenos:
    estrenos.append("3D")
else:
    print("este string no esta en la lista")

if "3D" in estrenos:
    programacion = {"pelicula": "Avatar 2", "sala": "Sala 2", "formato": "3D"}
else:
    print("este string no esta en la lista")
    
if 'programacion' in locals():
    programacion["hora"] = "6:30PM"
else:
    print("la variable programacion no existe")

if "Sala 4" not in salas:
    salas.append("Sala 4")
else:
    print("este string no esta en la lista")

if "Titanic" not in peliculas:
    peliculas.append("Titanic")
else:
    print("este string ya esta en la lista")
    
print(salas)
print(peliculas)
print(estrenos)
print(salas_disponibles)
print(funcion_especial)

if 'programacion' in locals():
    print(programacion)
else:
    print("la variable programacion no existe")