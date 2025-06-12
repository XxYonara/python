print("Qual série voçê viu no final de semana ?")
print("[1] Sandman")
print("[2] Wandinha")
print("[3] Game of Thrones")
print("[4] Dota")
print("[5] Dexter")
r = int(input("")) 

match  r:
    case 1:
        print("A serie escolhida foi Sandman")
    case 2:
        print("A serie escolhida foi Wandinha")
    case 3:
        print("A serie escolhida foi Game of Thrones")
    case 4:
        print("A serie escolhida foi Dota")
    case 5:
        print("A serie escolhida foi Dexter")