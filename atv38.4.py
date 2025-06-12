nome = str(input("Digite seu nome."))
idade = int(input("Digite sua idade."))

if(idade < 18):
    print(str(nome)+" é menor idade.")
elif(idade >= 18):
    print(str(nome)+" é maior de idade.")