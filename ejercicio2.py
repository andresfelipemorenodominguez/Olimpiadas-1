print("Comparacion de precios por kilo")
producto1 = input("Ingrese el nombre del primer producto: ")
precio1 = float(input(f"Ingrese el precio por kilo de {producto1}: "))
peso1 = float(input(f"Ingrese el peso del {producto1} en kilos: "))
op1 = precio1 / peso1

producto2 = input("Ingrese el nombre del segundo producto: ")
precio2 = float(input(f"Ingrese el precio por kilo de {producto2}: "))
peso2 = float(input(f"Ingrese el peso del {producto2} en kilos: "))
op2 = precio2 / peso2

if op1 < op2:
    print(f"El producto {producto1} es mas barato que {producto2}.")
    
elif op1 > op2:
    print(f"El producto {producto2} es mas barato que {producto1}.")
    
else:
    print(f"Los productos {producto1} y {producto2} tienen el mismo precio por kilo.")