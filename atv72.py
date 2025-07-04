import random
soma = int(0)
c= int(0)
derrota = int(0)

while (c != 999999):
 a = random.randint(1,9)
 resp = int(input("Digite um numero."))
 b = str(input("Gostaria de par ou impar ?"))
 print(str(a))
 soma = a + resp
 if(b == "par" and soma %2==0):
  print("Voçê ganhou")
  break
 elif(b == "impar" and soma %2==1):
   print("Ganhou")
   break
 else:
  print("voçê perdeu")
  derrota = derrota + 1

print(f"Voçê teve {derrota} derrotas")
 


