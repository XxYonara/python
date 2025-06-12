n1 = int(input("Digite mnúmero."))
n2  = int(input("Digite outro número."))
resp = str(input("Gostaria de saber qual a operação?"))

if(resp == "soma"):
    soma = int(n1 + n2)
    print("A soma de "+str(n1)+" + "+ str(n2)+" é igual a "+str(soma))
if(resp == "media"):
    media = int((n1 + n2)/2)
    print("A média de "+str(n1)+" + "+str(n2)+" é igual a "+str(media))