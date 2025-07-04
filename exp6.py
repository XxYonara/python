#array -> vetor

#inteiro a[4] = {"joaquim","22","rua a","40"}
a = ["joaquim",22,"rua a",40]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print("----------")
#for cont in range (0,4,1) versão estendida
cont = int(0)
for cont in range (4):
    print(a[cont])
    #soma = soma + a[cont]

for k in a:
    print(k)
    #soma = soma + k

print("-------")
ze = len(a)
print(ze)

#métodos -> são rotinas que pertencem a um elemento
a.append("pedro")
print(a)
