def perguntar():
    return   input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n" +
            "<P> - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
             "<L> - Para Listar um usuário\n"
).upper()

def salvar(dicionario):
    with open("Cap5_ep3/bd.txt", "a") as arquivo: 
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def inserir(dicionario):
    dicionario[input("Digite o Login: \n").upper()] = [input("Digite o Nome: \n").upper(),
                                                   input("Digite o última data de acesso: \n").upper(),
                                                   input("Última estação acessada: \n\n").upper()]
    salvar(dicionario)       
              
            
                                                        


