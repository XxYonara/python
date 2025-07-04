c= int(0)
n1 = int(0)
n2 = int(0)
n3 = int(0)
n4 = int(0)

while (c != 9999):
    c = c + 1
    n = int(input("Digite um numero."))
    resp = str(input("Gostaria de parar ?"))

    if(n >= 0 and n <=25):
        n1 = n1 +1
    if(n >= 26 and n <= 50):
        n2 = n2 + 1
    if(n >= 51 and n <= 75):
        n3 = n3 + 1
    if(n >=76 and n <= 100):
        n4 = n4 + 1
    if(resp == "s"):
        break

print(f"Estão entre 0-25 {n1}, entre 26-50 estão {n2}, entre 51-75 estão {n3} e entre 76-100 {n4}")
