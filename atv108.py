import random 
s = random.randint(0,2)
print("[0] pedra")
print("[1] papel")
print("[2] tesoura")
r = int(input(" "))

match r:
    case 0:
        if(r == 0 and s == 0):
            print("Pedra com pedra , empate")
        if(r == 0 and s == 1):
            print("Pedra com papel, voçê perdeu.")
        if(r == 0 and s == 2):
            print("Pedra com tesoura, pedra ganha")
    case 1:
        if(r == 1 and s == 0):
            print("Papel com pedra , papel vence")
        if(r == 1 and s == 1):
            print("Papel com papel , empate")
        if(r == 1 and s == 2):
            print("Papel com tesoura, voçê perdeu")
    case 2:
        if(r == 2 and s == 0):
            print("Tesoura com pedra , voçê perdeu")
        if(r == 2 and s == 1):
            print("Tesoura com papel , tesoura vence")
        if(r == 2 and s == 2):
            print("Tesoura com tesoura, empate")