nome = str(input("Qual seu nome ?"))
n1 = int(input("Sua primeira nota é "))
n2 = int(input("Sua segunda nota é "))
n3= int(input("Sua terceira nota é"))
n4 = int(input("Sua quarta nota é "))

media = int((n1 +n2 + n3 + n4)/4)

if(media >= 7):
    print("O aluno "+str(nome)+" com media de "+str(media)+" está aprovado.")
elif(media < 7):
    print("O aluno "+str(nome)+" foi reprovado.")
