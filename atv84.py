cont = int(0)
a = int(0)
b = int(0)
c = int(0)

while (cont != 4):
    cont = cont + 1
    v = str(input("Qual o nome do produto ?"))
    p = int(input("Qual o valor do produto ?"))

    if(p >= 1000):
        a = a + 1
    if(p >=500 and p <=999):
        b = b + 1
    if(p < 499):
        c = c + 1

print(f"{a} são clientes tipo A , {b} são clientes tipo B e {c} são clientes tipo C")


 