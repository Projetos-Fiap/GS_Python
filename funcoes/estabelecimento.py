import os
limpa_a_tela = lambda: os.system('cls')

def mostra_tela_editar_informacoes(estabelecimento):
    limpa_a_tela()
    print('==========================')
    print('||     Editar Info      ||')
    print('==========================')
    print(f"1. Nome:      {estabelecimento['nome']}\n")
    print(f"2. Endereço:  {estabelecimento['endereco']}\n")
    print(f"3. Descricao: {estabelecimento['descricao']}\n")
    print(f"0. Sair do modo edição")
    print('=====================================\n')

def fluxo_editar_informacoes(estabelecimento, Dbestabelecimentos):
    while True:
        mostra_tela_editar_informacoes(estabelecimento)
        opcaoEditarInfo = input('Qual informação deseja editar? ')

        match opcaoEditarInfo:
            case "1":
                nome = input('Informe um novo nome para o sua estabelecimento: ')
                estabelecimento['nome'] = nome
            case "2":
                endereco = input('Informe um novo endereço para o sua estabelecimento: ')
                estabelecimento['endereco'] = endereco
            case "3":
                descricao = input('Informe uma nova descrição para o sua estabelecimento: ')
                estabelecimento['descricao'] = descricao
            case "0":
                Dbestabelecimentos[estabelecimento['id']] = estabelecimento
                print('Alterações salvas!')
                break
            case _:
                print('Opção inválida, tente novamente!')