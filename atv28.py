resp =  int(input("Qual a velocidade do carro?"))
multa = ((resp - 80)*10 + 450)

if(resp <= 80):
    print("Velocidade seguro")
else:
    print("Limete de velocidade excedido a multa é "+str(multa)+"reais.")
