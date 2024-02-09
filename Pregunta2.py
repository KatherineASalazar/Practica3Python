#Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
#la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
#calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
#cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
#formato. (Los métodos de cadena le serán de utilidad)

def obtener_calificaciones():
    while True:
        calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_list = calificaciones_str.split(',')
        calificaciones_enteros = []

        try:
            for calificacion_str in calificaciones_list:
                calificacion_entero = int(calificacion_str.strip())  # Eliminar espacios en blanco y convertir a entero
                calificaciones_enteros.append(calificacion_entero)

            return calificaciones_enteros

        except ValueError:
            print("Error: Por favor, asegúrese de ingresar solo números enteros separados por comas.")


def main():
    calificaciones = obtener_calificaciones()
    print("Las calificaciones ingresadas son:", calificaciones)


if __name__ == "__main__":
    main()