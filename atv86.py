import random
c = int(0)
derr = int(0)

while ( c != 99999):
    a = random.randint(1,10)
    print(str(a))
    resp = int(input("Adivinhe o número."))
    print(str(a))

    if(resp > a):
        print("Voçê errou tente um número maior")
        derr = derr + 1
    if(resp <  a):
        print("Voçê errou tente um número menor.")
        derr = derr + 1
    if(resp == a):
        print(f"Sucesso voçê acertou após {derr} tentativas")
        break

