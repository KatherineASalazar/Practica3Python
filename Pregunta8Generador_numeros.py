#Desarrollar un módulo que contenga las siguientes funciones:
#● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
#● Mostrar la lista obtenida por pantalla.
#● Ordenar los valores de la lista y mostrarla por pantalla.
#Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
#ejecutar las funciones.
#Nota: utilizar el módulo “random” para generar un número aleatorio.

import random

def generar_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista obtenida:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)


