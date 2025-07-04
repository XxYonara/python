import random 
print("Bem vindo ao jogo do Crash")
s = random.randint(1,1)
vlr = int(input("Qual valor deseja apostar ?"))
soma = int(0)
print("Escolha uma alternativa para apostar")
print("[1] multiplica seu valor em 1.1")
print("[2] multiplica seu valor em 1.3")
print("[3] multiplica seu valor em 1.6")
print("[4] multiplica seu valor em 2")
print("[5] multiplica seu valor em 2.5")
r = int(input(" "))

if(r == 1):
   vlr = vlr *1.1
if(r ==2):
    vlr = vlr * 1.3
if(r == 3):
   vlr = vlr * 1.6
if(r == 4):
    vlr = vlr * 2
if(r == 5):
    vlr = vlr * 2.5

print(f"O valor atual na conta é {vlr} ")

s = random.randint(1,10)
vlr = int(input("Qual valor deseja apostar ?"))
soma = int(0)
print("Escolha uma alternativa para apostar")
print("[1] multiplica seu valor em 1.1")
print("[2] multiplica seu valor em 1.3")
print("[3] multiplica seu valor em 1.6")
print("[4] multiplica seu valor em 2")
print("[5] multiplica seu valor em 2.5")
r = int(input(" "))


match r:
    case 1 :
        if(r == 1 and s == 1 or r == 1 and s == 2 or r == 1 and s == 3 or r == 1 and s == 4  or r == 1 and s == 5 or r == 1 and s == 6 or r == 1 and s == 7 or r == 1 and s == 8 or r == 1 and s == 9):
            soma = vlr * 1.1
        else:
          vlr = 0
    case 2: 
        if(r == 1 and s == 1 or r == 1 and s == 2 or r == 1 and s == 3 or r == 1 and s == 4  or r == 1 and s == 5 or r == 1 and s == 6 or r == 1 and s == 7 or r == 1 and s == 8):
            soma = vlr * 1.3
        else:
            vlr = 0
    case 3:
        if(r == 1 and s == 1 or r == 1 and s == 2 or r == 1 and s == 3 or r == 1 and s == 4  or r == 1 and s == 5):
            soma = vlr * 1.6
        else:
            vlr = 0
    case 4:
        if(r == 1 and s == 1 or r == 1 and s == 2 or r == 1 and s == 3 or r == 1 and s == 4):
            soma = vlr * 2
        else:
            vlr = 0
    case 5:
        if(r == 1 and s == 1 or r == 1 and s == 2):
            soma = vlr * 2.5
        else:
            vlr = 0
        
print(f"O valor atual na conta é {soma} ")
