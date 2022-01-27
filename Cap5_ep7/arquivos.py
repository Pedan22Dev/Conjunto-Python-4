import json

#with open("Cap5_ep7/bd.json", "r") as arq_json:
   # dic = json.load(arq_json)
    #for chave, dados in dic.items():
     #   print(chave + " || " + str(dados))

dicionario = {
    "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO": ["QUICO DAS FLORES", "24/04/2017", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_03"]
}

with open("Cap5_ep7/bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)