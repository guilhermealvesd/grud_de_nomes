"""
Crie um programa que tenha as opções:

- Cadastrar pessoa
- Lista pessoas cadastradas
- Pesquisar pelo nome de uma pessoa
- Ordenar a lista por ordem alfabética
- Atualizar nome
- Deletar nome da lista
- Sair do porgrama

"""
#Importando biblioteca

import os

#Criando a lista 

lista = []

#Repetição do programa (loop)

while True:

    #Exibe a lista de funcionalidades:

    print(f'{'-'*30} FUNCIONALIDADES {'-'*30}\n')

    print('Digite 1: para INSERIR uma pessoa na lista.')
    print('Digite 2: para LISTAR as pessoas cadastradas.')
    print('Digite 3: para PESQUISAR uma pessoa na lista.')
    print('Digite 4: para ORDENAR a lista em ordem alfabética.')
    print('Digite 5: para ATUALIZAR um nome da lista.')
    print('Digite 6: para DELETAR uma pessoa na lista.')
    print('Digite 7: para SAIR.\n')

    #Usuário informa a opção desejada

    op = int(input('Informe a opção desejada: '))

    #Limpa o console

    os.system('cls')

    #Função INSERIR
    match op:
        case 1:
            novo_nome = input('Digite o nome a ser inserido na lista: ')
            lista.apend(novo_nome)
            print('Nome inserido com sucesso.\n')
            continue
        case 2:
            for i in range(len(lista)):
                print(f'ID: {i + 1} - {lista[i]}')
            print('')
            continue
        case 3:
            pesquisa_nome = input('Informe o nome a ser pesquisado: ')
            quantidade = lista.count(pesquisa_nome)
            try:
                print(f'Encontrado {quantidade} vezes: {pesquisa_nome}\n')
            except:
                print(f'{pesquisa_nome} não encontrado.\n')
            continue
        case 4:
            lista.sort()
            print('Ordem alfabética realizada com sucesso.\n')
            continue
        case 5:
            id_nome = int(input('Informe o ID do nome a ser alterado: '))
            if id_nome > 0 and id_nome < len(lista):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            lista[id_nome] = input('Informe o novo nome: ')
            print(f'Nome do ID {id_nome + 1} alterado com sucesso.\n')
            continue
        case 6:
            id_nome = int(input('Informe o ID do nome a ser excluído: '))
            if id_nome > 0 and id_nome < len(lista):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            del(lista[id_nome])
            print(f'Nome deletado com sucesso.\n')
            continue
        case 7:
            break
        case _:
            print('Opção inválida. \n')
            continue