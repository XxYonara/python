peso = int(input("Qual seu peso?"))
qnt = int(input("Quantos sandiches voçê comeu esse mês?"))

total = float(peso+(qnt * 0.1))
gasto = int(qnt * 8.50)
print("O novo peso dessa pessoa é "+str(total)+" e o gasto durante o mês é"+str(gasto))
