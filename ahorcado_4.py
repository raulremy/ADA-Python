import random

print("Bienvenido al juego del ahorcado")
print("================================")

# Lista de palabras del juego
palabras_al_azar = ["almanaque", "historia", "edificio", "cuna", "reposera"]

letras_incorrectas = []

dict_correcto = {}

vidas = 5

cant_correctas = 0

# Elegir una palabra al azar dentro de una lista de palabras, previamente definida
palabra_al_azar = random.choice(palabras_al_azar)

print(palabra_al_azar)
                  
"""
def mostrar_guiones(palabra_al_azar):
    for i in range(len(palabra_al_azar)):
        print("_", end=" ")
    print()

mostrar_guiones(palabra_al_azar)
"""

def mostrar_diccionario(diccionario):
    for i in range(len(palabra_al_azar)):
        if i in diccionario.keys():
            diccionario_ordenado = dict(sorted(diccionario.items()))
        else:
            print("_", end=" ")

    for j in diccionario_ordenado.values():
        print(j, end = '')
#        print(" ", end = '')
    print("\n", end = '')
"""
    for j in diccionario_ordenado.values():
        print("- ", end = '')
    print("\n", end = '')
"""
print("Ganaste!")

    #fin_diccionario

def pedir_letra():
    letra = input("Ingrese una letra: ")
    if type(letra) != str:
        print("Debe ingresar una letra!")
    elif len(letra) > 1:
        print("Debe ingresar una sola letra!")
    else:
        return letra
def letra_en_palabra(letra, palabra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            return True
    return False

""""
def fin_diccionario(dicc):
    for i in dicc:
        print(str(dicc[i]), end=" ")
        print("\n")
        print("_", end=" ")
    return True
"""
                 
while vidas > 0 and cant_correctas < len(palabra_al_azar):
    
    letra_elegida = pedir_letra()

    print(letra_elegida)

    if letra_en_palabra(letra_elegida, palabra_al_azar):
        # print("La letra está en la palabra")
        # Idea: poblar la lista, palabra creada
        # for i in range(0, len(palabra_al_azar)-1):
        for i in range(len(palabra_al_azar)):
            if palabra_al_azar[i] == letra_elegida:

                dict_correcto.update({i: letra_elegida})

                #print("3 dict_correcto: " + str(dict_correcto))

                #mostrar_diccionario(dict_correcto)
                cant_correctas += 1
                #print(f"cant_correctas: {cant_correctas}")
                #print(f"dict_correcto: {dict_correcto}")

            else:
                print("_", end=" ")
    else:
        letras_incorrectas.append(letra_elegida)

        print(f"La letra {letra_elegida} no está en la palabra.")
        print(f"La lista de letras incorrectas, es: {letras_incorrectas}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")


if vidas == 0:
    print("Perdiste")
    print(f"La palabra era: {palabra_al_azar}")

if cant_correctas == len(dict_correcto):
    #print(f"cant_correctas: {cant_correctas}")
    #print(f"dict_correcto: {dict_correcto}")
    mostrar_diccionario(dict_correcto)
    