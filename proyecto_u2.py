nombre = "Maria Jose"
producto = input("Ingresa el nombre del producto: ")
cantidad = int(input("Ingresa la cantidad: "))
precio = float(input("Ingresa el precio por unidad: "))

subtotal = cantidad * precio
iva = subtotal * 0.16
total = subtotal + iva

print("Recibo de la compra:")
print(f"Nombre: {nombre}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"IVA (16%): ${iva}")
print(f"Total a pagar: ${total}")
