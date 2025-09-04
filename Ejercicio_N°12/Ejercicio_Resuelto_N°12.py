from calculos import Calculos

class EjercicioN12:
    @staticmethod
    def ejecutar():
        try:
            horas_trabajadas = int(input("Ingresa cuántas horas trabajaste: "))
            
            salario_bruto = Calculos.calcular_salario_bruto(horas_trabajadas)
            retencion = Calculos.calcular_retencion(salario_bruto)
            salario_neto = Calculos.calcular_salario_neto(salario_bruto, retencion)

            print(f"Salario Bruto: {salario_bruto}")
            print(f"Retención: {retencion}")
            print(f"Sueldo Neto: {salario_neto}")
        except ValueError:
            print("Por favor, ingrese un número entero válido para las horas trabajadas." )

if __name__ == "__main__":
    EjercicioN12.ejecutar()
