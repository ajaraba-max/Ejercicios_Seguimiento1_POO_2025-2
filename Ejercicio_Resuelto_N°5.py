class Operaciones:
    @staticmethod
    def mostrar(x, y, suma):
        print(f"  {suma:<6}{x:<6}{y:>4}")

    @staticmethod
    def calcular(x, y, suma):
        suma = suma + x
        x = x + y**2
        print(f"  {suma:<6}{x:<6}{y:>4}")

        suma = suma + x / y
        print(f"  {suma:<6}")
        return x, y, suma


class EjercicioN5:
    @staticmethod
    def ejecutar():
        try:
            x = int(input("Dale un valor a X: "))
            y = int(input("Dale un valor a Y: "))
            suma = 0

            print(" SUMA    X      Y")
            Operaciones.mostrar(x, y, suma)
            Operaciones.calcular(x, y, suma)

        except ValueError:
            print("Por favor, ingrese números enteros válidos para X y Y.")


if __name__ == "__main__":
    EjercicioN5.ejecutar()
