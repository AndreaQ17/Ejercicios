#1. Contar Ocurrencias de Elementos 
def contar_ocurrencias(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
palabras = ["python", "java", "python", "c++", "java", "java"]
resultado = contar_ocurrencias(palabras)
print(resultado)


#2. Combinar diccionarios 
def combinar_diccionarios(dict1, dict2):
    combinado = dict1.copy()  
    for clave, valor in dict2.items():
        if clave in combinado:
            combinado[clave] += valor  
        else:
            combinado[clave] = valor  
    return combinado
diccionario1 = {'a': 1, 'b': 2,}
diccionario2 = {'b': 3, 'c': 4,}
resultado = combinar_diccionarios(diccionario1, diccionario2)
print(resultado)


#LISTA DE FRECUENCIAS 
def lista_frecuencia(lista_numeros):
    frecuencia = {}
    for numero in lista_numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1  
        else:
            frecuencia[numero] = 1 
    return frecuencia
numeros = [1, 1, 2, 3, 3, 3]
resultado = lista_frecuencia(numeros)
print(resultado)


#4. FILTRAR PALABRAS LARGAS 
def filtrar_palabras_largas(lista_palabras, longitud_minima):
    palabras_largas = [palabra for palabra in lista_palabras if len(palabra) > longitud_minima]
    return palabras_largas
palabras = ["hola", "mundo", "python", "programacion"]
resultado = filtrar_palabras_largas(palabras, 6)
print(resultado)


#5. INVERSION DE TUPLAS EN LISTAS 
def invertir_tuplas(lista_tuplas):
    tuplas_invertidas = [tupla[::-1] for tupla in lista_tuplas]
    return tuplas_invertidas
lista = [(1, 2), (3, 4), (5, 6)]
resultado = invertir_tuplas(lista)
print(resultado)


#6. ENCONTRAR EL VALOR MAS FRECUENTE
from collections import Counter
def valor_mas_frecuente(lista_numeros):
    if not lista_numeros:
        return None 
    contador = Counter(lista_numeros)
    valor, frecuencia = contador.most_common(1)[0]
    return valor
numeros = [1, 2, 3, 1, 2, 1]
resultado = valor_mas_frecuente(numeros)
print(resultado) 


#7. COMPROBAR SUBCONJUNTO 
def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
resultado = es_subconjunto(conjunto_a, conjunto_b)
print(resultado)


#8. AGRUPACION POR CLAVE 
def agrupar_por_edad(lista_personas):
    agrupados = {}
    for persona in lista_personas:
        edad = persona["edad"]
        nombre = persona["nombre"]
        if edad not in agrupados:
            agrupados[edad] = []  
        agrupados[edad].append(nombre) 
    return agrupados
personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
resultado = agrupar_por_edad(personas)
print(resultado)  


#9. MERGUE SOURT UTILIZANDO LISTAS 


#10. ELIMINAR ELEMENTOS POR CONDICION 
def eliminar_menores(lista, limite):
    return [numero for numero in lista if numero >= limite]
numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = eliminar_menores(numeros, limite)
print(resultado)


#11. FLATTEN LIST OF LIST 
def aplanar_lista(lista_de_listas):
    return [elemento for sublista in lista_de_listas for elemento in sublista]
lista_de_listas = [[1, 2], [3, 4], [5]]
resultado = aplanar_lista(lista_de_listas)
print(resultado)  


#12 CALCULO DE MEDIANA 
def calcular_mediana(numeros):
    numeros.sort() 
    n = len(numeros)
    medio = n // 2
    if n % 2 == 0:
        return (numeros[medio - 1] + numeros[medio]) / 2
    else:
        return numeros[medio]
numeros = [1, 3, 2, 4, 5]
resultado = calcular_mediana(numeros)
print(resultado)  


#13. DUPLICAR ELEMENTOS DE UNA LISTA 
def duplicar_elementos(lista_numeros):
    return [numero for numero in lista_numeros for _ in range(2)]
numeros = [1, 2, 3]
resultado = duplicar_elementos(numeros)
print(resultado)


#14. CONTAR PALABRAS EN FRASES 
def contar_palabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = contar_palabras(frases)
print(resultado) 


#15. CONTAR CLAVE MAXIMA EN DICCIONARIO 
def clave_maxima(diccionario):
    if not diccionario:
        return None  
    return max(diccionario, key=diccionario.get)
diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = clave_maxima(diccionario)
print(resultado)  


#16. PALINDROMOS EN UNA LISTA 
def encontrar_palindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]

palabras = ["ana", "oso", "hola", "level"]
resultado = encontrar_palindromos(palabras)
print(resultado) 

