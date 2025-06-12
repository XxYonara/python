uber = int(input("Qual a distancia percorrida pelo uber ?"))

if(uber <= 200):
    tx = float(uber * 0.35)
if(uber > 200):
    tx = float(uber * 0.20)

b = str(input("O bairro de destino é perigoso ?"))

if(b == "sim" and uber <= 200):
    tx = float(uber * 0.70)
if(b == "sim" and uber > 200):
    tx = float(uber * 0.36)

print("O valor da corrida para o destino escolhido é "+str(tx)+" reais.")


