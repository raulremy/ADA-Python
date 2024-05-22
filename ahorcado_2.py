import random

print("Bienvenido al juego del ahorcado")
print("================================")

# Lista de palabras del juego
palabras_al_azar = ["almanaque", "historia", "edificio", "cuna", "reposera"]

letras_incorrectas = []

vidas = 5

intentos = 0

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
            return True
    return False

while vidas > 0 and intentos < len(palabra_al_azar):
    
    letra_elegida = pedir_letra()

    print(letra_elegida)

    if letra_en_palabra(letra_elegida, palabra_al_azar):
        print("La letra está en la palabra")
        # Idea: poblar la lista, palabra creada
        for i in range(0, len(palabra_al_azar)-1):
            if palabra_al_azar[i] == letra_elegida:
                print("1 palabra_al_azar[i]: " + palabra_al_azar[i])
                print("2 str(i): " + str(i))
                palabra_creada.append(palabra_al_azar[i])

                print("3 str(intentos): " + str(intentos))
                print("4 str(palabra_creada[intentos]): " + str(palabra_creada[intentos]))
                print("5 str(palabra_creada): " + str(palabra_creada))
            else:
                print("_", end=" ")
    else:
        letras_incorrectas.append(letra_elegida)
        print(f"La letra {letra_elegida} no está en la palabra.")
        print(f"La lista de letras incorrectas, es: {letras_incorrectas}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        
    intentos += 1
else:
    print("Perdiste")
    print(f"La palabra era: {palabra_al_azar}")
