def contar_vocales(nombre):
    #Creo un diccionario para almacenar el recuento de cada vocal
    recuento_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    #Convertimos el nombre a minúsculas para asegurarnos de contar las vocales correctamente
    nombre = nombre.lower()

    # Iteramos sobre cada letra del nombre
    for letra in nombre:
        if letra in recuento_vocales:
            # Incrementa el contador correspondiente si la letra es una vocal
            recuento_vocales[letra] += 1

    return recuento_vocales

def mostrar_recuento(recuento):
    # Muestra el recuento de cada vocal en la terminal
    for vocal, cantidad in recuento.items():
        print(f"{vocal}: {cantidad}")

# Pruebas para verificar el funcionamiento del código

def test_contar_vocales():
    resultado = contar_vocales("Gonzalo")
    assert resultado == {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 0}
    print("La función contar_vocales pasó las pruebas.")

def test_mostrar_recuento():
    recuento = {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 0}
    print("\nRecuento de vocales:")
    mostrar_recuento(recuento)

# Aca se ejecutan las pruebas
test_contar_vocales()
test_mostrar_recuento()
