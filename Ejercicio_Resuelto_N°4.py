import math
class Calculos:
    @staticmethod
    def Calcular_Longitud_Circunferencia(Radio):
        "Calcula la longitud de una circunferencia dado su radio"
        return 2 * math.pi * Radio
    
    @staticmethod
    def Calcular_Area_Circulo(Radio):
        "Calcula el area de un circulo dado su radio"
        return math.pi * Radio ** 2
    
class Calculos:
    
    if __name__ == "__main__":
        try:
            Radio = float(input("Ingrese el radio de la circunferencia: "))
            Longitud = Calculos.Calcular_Longitud_Circunferencia(Radio)
            Area = Calculos.Calcular_Area_Circulo(Radio)
            print(f"La longitud de la circunferencia es: {Longitud:.2f}")
            print(f"El area del circulo es: {Area:.2f}")
        except ValueError:
            print("Por favor, ingrese un valor numerico valido para el radio.")