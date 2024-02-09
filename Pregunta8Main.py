
import Pregunta8Generador_numeros

def main():
    # Generar la lista de números aleatorios
    numeros_aleatorios = Pregunta8Generador_numeros.generar_numeros_aleatorios()

    # Mostrar la lista obtenida
    Pregunta8Generador_numeros.mostrar_lista(numeros_aleatorios)

    # Ordenar y mostrar la lista ordenada
    Pregunta8Generador_numeros.ordenar_lista(numeros_aleatorios)

if __name__ == "__main__":
    main()