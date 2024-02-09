import Pregunta9Operaciones

def main():
    # Ejemplo de uso de las funciones del módulo operaciones
    print("Suma:", Pregunta9Operaciones.suma(10, 5))
    print("Resta:", Pregunta9Operaciones.resta(10, 5))
    print("Producto:", Pregunta9Operaciones.producto(10, 5))
    print("División:", Pregunta9Operaciones.division(10, 5))

    # Ejemplos de manejo de errores
    print("Ejemplos de manejo de errores:")
    print("Suma:", Pregunta9Operaciones.suma("10", 5))
    print("División:", Pregunta9Operaciones.division(10, 0))
    print("Producto:", Pregunta9Operaciones.producto(10, "5"))

if __name__ == "__main__":
    main()