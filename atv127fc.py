def Analisar(cargo): 
    s = int(0)
    if(cargo == "Policial" or cargo == "medico"):
     s = int(2000)
    elif(cargo == "magico" or cargo == "coach"):
       s = int(1500)
    else:
       s = int(500) 
    return s  