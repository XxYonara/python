def Abastecer(a,l):
    alcool = float(1.90 -(1.90 * 0.03))
    alc2 = float(1.90 -(1.90 * 0.05))
    gasolina = float(2.50 -(2.50 * 0.04))
    gas2 = float(2.50 -(2.50 * 0.06))

    if(a == "A" and l <= 20):
        soma = float(l * alcool)
        print(f"Voçê deve pagar equivalente a {soma} reais.")
    elif(a == "A" and l > 20):
        soma = float(l * alc2)
        print(f"Voçê deve pagar equivalente a {soma} reais.")
    elif(a == "G" and l <= 20):
        soma = float(l * gasolina)
        print(f"Voçê deve pagar equivalente a {soma} reais.")
    elif(a == "G" and l >= 20):
        print(f"Voçê deve pagar equivalente a {soma} reais.")




