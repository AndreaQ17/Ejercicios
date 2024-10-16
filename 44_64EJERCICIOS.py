#1 Variante con nombre 
nombre = "Rubi"
print(nombre)

# 2 Crear una variable que contenga tu edad y mostrarla.
edad = 25
print(edad)  

# 3 Comprobar si tu edad es mayor de 18 y mostrar un mensaje.
if edad > 18:
    print("Eres mayor de edad.")  

# 4 Comprobar si tu edad es igual a 18 y mostrar un mensaje.
if edad == 18:
    print("Tienes 18 años.")  

# 5 Crear una lista de números del 1 al 5 y mostrarla.
numeros = [1, 2, 3, 4, 5]
print(numeros)  

# 6 Sumar todos los números de la lista y mostrar el resultado.
suma = sum(34)
print(suma)  

# 7. Crear un diccionario con información personal y mostrarlo.
persona = {"nombre": "Rubi", "edad": 20}
print(persona)

# 8 Acceder a un valor en el diccionario y mostraralo 
mi_diccionario = {
    "nombre": "Rubi"
}
valor = mi_diccionario["nombre"]
print(valor)

# 9 Crea un bucle que imprima los numeros del 1 al 10 
for i in range(1, 11):
    print(i, end=", " if i < 10 else "")

# 10 Crear un bucle que imprima solo los numeros pares del 1  
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=', ')
print('\b\b ') 

# 11 Crear una lista de frutas y mostrara solo la que empieza con "a"
frutas = ["manzana", "pera", "aguacate", "banana"]
frutas_con_a = [fruta for fruta in frutas if fruta.startswith('a')]
print(frutas_con_a)

# 12 Crear un bucle que imprima los elementos de una lista con su índice. 
frutas = ["manzana", "pera", "aguacate", "banana"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: \"{fruta}\"")

# 13 Crear un conjunto de números y mostrarlo.
numeros = {1, 2, 3, 4, 5}
print(numeros)

# 14 Comprobar si un número está en el conjunto (set) y mostrar un mensaje.
numeros = {1, 2, 3, 4, 5}
numero_a_comprobar = 3
if numero_a_comprobar in numeros:
    print(f"{numero_a_comprobar} está en el conjunto.")
else:
    print(f"{numero_a_comprobar} no está en el conjunto.")

# 15 Crear un bucle que imprima los números del 10 al 1 en orden descendente.
for i in range(10, 0, -1):
    print(i, end=', ')
print('\b\b ')

# 16 Crear una función que reciba dos números y devuelva su suma.
def suma(a, b):
    return a + b
resultado = suma(3, 5)
print(resultado)  

# 17 Crear una función que reciba una lista y devuelva su longitud.
def longitud(lista):
    return len(lista)
resultado = longitud([1, 2, 3])
print(resultado) 

# 18 Crear una función que determine si un número es par.
def es_par(numero):
    return numero % 2 == 0
resultado = es_par(4)
print(resultado) 

# 19 Crear una función que reciba un diccionario y devuelva solo sus claves.
def obtener_claves(diccionario):
    return list(diccionario.keys())
resultado = obtener_claves({"a": 1, "b": 2})
print(resultado)  

# 20 Crear una lista de números y mostrar solo los que son mayores que 5.
numeros = [1, 3, 5, 7, 9, 2, 4, 6]
mayores_que_5 = [num for num in numeros if num > 5]
print(mayores_que_5) 

# 21 Crear una lista de palabras y mostrar su longitud total.
palabras = ["hola", "mundo", "python"]
longitud_total = sum(len(palabra) for palabra in palabras)
print(longitud_total)

#22
elementos = ["a", "b", "a", "c"]
resultado = elementos.count("a")
print(resultado) 

#23
numeros = [1, 2, 3, 4, 5]
promedio = sum(numeros) / len(numeros)
print(promedio) 

#24
mi_diccionario = {"nombre": "Juan"}
mi_diccionario["edad"] = 30
print(mi_diccionario)  

# 25
mi_diccionario = {"nombre": "Juan", "edad": 25}
mi_diccionario.pop("edad")
print(mi_diccionario)
mi_diccionario["edad"] = 25
del mi_diccionario["edad"]
print(mi_diccionario)

# 26
for num in range(1, 6):
    print(num ** 2)
  
# 27
fibonacci = [0, 1]
for i in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci) 

# 28
numeros = [1, 2, 3, 4, 5]
if 3 in numeros:
    print("3 está en la lista.")  
    
# 29
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 30
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(7))  

# 31
for i in range(1, 21):
    if i == 3:
        print("Fizz")
    elif i == 5:
        print("Buzz")
    else:
        print(i)

#32
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
#33
numeros = [1, 2, 3, 4, 5]
resultado_33 = list(map(lambda x: x * 2, numeros))
print(resultado_33)  

        
#34
numeros = [1, 2, 3, 4, 5, 6]
resultado_34 = list(filter(lambda x: x % 2 == 0, numeros))
print(resultado_34)  
        
