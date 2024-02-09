#Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos para:
# 1. Display - Debe mostrar toda la información del estudiante (nombre y número de registro).
# 2. setAge - Debe asignar la edad al estudiante
# 3. setNota - Debe asignar las notas al estudiante.

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas = list(notas)

# Ejemplo de uso
alumno1 = Alumno("Juan", "2022001")
alumno1.display()
alumno1.set_edad(20)
alumno1.set_notas(85, 90, 75)
alumno1.display()