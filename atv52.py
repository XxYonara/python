prod = int(input("Qual o preçp do produto ?"))
print("Em que época de ano estamos ?")
print("[1] Carnava")
print("[2] Ferias escolares")
print("[3] Dia das crianças")
print("[4] Black Friday")
print("[5] Natal")
r = int(input(""))

match r:
    case 1:
        r = ((prod * 1.10)+prod)
        print("O preço final nesta data é"+str(r))
    case 2:
        r = ((prod * 1.20)+prod)
        print("O preço final nesta data é"+str(r))
    case 3:
        r = ((prod * 1.05)+prod)
        print("O preço final nesta data é"+str(r))
    case 4:
        r = ((prod * 0.70)+prod)
        print("O preço final nesta data é"+str(r))
    case 5:
        r = ((prod * 0.95)+prod)
        print("O preço final nesta data é"+str(r))
