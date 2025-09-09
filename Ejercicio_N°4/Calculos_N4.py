class Calculos:
    @staticmethod
    def calcular_alberto(edad_juan):
        return (2 * edad_juan) / 3

    @staticmethod
    def calcular_ana(edad_juan):
        return (4 * edad_juan) / 3

    @staticmethod
    def calcular_mama(edad_juan, edad_alberto, edad_ana):
        return edad_juan + edad_alberto + edad_ana
