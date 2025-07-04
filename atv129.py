import atv129fc
r = int(input("Quantos reais voçê tem na conta ?"))
m = str(input("Para qual moeda gostaria de converter ?"))

if(m == "dolar"):
    atv129fc.Dolares(r,m)
if(m == "euros"):
    atv129fc.Euros(r,m)
if(m == "iene"):
    atv129fc.Iene(r,m)
    