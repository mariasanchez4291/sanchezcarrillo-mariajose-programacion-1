# Ejercicio - ¿Es par o impar?

numero = 8
es_par = "numero % 2 == 0"
print("Número:", numero)
print("¿Es par?", es_par)

# Ejercicio - concatenar vs sumar

texto1 = "5"
texto2 = "3"
resultado_concatenar = texto1 + texto2
print("Resultado como texto (concatenación):", resultado_concatenar)
numero1 = int(texto1)
numero2 = int(texto2)
resultado_sumar = numero1 + numero2
print("Resultado como número (suma):", resultado_sumar)

# Ejercicio - Mini reporte de un perfil
nombre = "Maria"
edad = 18
estatura = 1.60
es_estudiante = True

print("nombre", nombre, "| Tipo:" , type(nombre))
print("edad", edad, "| Tipo:" , type(edad))
print("estatura", estatura, "| Tipo:" , type(estatura))
print("es_estudiante", es_estudiante, "| Tipo:" , type(es_estudiante))

mensaje_resumen = nombre + " tiene " + str(edad) + " años"
print("\n--- RESUMEN ---")
print(mensaje_resumen)

# Ejercicio - Operadores aritméticos basicos

a = 17
b = 5

print("Ejercicio 1: Operadores aritméticos básicos")
print("Suma (17 + 5):", a + b)
print("Resta (17 - 5):", a - b)
print("Multiplicación (17 * 5):", a * b)
print("División (17 / 5):", a / b)

print("\nEjercicio 2: División entera y módulo")
print("División entera (17 // 5):", a // b)
print("Módulo (17 % 5):", a % b)

# Ejercicio - Operadores relacionales

a = 8
b = 5
es_mayor = a > b
es_menor = a < b
es_igual = a == b
es_diferente = a != b

print("Prueba con numeros diferentes:")
print("¿8 es mayor que 5?", es_mayor)
print("¿8 es menor que 5?", es_menor)
print("¿8 es igual a 5?", es_igual)
print("¿8 es diferente de 5?", es_diferente)

# Prueba con numeros iguales:

a = 5
b = 5
es_mayor = a > b
es_menor = a < b
es_igual = a == b
es_diferente = a != b

print("\nPrueba con numeros iguales (a =", a, ", b =", b, ") ---")
print("¿a es mayor que b?", es_mayor)
print("¿a es menor que b?", es_menor)
print("¿a es igual a b?", es_igual)
print("¿a es diferente de b?", es_diferente)

# Operadores lógicos

x = 15
y = 20
condicion1 = x > 10
condicion2 = y < 18
resultado_and = (x > 10) and (y < 18)
resultado_or = (x > 10) or (y < 18)
resultado_not = not (x > 10)

print("prueba de operadores lógicos:")
print("Valores de prueba: x =", x, ", y =", y)
print("Condición 1 (x > 10):", condicion1)
print("Condición 2 (y < 18):", condicion2)
print("Resultado AND (x >10 and y <18):",resultado_and)
print("Resultado OR (x >10 or y <18):", resultado_or)
print("Resultado NOT (not x >10):", resultado_not)

# Ejercicio - promedio y descuento
nota1 = 8.0
nota2 = 7.5
nota3 = 6.0
promedio = (nota1 + nota2 + nota3) / 3
aprobado = promedio >= 6.0

print("caso 1: Notas altas")
print("calificaciones:", nota1, nota2, nota3)
print("promedio:", promedio)
print("¿Está aprobado?:", aprobado)

# caso 2: Notas bajas
nota1 = 4.0
nota2 = 5.0
nota3 = 5.5
promedio = (nota1 + nota2 + nota3) / 3
aprobado = promedio >= 6.0

print("\ncaso 2: Notas bajas")
print("calificaciones:", nota1, nota2, nota3)
print("promedio:", promedio)
print("¿Está aprobado?:", aprobado)

# Ejercicio - Validacion de elegibilidad
edad = 20
nacionalidad = "mexicana"
es_elegible = (edad > 18) and nacionalidad == "mexicana"

print("caso 1:elegible")
print("Edad:", edad, "| Nacionalidad:", nacionalidad)
print("¿Es elegible?:", es_elegible)

# caso 2: no elegible
edad = 17
nacionalidad = "mexicana"
es_elegible = (edad > 18) and nacionalidad == "mexicana"

print("caso 2: no elegible")
print("Edad:", edad, "| Nacionalidad:", nacionalidad)
print("¿Es elegible?:", es_elegible)

# caso 3: no elegible por nacionalidad
edad = 20
nacionalidad = "Argentina"
es_elegible = (edad > 18) and nacionalidad == "mexicana"

print("caso 3: no elegible por nacionalidad")
print("Edad:", edad, "| Nacionalidad:", nacionalidad)
print("¿Es elegible?:", es_elegible)