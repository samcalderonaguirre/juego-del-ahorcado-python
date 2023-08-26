# -*- coding: utf-8 -*-
import random

# Variables
categoria = 0
palabraAdivinar = ''
listaPalabraAdiv = []
listaPalabraMost = []
intentos = 5
letra = ''
run = True
listaPalabras = []
cont = 0

# Logica
print('JUEGO DEL AHORCADO\n\nSamuel Calderon Ag\n\n')
print('Categorias\n1. Nombre de peliculas\n2. Nombre de cantantes\n3. Nombres de actores\n\n')
categoria = int(input('Ingrese el numero de categoria que desea iniciar(1-2-3): '))

if categoria == 1:
    file_name = 'peliculas.txt'
    with open(file_name, 'r') as f:
        for linea in f.readlines():
            #print(linea)
            listaPalabras.insert(cont, linea)
            cont = cont + 1
    print('Ha seleccionado la categoria nombres de peliculas\n\n')

elif categoria == 2:
    file_name = 'cantantes.txt'
    with open(file_name, 'r') as f:
        for linea in f.readlines():
            #print(linea)
            listaPalabras.insert(cont, linea)
            cont = cont + 1
    print('Ha seleccionado la categoria nombres de cantantes\n\n')

elif categoria == 3:
    file_name = 'actores.txt'
    with open(file_name, 'r') as f:
        for linea in f.readlines():
            #print(linea)
            listaPalabras.insert(cont, linea)
            cont = cont + 1
    print('Ha seleccionado la categoria nombres de actores\n\n')

# Generar el numero aleatorio de la lista de palabras
longLista = len(listaPalabras)
valorAleatorio = random.randint(0, longLista - 1)

## Pedimos la palabra a adivinar
palabraL = listaPalabras[valorAleatorio]
temp = len(palabraL)

palabraAdivinar = palabraL[:temp - 1] #Elimina el ultimo caracter de un string

## Separamos la palabra en letras
listaPalabraAdiv = list(palabraAdivinar)

for item in listaPalabraAdiv:
    listaPalabraMost.append('_')

while run:
    ## Mostramos la palabra a adivinar
    print(' '.join(listaPalabraMost))

    ## Pedimos una letra
    letra = input('Dame una letra: ')

    ## Limpiar pantalla
    for num in range(100):
        print()

    ## Comprueba si se ha equivocado
    fallo = False

    if letra not in listaPalabraAdiv:
        ## Ha fallado
        fallo = True
        intentos = intentos - 1
        print('Has fallado!!!! Te quedan {intentos} intentos'.format(intentos=intentos))
    else:
        print('Has Acertado!!!!')
        ## Adivinado, sustituimos
        for key, value in enumerate(listaPalabraAdiv):
            if value == letra:
                listaPalabraMost[key] = value

    ## Comprueba si ha terminado la partida
    ### Se le acaban los intentos
    if intentos <= 0:
        run = False
        print('Has perdido, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print('Has ganado, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))