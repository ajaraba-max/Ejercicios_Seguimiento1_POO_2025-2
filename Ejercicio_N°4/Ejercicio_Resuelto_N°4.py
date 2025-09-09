from Calculos_N4 import Calculos

class EjercicioN4:
    @staticmethod
    def ejecutar():
        try:
            edad_juan = int(input("Ingrese la edad de Juan: "))

            edad_alberto = Calculos.calcular_alberto(edad_juan)
            edad_ana = Calculos.calcular_ana(edad_juan)
            edad_mama = Calculos.calcular_mama(edad_juan, edad_alberto, edad_ana)

            print()
            print(f"Edad de Juan: {edad_juan}")
            print(f"Edad de Alberto: {edad_alberto}")
            print(f"Edad de Ana: {edad_ana}")
            print(f"Edad de Mamá: {edad_mama}")

        except ValueError:
            print("Por favor, ingrese un número entero válido para la edad.")

if __name__ == "__main__":
    EjercicioN4.ejecutar()
