# Ejercicio: Clasificación por edad

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("niño.")
elif 13 <= edad < 17:
    print("adolescente.")
else:
    print("adulto.")

# Ejercicio: Validar acceso

usuario_correcto = "Maria"
contraseña_correcta = "1234"

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == usuario_correcto:
    if contraseña == contraseña_correcta:
        print("Acceso concedido.")
    else:
        print("Usuario correcto, pero contraseña incorrecta.")
else:
    print("Usuario no encontrado.")

# Ejercicio: Calculadora de envío

peso = float(input("Ingrese el peso del paquete (kg): "))

if peso <= 1:
    print("El costo de envío es $50.")
elif 1 < peso <= 5:
    print("El costo de envío es $90.")
elif 5 < peso:
    print("El costo de envío es $150.")

descuento = 0.10
if peso > 10:
    print(f"10% de descuento:${150 * (1 - descuento)}.")

# Ejercicio: Clasificación de temperatura
temperatura = float(input("Ingrese la temperatura (°C): "))
    
if temperatura < 10:
    print("frio.")
elif 10 <= temperatura <= 24:
    print("templado.")
else:
    print("calor.")

# Ejercicio: Clasificación de letras

calificacion = float(input("Ingresa la calificación (de 0 a 100): "))

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
else:
    print("D")

# Ejercicio: Clasificación de números

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("positivo.")
elif numero < 0:
    print("negativo.")
else:
    print("cero.")

# Ejercicio: Descuento por monto de compra

monto = float(input("Ingresa el monto de la compra: "))
if monto > 500:
    porcentaje_descuento = 20
    descuento = monto * 0.20
elif monto > 200:
    porcentaje_descuento = 10
    descuento = monto * 0.10
else:
    porcentaje_descuento = 0
    descuento = 0

monto_final = monto - descuento
print(f"Porcentaje de descuento aplicado: {porcentaje_descuento}%")
print(f"Monto final a pagar: ${monto_final:.2f}")

# Ejercicio: Validar un rango con comparación encadenada

numero = int(input("Ingresa un número: "))
if 1 <= numero <= 100:
    print("El número está en el rango (entre 1 y 100).")
else:
    print("El número no está en el rango.")

# Ejercicio: Clasificar el IMC

peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))
imc = peso / (estatura ** 2)

if imc < 18.5:
    clasificacion = "bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "normal"
elif 25 <= imc <= 29.9:
    clasificacion = "sobrepeso"
else:
    clasificacion = "obesidad"
print(f"Tu IMC es: {imc:.2f}")
print(f"Clasificación: {clasificacion}")

# Ejercicio: Tarifas de electricidad

consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo <= 150:
    costo_total = consumo * 1.20
elif consumo <= 300:
    costo_total = (150 * 1.20) + ((consumo - 150) * 1.80)
else:
    costo_total = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print(f"Consumo: {consumo} kWh")
print(f"Costo total: ${costo_total:.1f}")
