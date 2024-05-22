import random

print("Bienvenido al juego del ahorcado")
print("================================")

# Lista de palabras del juego
palabras_al_azar = ["almanaque", "historia", "edificio", "cuna", "reposera"]

letras_incorrectas = []

dict_correcto = {}

dict_anterior = {}

vidas = 5

cant_correctas = 0

# Elegir una palabra al azar dentro de una lista de palabras, previamente definida
palabra_al_azar = random.choice(palabras_al_azar).upper()

print(palabra_al_azar)

def pedir_letra():
    letra = input("Ingrese una letra: ").upper()
    print("letra: ", letra)
    if type(letra) != str:
        print("Debe ingresar una letra!")
    elif len(letra) > 1:
        print("Debe ingresar una sola letra!")
    else:
        letra = letra.upper()
        return letra
    
def letra_en_palabra(letra, palabra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            return True
    return False

def ordenar_diccionario(dicc):
    diccionario_con_claves_faltantes = {}
    for clave in range(len(palabra_al_azar)):
        valor = dicc.get(clave, "-")
        diccionario_con_claves_faltantes.setdefault(clave, valor)

    valores = diccionario_con_claves_faltantes.values()

    valores_sin_formato = ' '.join(valores)

    print(valores_sin_formato)

    return diccionario_con_claves_faltantes
                         
while vidas > 0 and cant_correctas < len(palabra_al_azar):
    
    letra_elegida = pedir_letra()

    if letra_en_palabra(letra_elegida, palabra_al_azar):

        for i in range(len(palabra_al_azar)):
            if palabra_al_azar[i] == letra_elegida:

                dict_correcto.update({i: letra_elegida})
                cant_correctas += 1

            elif palabra_al_azar[i] == "_" or palabra_al_azar[i] == "":
                print(f"palabra_al_azar[i]: {palabra_al_azar[i]}")
                dict_correcto.update({i: "_"})
    else:
        letras_incorrectas.append(letra_elegida)

        print(f"La letra {letra_elegida} no está en la palabra.")
        print(f"La lista de letras incorrectas, es: {letras_incorrectas}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")

    ordenar_diccionario(dict_correcto)

if vidas == 0:
    print("Perdiste")
    print(f"La palabra era: {palabra_al_azar}")

if cant_correctas == len(palabra_al_azar):
    #ordenar_diccionario(dict_correcto)
    print("Ganaste!")