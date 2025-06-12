p1 = int(input("Qual sua idade ?"))
p2 = int(input("Qual sua idade ?"))

if(p1 <= 9):
    print("mirim")
if(p2 <= 9):
    print("mirim")
if(p1 >= 10 and p1 <= 14):
    print("Infantil")
if(p2 >= 10 and p2 <= 14):
    print("Infantil")
if(p1 >= 15 and p1 <= 18):
    print("jovem")
if(p2 >= 15 and p2 <= 18):
    print("jovem")
if(p1 >= 19 and p1 <=24):
    print("adulto")
if(p2 >= 19 and p2 <=24):
    print("adulto")
elif(p1 == p2):
    resp = str(input("Qual será o horário da luta?"))
    print("Está marcado a luta de uma pessoa com "+str(p1)+" anos e outra com "+str(p2)+" anos as "+str(resp)+" horas")
else:
    print("luta cancelada")

