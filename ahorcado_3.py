import random

print("Bienvenido al juego del ahorcado")
print("================================")

# Lista de palabras del juego
palabras_al_azar = ["almanaque", "historia", "edificio", "cuna", "reposera"]

letras_incorrectas = []

dict_correcto = {}

vidas = 5

cant_correctas = 0

posicion_letra = 0

# Elegir una palabra al azar dentro de una lista de palabras, previamente definida
palabra_al_azar = random.choice(palabras_al_azar)

print(palabra_al_azar)

# Crear una lista de letras de la palabra que está siendo armada
palabra_creada = [len(palabra_al_azar)]
                  
def mostrar_guiones(palabra_al_azar):
    for i in range(len(palabra_al_azar)):
        print("_", end=" ")
    print()

mostrar_guiones(palabra_al_azar)
                  
def mostrar_diccionario(diccionario):
    for i in range(len(palabra_al_azar)):
        if i in diccionario.keys():
#            print(dict[i], end=" ")
#            print(dict.items())
            diccionario_ordenado = dict(sorted(diccionario.items()))
        else:
            print("_", end=" ")
    
    print(diccionario_ordenado )

    

def pedir_letra():
    letra = input("Ingrese una letra: ")
    if type(letra) != str:
        print("Debe ingresar una letra!")
        return pedir_letra()
    else:
        return letra
def letra_en_palabra(letra, palabra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            global cant_correctas
            cant_correctas += 1
            return True
    return False

while vidas > 0 and cant_correctas < len(palabra_al_azar):
    
    letra_elegida = pedir_letra()

    print(letra_elegida)

    if letra_en_palabra(letra_elegida, palabra_al_azar):
        print("La letra está en la palabra")
        # Idea: poblar la lista, palabra creada
        for i in range(0, len(palabra_al_azar)-1):
            if palabra_al_azar[i] == letra_elegida:

                dict_correcto.update({i: letra_elegida})

                print("3 dict_correcto: " + str(dict_correcto))

                mostrar_diccionario(dict_correcto)
            else:
                print("_", end=" ")
    else:
        letras_incorrectas.append(letra_elegida)

        print(f"La letra {letra_elegida} no está en la palabra.")
        print(f"La lista de letras incorrectas, es: {letras_incorrectas}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
else:
    print("Perdiste")
    print(f"La palabra era: {palabra_al_azar}")

if vidas > 0 and cant_correctas == len(palabra_al_azar):
    print(f"Ganaste! La palabra es: {palabra_al_azar}")
