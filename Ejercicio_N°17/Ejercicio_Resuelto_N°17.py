from Calculos_N17 import Circulo

class EjercicioN17:
    @staticmethod
    def ejecutar():
        try:
            radio = float(input("\nIngresa el radio del círculo: "))
            area, circunferencia = Circulo.calcular(radio)

            print(f"\nEl Área del círculo es: {area:.2f}")
            print(f"La longitud de la circunferencia es: {circunferencia:.2f}\n")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el radio.")

if __name__ == "__main__":
    EjercicioN17.ejecutar()
