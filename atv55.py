print("Qual seu conhecimento no Excel?")
print("1] Básico")
print("[2] Intermediario")
print("[3] Avançado")
b = int(input(""))

match b:
    case 1:
        b = int(input("Para que serve [1] soma,[2] média, [3] maximo"))
        if(b ==1):
            print("A soma é pra somar")
        if(b == 2):
            print("A media é pra calcular a média.")
        if(b == 3):
            print("O maximo é pra calcular o maximo")
    case 2:
        b = int(input("Para que serve [1]se, [2]somas, [3]cont.se"))
        if(b == 1):
            print("Para realizar comparações lógicas entre um valor e um resultado esperado")
        if(b == 2):
            print("Para somar valores com base em um critério específico")
        if(b == 3):
            print("serve para contar o número de células em um intervalo que atendem a um critério específico")
    case 3:
        b = int(input("Para que serve as formulas [1]ordem.eq ,[2]procv, [3]proch"))
        if(b == 1):
            print("Serve para determinar a posição de um número dentro de uma lista de números")
        if(b == 2):
            print("serve para procurar um valor em uma coluna e retornar um valor correspondente de outra coluna na mesma linha")
        if(b == 3):
            print("é utilizada para pesquisar um valor em uma linha de uma tabela ou matriz e retornar um valor na mesma coluna de uma linha especificada")    