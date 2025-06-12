resp =  int(input("Qual a velocidade do carro?"))
exc = int(resp -80)

if(resp <= 80):
    print("Velocidade seguro")
elif(exc >= 0 and exc <= 20 ):
    multa = ((exc *5)+150)
    print("Limite de velocidade excedida.Sua multa é "+str(multa)+"reais.")
if(exc >=21 and exc <= 80):
    multa = ((exc *10)+250)
    print("Limite de velocidade excedida.Sua multa é "+str(multa)+"reais.")
if(exc >= 81 and exc <= 200):
    multa = ((exc *20)+500)
    print("Limite de velocidade excedida.Sua multa é "+str(multa)+"reais.")
else:
    print("O veiculo será confiscado")