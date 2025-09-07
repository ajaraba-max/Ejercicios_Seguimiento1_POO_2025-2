from Calculos_N14 import Matematicas

class EjercicioN14:
    @staticmethod
    def ejecutar():
        try:
            numero = int(input("Ingresa un número para hallar su Cuadrado y su Cubo: "))
            cuadrado, cubo = Matematicas.calcular(numero)
            print(f"Cuadrado: {cuadrado}")
            print(f"Cubo: {cubo}")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    EjercicioN14.ejecutar()
