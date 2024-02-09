#Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
#“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2


radio = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio)
area = circulo.calcular_area()
print(f"El área del círculo con radio {radio} es: {area}")