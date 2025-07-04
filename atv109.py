import random 
s = random.randint(0,4)
print("[0] pedra")
print("[1] papel")
print("[2] tesoura")
print("[3] largato")
print("[4] Spock")
r = int(input(" "))

match r:
    case 0:
          if(r == 0 and s == 0):
            print("Pedra com pedra , empate")
          if(r == 0 and s == 1):
            print("Pedra com papel, voçê perdeu.")
          if(r == 0 and s == 2):
            print("Pedra com tesoura, pedra ganha")
          if(r == 0 and s == 3):
             print("Pedra com largato, pedra ganha")
          if(r == 0 and s == 4):
             print("Pedra com Spock, Spock vence")
    case 1:
         if(r == 1 and s == 0):
            print("Papel com pedra , papel vence")
         if(r == 1 and s == 1):
            print("Papel com papel , empate")
         if(r == 1 and s == 2):
            print("Papel com tesoura, voçê perdeu")
         if(r == 1 and s == 3):
            print("Papel com largato , largato ganha")
         if(r == 1 and s == 4):
            print("Papel com Spock, papel vence")
    case 2:
         if(r == 2 and s == 0):
            print("Tesoura com pedra , voçê perdeu")
         if(r == 2 and s == 1):
            print("Tesoura com papel , tesoura vence")
         if(r == 2 and s == 2):
            print("Tesoura com tesoura, empate")
         if(r == 3 and s == 3):
            print("tesoura com largato , tesoura vence")
         if(r == 3 and s == 4):
            print("tesoura com Spock ,Spock vence")
    case 3:
        if(r == 3 and s == 0):
           print("Largato com pedra ,pedra ganha")
        if(r == 3 and s == 1):
           print("Largato com papel, largato ganha")
        if(r == 3 and s == 2):
           print("Largato com tesoura ,tesoura vence")
        if(r == 3 and s == 3):
           print("Largato com largato , empate")
        if(r == 3 and s == 4):
           print("Largato com spock , largato vence")
    case 4:
        if(r == 4 and s == 0):
           print("Spock com pedra ,spock vence")
        if(r == 4 and s == 1):
           print("Spock com papel, papel vence")
        if(r == 4 and s == 2):
           print("Spock com tesoura, spock vence")
        if(r == 4 and s == 3):
           print("Spock com largato,largato vence")
        if(r == 4 and s == 4):
           print("Spock com Spock , empate")

