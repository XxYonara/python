import atv123fc
v = int(input("Qual o valor da venda ?"))
p = str(input("Qual a forma de pagamento ?"))

if(p == "v"):
  t = atv123fc.Avista(v)
  print(f"Sua compra de {v} ficou no valor de {t}")
if( p == "a"):
  t = atv123fc.Aprazo(v)
  print(f"Sua compra de {v} ficou no valor de {t}.")
if(p == "c"):
  t = atv123fc.Cartao(v)
  print(f"Sua compra de {v} dividido, ficou no valor de {t}")
