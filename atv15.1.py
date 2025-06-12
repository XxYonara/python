km = int(input("Qual a quantidade de km rodados no carro?"))
dias = int(input("Quantos dias ele foi alugado?"))

total = float(60 * dias) +(0.15 * km)

print("O totla a pagar no carro é "+str(total))