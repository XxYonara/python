n1 = int(input("Digite um número")) 
n2 = int(input("Digite um outro número")) 
n3 = int(input("Digite um outro número"))

sm1 = int(n2 + n3)
sm2 = int(n1 + n3)
sm3 = int(n1 + n2)

if(n1 < sm1 and n2 < sm2 and n3 < sm3):
    print("É triangulo")
else:
    print("Não é triangulo")