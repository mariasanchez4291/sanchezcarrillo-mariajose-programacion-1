# Ejercicio: Datos personales

nombre = "Maria"
edad = 18
ciudad = "Guadalajara"
print (nombre, edad, ciudad)

# Ejercicio: Actualizar un contador
contador = 0
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)

# Ejercicio: Constante de conversión
PULGADAS_A_CM = 2.54
pulgadas = "10"
centimetros = int (pulgadas) * PULGADAS_A_CM
print(f"{pulgadas} pulgadas son {centimetros} centímetros.")

# Ejercicio: Área de un rectángulo
base = "9"
altura = "5"
area = int(base) * int(altura)
print(f"El área del rectángulo es {area}.")

# Ejercicio: Total con IVA

IVA = 0.16
precio_texto = "100"
precio = float(precio_texto)
monto_iva = precio * IVA
total = precio + monto_iva

es_valido = total > 0

print("--- Total con IVA ---")
print(f"Precio: {precio}")
print(f"IVA: {monto_iva}")
print(f"Total: {total}")
print(f"¿Es válido? {es_valido}")

print("\n--- RESULTADO ---")
print(f"El precio base es: ${precio}")
print(f"El monto del IVA es: ${monto_iva}")
print(f"El total a pagar es: ${total}")

# Ejercicio: Intercambio de valores
a = 10
b = 20
print("--- Antes del intercambio ---")
print("a:", a)
print("b:", b)

temp = a
a = b
b = temp
print("--- Después del intercambio ---")
print("a:", a)
print("b:", b)

print("\n--- Intercambio abreviado en Python ---")
a, b = b, a
print("a:", a)
print("b:", b)

# Ejercicio: Identificar tipos con type()
print(10 + 20)
print(type(10 + 20))

# Ejercicio: convertir tipos
texto = "25"
print(texto, "tipo:", type(texto))
numero = int(texto)
print("Resultado entero:", numero, "tipo:", type(numero))
numero = 100
texto = str(numero)
print("Resultado de la conversión:", texto, "tipo:", type(texto))

# Ejercicio :Booleanos y comparaciones

a = 8
b = 3
mayor = a > b
print("Resultado de la comparación:", mayor)
print("Tipo de dato:", type(mayor))