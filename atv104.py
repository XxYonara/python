import random 
resp = int(input("Qual valor deseja apostar ?"))
sort = random.randint(0,12)
soma = int(0)
print("Escolha uma cor.")
print("[0] Verm")
print("[1] Branco") 
print("[2] Preto") 
r = int(input(""))

match r:
    case 0:
        if(r == 0 and sort == 0 or r == 0 and sort == 1 or r == 0 and sort == 2 or r == 0 and sort == 3 or r == 0 and sort == 4 or r == 0 and sort == 5 or r == 0 and sort == 6):
         soma = resp * 2
        else:
           resp = 0   
        if(r == 1 and sort == 1):
           soma = resp * 14
        else:
           resp = 0
    case 2:
        if(r == 2 and sort == 7 or r == 2 and sort == 8 or r == 2 and sort == 9 or r == 2 and sort == 10 or r == 2 and sort == 11 or r == 2 and sort == 12):
           soma = resp * 2
        else:
           resp = 0

print(f"O valor atual da conta é {soma}. ")
           
      



