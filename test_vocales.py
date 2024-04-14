import unittest

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

# Clase que contiene las pruebas unitarias
class TestContarVocales(unittest.TestCase):
    # Método de prueba para verificar el comportamiento cuando se pasa una cadena sin vocales
    def test_nada(self):
        sinacentos = replace('zzz')  # Reemplaza acentos en una cadena sin vocales
        resultado2 = count_vocales(sinacentos)  # Cuenta las vocales en la cadena sin acentos
        self.assertEqual(resultado2, {})  # Verifica que el resultado sea un diccionario vacío

    # Método de prueba para verificar el comportamiento cuando se pasa una cadena con una vocal 'a'
    def test_cas(self):
        sinacentos = replace('cas')  # Reemplaza acentos en una cadena con la vocal 'a'
        resultado2 = count_vocales(sinacentos)  # Cuenta las vocales en la cadena sin acentos
        self.assertEqual(resultado2, {'a': 1})  # Verifica que el resultado sea un diccionario con una 'a'
    # Prueba con una cadena sin ninguna vocal
    def test_sin_vocales(self):
        sinacentos = replace('hola mundo')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {})

    # Prueba con una cadena que contiene todas las vocales
    def test_todas_vocales(self):
        sinacentos = replace('a e i o u')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    # Prueba con una cadena que contiene múltiples repeticiones de las mismas vocales
    def test_repeticiones_vocales(self):
        sinacentos = replace('elefante')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'e': 2, 'a': 1})

    # Prueba con una cadena que contiene mayúsculas y minúsculas
    def test_mayusculas_minusculas(self):
        sinacentos = replace('AeIoU')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

     # Prueba para la palabra "casa"
    def test_casa(self):
        sinacentos = replace('casa')  # Reemplaza acentos en "casa"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "casa" sin acentos
        self.assertEqual(resultado2, {'a': 2})  # Verifica que el resultado sea {'a': 2}

    # Prueba para la palabra "bese"
    def test_bese(self):
        sinacentos = replace('bese')  # Reemplaza acentos en "bese"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "bese" sin acentos
        self.assertEqual(resultado2, {'e': 2})  # Verifica que el resultado sea {'e': 2}

    # Prueba para la palabra "besa"
    def test_besa(self):
        sinacentos = replace('besa')  # Reemplaza acentos en "besa"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "besa" sin acentos
        self.assertEqual(resultado2, {'a': 1, 'e': 1})  # Verifica que el resultado sea {'a': 1, 'e': 1}

    # Prueba para la palabra "casanova"
    def test_casanova(self):
        sinacentos = replace('casanova')  # Reemplaza acentos en "casanova"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "casanova" sin acentos
        self.assertEqual(resultado2, {'a': 3, 'o': 1})  # Verifica que el resultado sea {'a': 3, 'o': 1}

    # Prueba para la palabra "mUrciElago"
    def test_mUrciElago(self):
        sinacentos = replace('mUrciElago')  # Reemplaza acentos en "mUrciElago"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "mUrciElago" sin acentos
        self.assertEqual(resultado2, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})  # Verifica el resultado completo

    # Prueba para la palabra "RELAMPAGO"
    def test_RELAMPAGO(self):
        sinacentos = replace('RELAMPAGO')  # Reemplaza acentos en "RELAMPAGO"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "RELAMPAGO" sin acentos
        self.assertEqual(resultado2, {'a': 2, 'e': 1, 'o': 1})  # Verifica que el resultado sea {'a': 2, 'e': 1, 'o': 1}

    # Prueba para la palabra "matEmática"
    def test_matEmática(self):
        sinacentos = replace('matEmática')  # Reemplaza acentos en "matEmática"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "matEmática" sin acentos
        self.assertEqual(resultado2, {'a': 3, 'e': 1, 'i': 1})  # Verifica el resultado

    # Prueba para la palabra "ÁRBITRO"
    def test_ÁRBITRO(self):
        sinacentos = replace('ÁRBITRO')  # Reemplaza acentos en "ÁRBITRO"
        resultado2 = count_vocales(sinacentos)  # Cuenta vocales en "ÁRBITRO" sin acentos
        self.assertEqual(resultado2, {'a': 1, 'i': 1, 'o': 1})  # Verifica el resultado

unittest.main()