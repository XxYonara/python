resp = str(input("Voçê tem mais de 25 anos ?"))
idio = str(input("Voçê fala inglês ?"))

if(idio == str("sim")):
    print("verdadeiro")
if(resp == str("sim") and idio == str("sim")):
   print("verdadeiro")
if(resp == str("sim") and idio == str("nao")):
    print("falso")
