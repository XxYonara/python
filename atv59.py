n = int(input("Qual número gostaria de começar?"))
lim = int(input("Qual o limite da contagem ?"))
pulo = int(input("Em quanto em quanto irá pular ?"))

c = int(n)

while (c < lim):
    c = c + pulo
    print(str(c))