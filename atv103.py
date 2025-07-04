import random 
conta = int(input("Qual valor voçê tem em conta ?"))
resp = int(input("Qual valor deseja apostar ?"))
sort = random.randint(0,2)
soma = int(0)
print("Escolha uma cor.")
print("[0] Verm")
print("[1] Preto") 
print("[2] Branco") 
r = int(input(""))

match r :
    case 0:
        if(sort == 0 and r == 0):
            resp = resp * 2
            soma = resp + conta
        else:
            resp = 0
    case 1:
        if(sort == 1 and r ==1):
            resp = resp *2 
            soma = resp + conta
        else:
            resp = 0
    case 2:
        if(sort == 2 and r == 2):
            resp = resp * 14
            soma = resp + conta
        else:
            resp = 0

print(f"O valor atual da conta é {soma}. ")
