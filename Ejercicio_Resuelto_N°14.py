class CuadradoYCubo:
    @staticmethod
    def calcular(numero):
        cuadrado = numero ** 2
        cubo = numero ** 3
        return cuadrado, cubo

    @staticmethod
    def mostrar(cuadrado, cubo):
        print(f"Cuadrado: {cuadrado}")
        print(f"Cubo: {cubo}")


class EjercicioN14:
    @staticmethod
    def ejecutar():
        try:
            numero = int(input("Ingresa un número para hallar su Cuadrado y su Cubo: "))
            cuadrado, cubo = CuadradoYCubo.calcular(numero)
            CuadradoYCubo.mostrar(cuadrado, cubo)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


if __name__ == "__main__":
    EjercicioN14.ejecutar()
