resp = int(input("Digite um número."))

if(resp < 0):
    print("negativo não conta")
if(resp == 0):
    print("é zero")
elif(resp%2==0):
    print("é par")
if(resp%2==1):
    print("é impar")