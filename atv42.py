n1 = int(input("Qual sua primeira nota ?"))
n2 = int(input("Qual sua segunda nota ?"))
freq = float(input("Qual sua frequência ?"))

media = int((n1 + n2)/2)

if(media >= 60 and freq == 0.75):
    print("Aprovado")
if(media > 40 and media < 60):
    print("Está de recuperação")
    rec = (float(input("Qual sua nota de recuperação ?")))
    if(rec <= 69.99):
        print("Reprovado")
    else:
        print("Aprovado")
if(media < 40):
    print("Reprovado sem direito a recuperação")