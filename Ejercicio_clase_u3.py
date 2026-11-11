clave = " "
while clave != "python123":
    clave = input("contraseña: ")
print("acceso concedido")

while True:
    print("Se ejecuta al menos una vez")
    user_input = input("¿continuar? (si/no): ")
    if user_input.lower() != 'si': #upper()
        break

contador = 0
for _ in range(5):
    contador = contador + 1
print(contador)

# Ejercicio: Lista

precios = [50, 120, 30]
total = 0
for precio in precios:
    total = total + precio
print(total)

precios = [30 ,10, 9, 50, 29, 10]
total = 0
for precio in precios:
    total = total + precio
for precio in precios:
    print(precio)


matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[0][1])  #fila 0, columna 1

matriz = [
    [15, 8],
    [20,30]
]

matriz = [
    ["s", "o", "r", "p"],
    ["r", "e", "s"]
    ]

frutas = ["manzana", "pera"]
frutas.append("uva")        #agrega al final
frutas.insert(1, "kiwi")    #agrega en la posición 1
print(frutas)

frutas.remove("pera")       #elimina el valor
frutas.pop(0)               #elimina por indice
del frutas[0]               #elimina por indice
print(frutas)

frutas = ["manzana", "pera", "uva"]
print("pera" in frutas)  #True
print(frutas.index("uva"))  #2

precios = [45, 99, 150, 20]
total = 0
for precio in precios:
    total += precio
print("total:", total)

for fila in range(3):
    for columna in range(3):
        print("*", end=" ")
    print()

for fila in range (1, 3):
    for columna in range(1, 3):
        print(fila, columna)

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j)
        resultado = i * j
        print(i, "x", j, "=", resultado)

for numero in range(1, 10):
    if numero== 5:
        break
    print(numero)

numeros = [4, 9, -2, 7, -5]
for n in numeros:
    if n < 0:
        print ("Encontrado:" , n)
        break

for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)

alumno = {"nombre": "Ana", "edad": 20, "carrera": "creatividad"}
print(alumno["nombre"])
print(alumno["edad"])
alumno["edad"] = 21
print(alumno)
alumno["promedio"] = 9.5
print(alumno)
del alumno["carrera"]
print(alumno)
for clave in alumno:
    print(clave, ":", clave)

# Lista de diccionarios (ejemplo realista)
alumnos = [
    {"nombre": "Ana", "edad": 20, "carrera": "creatividad"},
    {"nombre": "Luis", "edad": 22, "carrera": "diseño"},
    {"nombre": "María", "edad": 21, "carrera": "arte"}
]

# Recorrer la lista y imprimir los dicionarios
for alumno in alumnos:
    print(f"{alumno['nombre']} estudia: {alumno['carrera']} y tiene {alumno['edad']} años")

# Lista de disccionarios (base de datos bancaria simple)
cuentas = [
    {"tarjeta": "1234567890", "nip": "4321", "saldo": 5000.0},
    {"tarjeta": "5555555555", "nip": "1111", "saldo": 2500.0},
    {"tarjeta": "9876543210", "nip": "9999", "saldo": 1000.0}
    ]
# Recorrer la lista y mostrar los datos de cada cuenta
for cuenta in cuentas:
    print(f"Tarjeta: {cuenta['tarjeta']} | NIP: {cuenta['nip']} | Saldo: ${cuenta['nip']} | Saldp: ${cuenta['saldo']: .2f}")  