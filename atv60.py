com = int(input("Em quanto voçê quer contar ?"))

c = int(0)

while (c <= com):
    c = c + 1
    print(" {} --".format(c),end="")
    if(c%3==0):
        print("PIN \n")