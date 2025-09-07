import math

class Circulo:
    @staticmethod
    def calcular(radio):
        area = math.pi * (radio ** 2)
        circunferencia = 2 * math.pi * radio
        return area, circunferencia
