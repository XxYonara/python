resp = int(input("Digite seu sálario."))
ferias = float(resp * 1.33)
bonus = float(resp * 0.74)
promocao = float(resp * 1.45)

print("Baseado no seu sálario suas férias seriam "+str(ferias)+", seu bônus seria "+str(bonus)+" e caso você fosse promovida seria"+str(promocao)+".")