peso = int(input("Digite seu peso."))
print("[1] Mercurio")
print("[2] Venus")
print("[3] Marte")
print("[4] Jupiter")
print("[5] Saturno")
print("[6] Urano")
r = float(input(""))

match r:
    case 1:
        r = peso * 0.37
        print(str(r))
    case 2:
        r = peso * 0.88
        print(str(r))
    case 3:
        r = peso * 0.38
        print(str(r))
    case 4:
        r = peso * 2.64
        print(str(r))
    case 5:
        r = peso * 1.15
        print(str(r))
    case 6:
        r = peso * 1.17
        print(str(r))