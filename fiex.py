anual = 0.43
mensual = (0.43 / 12)

montoInicial = input("Ingresar monto: ")
xMonto = int(montoInicial)
montoAnual = int(xMonto * anual)

print("\n" + "Monto Inicial: $" + montoInicial)
print("Si se pone a 365 días: $" + str(xMonto+montoAnual)
      + "\n" + "Con una ganancia de: $" + str(montoAnual) + " por año." + "\n")

print("Si se pone a 31 días y se le agregan los intereses: ")

mes1 = (xMonto + xMonto * mensual)
print("Mes 1: " + str(mes1.__round__(2)))
mes2 = (xMonto + mes1 * mensual)
print("Mes 2: " + str(mes2.__round__(2)))
mes3 = (mes2 + mes2 * mensual)
print("Mes 3: " + str(mes3.__round__(2)))
mes4 = (mes3 + mes3 * mensual)
print("Mes 4: " + str(mes4.__round__(2)))
mes5 = (mes4 + mes4 * mensual)
print("Mes 5: " + str(mes5.__round__(2)))
mes6 = (mes5 + mes5 * mensual)
print("Mes 6: " + str(mes6.__round__(2)))
mes7 = (mes6 + mes6 * mensual)
print("Mes 7: " + str(mes7.__round__(2)))
mes8 = (mes7 + mes7 * mensual)
print("Mes 8: " + str(mes8.__round__(2)))
mes9 = (mes8 + mes8 * mensual)
print("Mes 9: " + str(mes9.__round__(2)))
mes10 = (mes9 + mes9 * mensual)
print("Mes 10: " + str(mes10.__round__(2)))
mes11 = (mes10 + mes10 * mensual)
print("Mes 11: " + str(mes11.__round__(2)))
mes12 = (mes11 + mes11 * mensual)
print("Mes 12: " + str(mes12.__round__(2)))
mes13 = (mes12 - xMonto)

print("Dejando un total al año de: $" + str(mes12.__round__(2)) + "\n"
      + "Que sería una ganancia de: $" + str(mes13.__round__(2)) + "\n")

print("Poniendo $" + str(xMonto) + " a 365 te da: $" + str(montoAnual))
print("Poniendo $" + str(xMonto) + " a 31 días y renovando con intereses te da: $" + str(mes13.__round__(2)))










