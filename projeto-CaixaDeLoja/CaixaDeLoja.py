
valor_compra = float(input("Valor da compra: "))
valor_pago = float(input("Valor pago pelo cliente: "))

troco = valor_pago - valor_compra

cedula20 = troco // 20     #divisao por exatamente 20
troco = troco % 20     #resto da divisao por 20

cedula10 = troco // 10
troco = troco % 10

cedula5 = troco // 5
troco = troco % 5

cedula1 = troco

print("Troco: ",valor_pago - valor_compra, "\nem: \n20,00: ", cedula20, "cedulas \n10,00: ", cedula10, " cedulas \n5,00: ", cedula5, "cedulas \n1,00: ", cedula1 ,"ceduals")
