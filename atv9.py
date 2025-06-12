resp = int(input("Qual a sua divida?"))
tempo = int(input("Qual o tempo da divida?"))
taxa = float(input("Qual a taxa de juros?"))

juros = float(resp * tempo * taxa)
total = float(resp + juros)

print("Os juros são "+str(juros)+" e o total é"+str(total))