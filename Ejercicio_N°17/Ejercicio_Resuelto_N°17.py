from calculos import Circulo

class EjercicioN17:
    @staticmethod
    def ejecutar():
        try:
            radio = float(input("Ingresa el radio del círculo: ") )
            area, circunferencia = Circulo.calcular(radio)

            print(f"El Área del círculo es: {area:.2f}")
            print(f"La Circunferencia es: {circunferencia:.2f}")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el radio.")

if __name__ == "__main__":
    EjercicioN17.ejecutar()
