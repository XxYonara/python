c = int(0)
total = int(0)

n = int(input("Qual tabuada gostaria de ver ?"))
while (c != 10):
    
    if(n < 0):
        break
    c = c + 1
    total = n * c
    print(f"{total} ")