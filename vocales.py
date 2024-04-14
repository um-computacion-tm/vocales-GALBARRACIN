def replace(mystring):
    # Diccionario que mapea las letras con acento a sus versiones sin acento
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'Á':'a', 'É':'e', 'Í':'i', 'Ó':'o', 'Ú':'u'}
    # Lista de las letras con acento, que son las claves del diccionario
    claves = list(acentos.keys())
    # Lista de las letras sin acento, que son los valores del diccionario
    valores = list(acentos.values())
    # Itera sobre cada índice en la cadena de texto
    for i in range(0, len(mystring)):
        # Verifica si la letra en la posición actual está en la lista de claves (letras con acento)
        if mystring[i] in claves:
            # Obtiene el índice de la letra con acento en la lista de claves
            indice = claves.index(mystring[i])
            # Reemplaza la letra con acento por su equivalente sin acento en la cadena de texto
            mystring = mystring.replace(mystring[i], valores[indice])
    # Devuelve la cadena de texto modificada
    return mystring

def count_vocales(mystring):
    # Convierte la cadena de texto a minúsculas para facilitar la comparación
    mystring = mystring.lower()
    # Tupla que contiene las vocales
    vocales = ('a', 'e', 'i', 'o', 'u')
    # Diccionario para almacenar el recuento de cada vocal
    resultado2 = {}
    # Itera sobre cada letra en la cadena de texto
    for letra in mystring:
        # Verifica si la letra actual es una vocal
        if letra in vocales:
            # Si la vocal no está en el diccionario resultado2, la agrega con un valor inicial de 0
            if letra not in resultado2:
                resultado2[letra] = 0
            # Incrementa el recuento de la vocal en el diccionario resultado2
            resultado2[letra] += 1
    # Devuelve el diccionario con el recuento de vocales
    return resultado2

# Solicita al usuario que ingrese una palabra
mystring = input('Ingrese una palabra: ')
# Llama a la función replace para quitar los acentos y luego a la función count_vocales para contar las vocales
print(count_vocales(replace(mystring)))