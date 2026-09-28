def calcular_pago(monto):
    denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]

    restante = round(monto * 100)
    resultado = []

    for d in denominaciones:
        valor = round(d * 100)
        cantidad = restante // valor

        if cantidad > 0:
            resultado.append((d, cantidad))
            restante -= cantidad * valor

    return resultado, restante


monto = float(input("Monto a pagar: "))

resultado, sobrante = calcular_pago(monto)

for denominacion, cantidad in resultado:
    print(f"{cantidad} de S/ {denominacion:.2f}")

if sobrante > 0:
    print(f"No se puede completar el monto. Faltan S/ {sobrante / 100:.2f}")
