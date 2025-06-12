tempo = int(input("Quantas tempo a viagme irá durar ?"))
veloc = int(input("Qual a velocidade que percorreu na viagem ?"))

distancia = int(tempo * veloc)
litros = int(distancia / 12)

print("A viagem demorou "+str(tempo)+" horas,percorreu em média "+str(veloc)+" km/hr, a distancia percorrida foi de "+str(distancia)+" e utilizou "+str(litros)+" litros.")