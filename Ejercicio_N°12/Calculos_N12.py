class Calculos:
    @staticmethod
    def calcular_salario_bruto(horas, valor_hora):
        return horas * valor_hora

    @staticmethod
    def calcular_porcentaje_retencion(retencion):
        return retencion / 100

    @staticmethod
    def calcular_valor_retencion(salario_bruto, porcentaje_retencion):
        return salario_bruto * porcentaje_retencion

    @staticmethod
    def calcular_salario_neto(salario_bruto, valor_retencion):
        return salario_bruto - valor_retencion
