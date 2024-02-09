#Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
#una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
#En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
#evitar que se quede bloqueada una funcionalidad, esto incluye:
#● En caso de que se envíen valores a las funciones que no sean números, deberá
#aparecer un mensaje que informe Error: Tipo de dato no válido.
#● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
#Error: No es posible dividir entre cero.
#Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
#importar el módulo y ejecutar las funciones.

def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except ZeroDivisionError as e:
        print(e)
    except TypeError:
        print("Error: Tipo de dato no válido.")