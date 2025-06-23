edad = int(input("Introduce tu edad: "))
membresia = input("¿Tienes membresía activa? (si/no): ").lower()

if edad < 18:
    print("No puedes acceder al club.")
elif edad >= 18:
    if membresia == "si":
        print("Puedes acceder al club.")
    else:
        print("No puedes acceder al club, necesitas membresía activa.")
