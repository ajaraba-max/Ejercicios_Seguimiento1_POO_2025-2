from calculos import Calculos

class EjercicioN4:
    @staticmethod
    def ejecutar():
        try:
            radio = float(input("Ingrese el radio de la circunferencia: "))
            longitud = Calculos.calcular_longitud(radio)
            area = Calculos.calcular_area(radio)

            print(f"La longitud de la circunferencia es: {longitud:.2f}")
            print(f"El área del círculo es: {area:.2f}")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el radio.")

if __name__ == "__main__":
    EjercicioN4.ejecutar()
