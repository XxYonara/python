t = ["tm1","tm2","tm3","tm4","tm5","tm6","tm7","tm8","tm9","tm10"]
cont = int(0)

print(f"{t[0]} => {t[1]} => {t[2]} => {t[3]} => {t[4]}")
print(f"{t[5]} =-= {t[6]} =-= {t[7]} =-= {t[8]} =-= {t[9]}")
print("-------")

for cont in range (0,4,1):
    print(t[cont] + "=>,",end="")

for cont in range(4,10,1):
    print(f"{t[cont]} =-= ",end="")
