print("Bienvenido al juego del ahorcado")
print("================================")
print(" ")      
print("Elija una palabra al azar")
print("=========================")
print(" ")      

palabras_al_azar = ["almanaque", "historia", "edificio", "cuna", "reposera"]

# Elegir una palabra al azar dentro de una lista de palabras, previamente definida
def palabra_al_azar():
    palabra = int(input("Elija un número del 0 al 4: "))
    return palabras_al_azar[palabra]

def mostrar_guiones(palabra_elegida):
    for i in range(len(palabra_elegida)):
        print("_", end=" ")
    print()

def pedir_letra():
    letra = input("Ingrese una letra: ")
    if type(letra) != str:
        print("Debe ingresar una letra!")
        return pedir_letra()
    else:
        return letra
    
def validar_letra():
    letra = pedir_letra()
    if len(letra) != 1:
        print("Debe ingresar una sola letra!")
        return validar_letra()
    else:
        return letra
    
def letra_en_palabra(letra, palabra):
    for i in range(len(palabra)):
        if palabra[i] == letra:

            return True
    return False


palabra_elegida = palabra_al_azar()

mostrar_guiones(palabra_elegida)

letra_elegida = pedir_letra()

validar_letra()    

if letra_en_palabra(letra_elegida, palabra_elegida):
    print("La letra está en la palabra")
    # posicionar la letra en la palabra
    ################################
else:
    print("La letra no está en la palabra")
    # pierde una vida y la letra es erronea


