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
