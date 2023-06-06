import os
limpa_a_tela = lambda: os.system('cls')

def mostra_tela_editar_informacoes_ong(ong):
    limpa_a_tela()
    print('==========================')
    print('||     Editar Info      ||')
    print('==========================')
    print(f"1. Nome:      {ong['nome']}\n")
    print(f"2. Endereço:  {ong['endereco']}\n")
    print(f"3. Descricao: {ong['descricao']}\n")
    print(f"0. Sair do modo edição")
    print('=====================================\n')

def fluxo_editar_informacoes_ong(ong, DbOngs):
    while True:
        mostra_tela_editar_informacoes_ong(ong)
        opcaoEditarInfo = input('Qual informação deseja editar? ')

        match opcaoEditarInfo:
            case "1":
                nome = input('Informe um novo nome para a sua ong: ')
                ong['nome'] = nome
            case "2":
                endereco = input('Informe um novo endereço para a sua ong: ')
                ong['endereco'] = endereco
            case "3":
                descricao = input('Informe uma nova descrição para a sua ong: ')
                ong['descricao'] = descricao
            case "0":
                DbOngs[ong['id']] = ong
                print('Alterações salvas!')
                break
            case _:
                print('Opção inválida, tente novamente!')


