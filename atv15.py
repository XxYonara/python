preco = int(input("Qual o preço do produto?"))
desct = float(input("Qual o desconto do produto?"))

desconto = float(preco-(preco *desct))

print("O produto custava "+str(preco)+" mas teve desconto de "+str(desct)+"% por isso agora está custando "+str(desconto)+" reais.")