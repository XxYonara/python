c = int(0)
mais = int(0)
homem = int(0)
mulher = int(0)

for cont in range (0,2,1):
    idade = int(input("Digite sua idade. "))
    sex = str(input("Digite seu gênero. "))

    if(idade > 10):
        mais = mais + 1
    if(sex == "h"):
        homem = homem + 1
    if(sex == "m" and idade < 20):
        mulher = mulher + 1

print(f"{mais} pessoas tem mais de 10 anos, {homem} homens foram cadastrados e {mulher} tem menos de 20 anos.")
