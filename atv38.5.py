hrs= int(input("Quantas horas trabalhadas ? "))

vlr = int(hrs * 40)

if(vlr < 1518):
    vlr = vlr -(0.075 * vlr)
    print("Voçe recebera "+str(vlr))
if(vlr >1518 and vlr < 2793):
    vlr = vlr -(0.09 * vlr)+22.75
    print("Voçe recebera "+str(vlr))
if(vlr > 2793 and vlr < 4190):
    vlr = vlr -(0.12 * vlr)+106.59
    print("Voçe recebera "+str(vlr))
if(vlr > 4190 and vlr < 8157):
    vlr = vlr -(0.14 * vlr)+190.40
    print("Voçe recebera "+str(vlr))