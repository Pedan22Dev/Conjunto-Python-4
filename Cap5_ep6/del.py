basedados = []

with open("Cap5_ep6/iris.data", "r") as arquivo:   
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)

print(float(basedados[0][0]) + float(basedados[0][0]))