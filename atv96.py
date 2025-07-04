n = [3,6,12,24,48,96,192,384,768,1536]

for k in n:
    if(k == 3 or k == 6 or k == 96):
       print(f"${k}$")
    else:
        print(k)

print("-------")

n1 = [3,0,0,0,0,0,0,0,0,0]
cont = int(0)
for cont in range(9):
    n1[cont +1]= n1[cont] * 2
    if(n1[cont] == 3 or n1[cont] == 6 or n1[cont] ==96):
        print(f"${n[cont]}$")
    else:
        print(f"${n1[cont]}")
    print(n1[cont])
