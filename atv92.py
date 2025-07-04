franc = float(1.50)
sara = float(1.10)
ano = int(0)

while (sara < franc):
    ano = ano + 1
    franc = franc + 0.02
    sara = sara + 0.03
    print(str(ano))

print(f"Demorou {ano} para Sara ficar maior que Francisco")