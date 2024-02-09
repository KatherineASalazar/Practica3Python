#Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
#ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
#atributos de la clase.

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = Rectangulo(largo, ancho)
area = rectangulo.calcular_area()
print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
