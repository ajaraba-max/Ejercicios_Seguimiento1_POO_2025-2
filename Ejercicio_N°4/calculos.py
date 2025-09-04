import math

class Calculos:
    @staticmethod
    def calcular_longitud(radio):
        return 2 * math.pi * radio

    @staticmethod
    def calcular_area(radio):
        return math.pi*(radio ** 2)
