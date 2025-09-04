class Sueldo:
    @staticmethod
    def calcular(Horas):
        sueldo_bruto = Horas * 5000
        retencion = sueldo_bruto * 0.125
        sueldo_neto = sueldo_bruto - retencion
        return sueldo_bruto, retencion, sueldo_neto

    @staticmethod
    def mostrar(sueldo_bruto, retencion, sueldo_neto):
        print(f"Salario Bruto: {sueldo_bruto}")
        print(f"Retención: {retencion}")
        print(f"Sueldo Neto: {sueldo_neto}")


class EjercicioN12:
    @staticmethod
    def ejecutar():
        try:
            horas = int(input("Ingresa cuántas horas trabajaste: "))
            bruto, retencion, neto = Sueldo.calcular(horas)
            Sueldo.mostrar(bruto, retencion, neto)
        except ValueError:
            print("Por favor, ingrese un número entero válido para las horas trabajadas.")


if __name__ == "__main__":
    EjercicioN12.ejecutar()
