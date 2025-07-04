import random
import atv128fc
n = [0,0,0,0]

n[0] = random.randint(0,10)
n[1] = random.randint(0,10)
n[2] = random.randint(0,10)
n[3] = random.randint(0,10)
print(n)

s = atv128fc.Analisar3(n[0],n[1],n[2],n[3])
print(f"O dobro do do terceiro é {s}")

t = atv128fc.Analisar2(n[0],n[1],n[2],n[3])
print(f"O triplo do segundo sorteio é {t}")

soma = float((s + t)* 3.14)
print(f"E a soma dos dois multiplicado por 3.14 é {soma}")