#35
palabras = ["Hola", "mundo"]
resultado_35 = " ".join(palabras)
print(resultado_35)  

#36
numeros = [1, -2, 3, -4, 5]
negativos = [n for n in numeros if n < 0]
print(negativos)  

#37
conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}
union = conjunto1 | conjunto2
print(union)

#38

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
interseccion = conjunto1 & conjunto2
print(interseccion)

#39
mi_diccionario = {"a": 1, "b": 2}
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}") 
    
    #40
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in cadena if letra in vocales)
    return contador
resultado = contar_vocales("Hola")
print(resultado)

#41
import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print(numeros_aleatorios)

#42
numeros = [5, 3, 1, 4, 2]
numeros.sort()
print(numeros)

#43
mi_diccionario = {"a": 1, "b": 2}
if "a" in mi_diccionario:
    print("La clave 'a' existe.")

# 44. Crear un bucle que imprima los elementos de una lista en reversa.
lista = [1, 2, 3]
for num in reversed(lista):
    print(num)

# 45. Crear una función que devuelva el factorial de un número.
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
print(factorial(5))

# 46. Crear una lista de tuplas y mostrar cada tupla en una línea.
lista = [(1, 'a'), (2, 'b')]
for tupla in lista:
    print(f"{tupla[0]}: {tupla[1]}")

# 47. Crear una lista y usar zip para combinar dos listas en una lista de tuplas.
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = list(zip(lista1, lista2))
print(combinada)


# 48. Crear una función que reciba un texto y devuelva el texto en mayúsculas.
def mayusculas(texto):
    return texto.upper()
print(mayusculas("hola"))

#49. Craer una lista de numeros y devolver la suma de los numeros negativos 
numeros = [1, -2, 3, -4, 5]
sumnegativos = sum(n for n in numeros if n < 0)
print(sumnegativos)

# 50. Crear un programa que imprima los números del 1 al 100, pero resalte los múltiplos de 3 y 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} es múltiplo de 3 y 5")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} es múltiplo de 5")
    else:
        print(i)

# 51. Crear una lista de nombres y contar cuántos nombres tienen más de 5 letras.
nombres = ["Juan", "Alejandro", "Maria"]
letras = sum(1 for nombre in nombres if len(nombre) > 5)
print(letras)

# 52. Crear un programa que imprima las tablas de multiplicar del 1 al 5.
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# 53. Crear una función que reciba una lista y devuelva la lista invertida.
def invertir_lista(lista):
    return lista[::-1]
print(invertir_lista([1, 2, 3])) 

# 54. Crear un programa que muestre la suma de todos los números pares del 1 al 100.
pares = sum(i for i in range(1, 101) if i % 2 == 0)
print(pares)

# 55. Crear un diccionario y mostrar solo los elementos con valores mayores a 10.
mi_diccionario = {"a": 5, "b": 15, "c": 20}
elementos = {k: v for k, v in mi_diccionario.items() if v > 10}
print(elementos) 

# 56. Crear una lista de números y multiplicar todos los elementos.
numeros = [1, 2, 3, 4]
producto = 1
for num in numeros:
    producto *= num
print(producto) 

# 57. Crear una función que reciba una lista y devuelva el máximo.
def maximo(lista):
    return max(lista)
print(maximo([1, 2, 3]))

# 58. Crear un bucle que imprima los caracteres de una cadena.
cadena = "Hola"
for char in cadena:
    print(char)


# 59. Crear un programa que sume todos los elementos de una lista y devuelva True si la suma es mayor a 50.
numeros = [10, 20, 30]
suma_total = sum(numeros)
print(suma_total > 50)

# 60. Crear una función que reciba una cadena y devuelva la cantidad de consonantes.
def contar (texto):
    consonantes = "bcdfghjklmnpqrstvwxyzh"
    return sum(1 for char in texto.lower() if char in consonantes)
print(contar ("Hola"))  

# 61. Crear una lista de números y mostrar el segundo mayor.
numeros = [5, 1, 3, 4, 2]
mayor = sorted(set(numeros))[-2]
print(mayor)

# 62. Crear una lista de palabras y contar cuántas contienen la letra 'e'.
palabras = ["mesa", "silla", "ventana", "puerta"]
conteo_e = sum(1 for palabra in palabras if 'e' in palabra)
print(conteo_e) 

# 63. Crear una lista de enteros y devolver una nueva lista con los elementos únicos.
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = list(set(numeros))
print(unicos) 

# 64. Crear una función que reciba una lista y devuelva una lista con los elementos duplicados.
def duplicados(lista):
    duplicados = set([x for x in lista if lista.count(x) > 1])
    return list(duplicados)
print(duplicados([1, 2, 2, 3]))