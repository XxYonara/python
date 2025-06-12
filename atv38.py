casa = int(input("Qual o valor da casa que está interessado?"))
salario = int(input("Qual é o seu sálario ?"))
meses = int(input("Em quantos meses irá parcelar?"))

porc = int(salario * 0.3)
parcela = int(casa / meses)

if(parcela > porc):
    print("Empréstimo negado")
elif(parcela < porc):
    print("APROVADO")