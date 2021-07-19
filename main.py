#Se inicializa la variable del resultado
suma_aseo = 0

while True:
    precio = int(input("Por favor ingrese el precio del artículo: "))
    tp = int(input("¿El artículo es de la categoría aseo? Sí(1) No(0)  "))
    if tp == 1:
        suma_aseo = suma_aseo + precio
    else:
        tp = int(
            input(
                "¿Desea continuar con el registro de productos? Si(1)_No(0)_"))
        if tp == 0:
            break
        continue

print("El total de su compra es: ", suma_aseo)
