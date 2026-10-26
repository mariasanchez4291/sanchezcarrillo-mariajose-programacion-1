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

# Ejercicio: : Calculadora de envío

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

    