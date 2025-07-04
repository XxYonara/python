c = int(0)
somap = int(0)
contp = int(0)
mediap = int(0)
contn = int(0)

while (c != 9999):
    c = c + 1
    n = int(input("Digite um número."))
    pare = str(input("Gostaria de parar ?"))
    
    if(n > 0):
        somap = somap + n
        contp = contp + 1
        mediap = somap / contp
    if(n < 0):
        contn = contn + 1
    if(pare =="sim"):
        break
print(f"A media dos valores positivos é {mediap}, a soma dos valores é {somap} e a quantidade dos negtivos é {contn}")
