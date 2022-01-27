arquivo = open("Cap5_ep1/firstMethod.txt", "w")

arquivo.write("Um pouco mais verbal, mas mais direto ao ponto.")

arquivo.close()

######ou######

with open("Cap5_ep1/secondMethod.txt", "w") as arquivo:
    arquivo.write("Pode ser desse jeito também, mais direto ao ponto mas deixa coisas inferidas")
