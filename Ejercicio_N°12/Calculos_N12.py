class Calculos:
    @staticmethod
    def calcular_salario_bruto(horas):
        return horas * 5000

    @staticmethod
    def calcular_retencion(salario_bruto):
        return salario_bruto * 0.125

    @staticmethod
    def calcular_salario_neto(salario_bruto, retencion):
        return salario_bruto - retencion
