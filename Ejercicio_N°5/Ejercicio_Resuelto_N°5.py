from Calculos_N5 import Operaciones

class EjercicioN5:
    @staticmethod
    def ejecutar():
        try:
            suma = float(input("Ingrese el valor inicial de Suma: "))
            x = float(input("Ingrese el valor de X: "))
            y = float(input("Ingrese el valor de Y: "))

            print(f"\n\nValores iniciales: Suma= {suma}, X= {x}, Y={y}")

            suma = Operaciones.calcular_suma(suma, x)
            x = Operaciones.calcular_x(x, y)
            suma = Operaciones.calcular_suma_div(suma, x, y)

            print(f"\nValores finales: Suma= {suma}, X= {x}, Y={y}")
            print()

        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    EjercicioN5.ejecutar()
