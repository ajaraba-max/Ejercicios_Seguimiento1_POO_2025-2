class Familia:
    @staticmethod
    def calcular_edades(edad_juan):
        edad_alberto = int(edad_juan * (2/3))
        edad_ana = int(edad_juan * (4/3))
        edad_madre = edad_juan + edad_alberto + edad_ana
        return edad_madre, edad_alberto, edad_ana, edad_juan

    @staticmethod
    def mostrar_edades(edad_madre, edad_alberto, edad_ana, edad_juan):
        print("\n   LAS EDADES SON:")
        print(f"MADRE: {edad_madre}   ALBERTO: {edad_alberto}")
        print(f"ANA: {edad_ana}     JUAN: {edad_juan}")


class EjercicioN14:
    @staticmethod
    def ejecutar():
        try:
            edad_juan = int(input("Juan, ¿Cuál es tu edad? "))
            madre, alberto, ana, juan = Familia.calcular_edades(edad_juan)
            Familia.mostrar_edades(madre, alberto, ana, juan)
        except ValueError:
            print("Por favor, ingrese un número entero válido para la edad de Juan.")


if __name__ == "__main__":
    EjercicioN14.ejecutar()
