#Implemente un programa que solicite al usuario una fracción, con
#formato X/Y, donde cada uno de X e Y es un número entero, y luego
#muestra, como un porcentaje redondeado al número entero más
#cercano, donde se indicará la cantidad de combustible en el
#tanque. Se debe tener en cuenta los siguientes casos:
#- Colocar E en caso X/Y sea menor a 1% del total
#- Colocar F en caso X/Y sea mayor a 99%.
#- En otro caso, devolver el valor en porcentaje %
#También debe tomar en cuenta los siguientes casos:
#- X y Y deben ser números enteros
#- X debe ser menor o igual a Y, y Y != 0
#De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
#cualquier excepción como ValueError o ZeroDivisionError.

def obtener_porcentaje(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ValueError("El denominador no puede ser cero.")
        if x < 0 or y < 0:
            raise ValueError("Los números deben ser enteros positivos.")
        if x > y:
            raise ValueError("El numerador debe ser menor o igual al denominador.")
        
        percentage = (x / y) * 100

        if percentage < 1:
            return "E"
        elif percentage > 99:
            return "F"
        else:
            return f"{round(percentage)}%"

    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese una fracción válida.")
    except ZeroDivisionError:
        print("Error: El denominador no puede ser cero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros): ")
        result = obtener_porcentaje(fraction)
        if result:
            print("La cantidad de combustible en el tanque es:", result)
            break