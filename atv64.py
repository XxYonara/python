c= int(0)
maior = int(0)
menor = int(999)
jovem = str("")
velho = str("")

while (c != 3):
    c = c + 1
    nome = str(input("Digite seu nome."))
    sexo = str(input("Digite seu sexo."))
    idade = int(input("Digite sua idade."))

    if(sexo == "f" and idade < menor):
        menor = idade 
        jovem = nome
    if(sexo == "m" and idade > maior):
        maior = idade
        velho = nome

print(f" O nome da mulher mais jovem é {jovem} e do homem mais velho é {velho}")
