from Calculos_N12 import Calculos

class EjercicioN12:
    @staticmethod
    def ejecutar():
        try:
            horas = float(input("\nIngrese el número de horas trabajadas: "))
            valor_hora = float(input("Ingrese el valor de la hora: "))
            retencion = float(input("Ingrese el porcentaje de retención (%): "))

            salario_bruto = Calculos.calcular_salario_bruto(horas, valor_hora)
            porcentaje_retencion = Calculos.calcular_porcentaje_retencion(retencion)
            valor_retencion = Calculos.calcular_valor_retencion(salario_bruto, porcentaje_retencion)
            salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion)

            print(f"\nSalario Bruto: {salario_bruto:.2f}")
            print(f"Valor de la Retención: {valor_retencion:.2f}")
            print(f"Salario Neto: {salario_neto:.2f}\n")

        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    EjercicioN12.ejecutar()
