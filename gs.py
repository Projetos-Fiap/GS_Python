import funcoes.usuario as usuario
import funcoes.ong as ong
import funcoes.agendamento as agendamento
import funcoes.estabelecimento as estabelecimento
import funcoes.excedente as excedente

import os
limpa_a_tela = lambda: os.system('cls')


usuarioCorrente = ''

estabelecimentos = [
    {
        'id': 0,
        'nome': 'PF do Tio',
        'descricao': 'Restaurante',
        'endereco': 'Rua Tesoura, 9, São Paulo',
        'email': 'pfTio@gmail.com',
        'senha': '123'
    },
    {
        'id': 1,
        'nome': 'Sorvete da Tia',
        'descricao': 'Doceria',
        'endereco': 'Rua Régua, 10, São Paulo',
        'email': 'sorveteTia@gmail.com',
        'senha': '123'
    }
]

ongs = [
    {
        'id': 0,
        'nome': 'Prato Cheio',
        'descricao': 'Ong que distribui PFs por caridade',
        'endereco': 'Rua Caneta, 3, São Paulo',
        'email': 'pratoCheio@gmail.com',
        'senha': '123'
    }
]

excedentes = [
    {
        'id': 0,
        'idEstabelecimento': 0,
        'nome': 'PFs do dia',
        'descricao': 'Arroz, feijão, batata, bisteca',
        'qtdGramas': 5000,
        'tipo': 'quente',
        'dataVencimento': '12:00-09/06/2023',
        'status': 'disponivel',
        'dataInicioRetirada': '17:00-08/06/2023',
        'dataFimRetirada': '18:00-08/06/2023'
    },
    {
        'id': 1,
        'idEstabelecimento': 1,
        'nome': 'sorvete de chocolate',
        'descricao': 'Sorvete de chocolate',
        'qtdGramas': 4000,
        'tipo': 'frio',
        'dataVencimento': '12:00-09/06/2023',
        'status': 'agendado',
        'dataInicioRetirada': '17:00-08/06/2023',
        'dataFimRetirada': '18:00-08/06/2023'
    }
]

agendamentos = [
    {
        'id': 0,
        'idExcedente': 1,
        'idOng': 0,
        'data': '17:00-08/06/2023',
        'status': 'agendado'
    }
]

def mostra_tela_inicial():
    print('==========================')
    print('||    MENU PRINCIPAL    ||')
    print('==========================')
    print('1. Login')
    print('2. Cadastro Ong')
    print('3. Cadastro Estabelecimento Doador')
    print('0. Finalizar programa')

def mostra_home_ONG():
    print('==========================')
    print('||       HOME ONG        ||')
    print('==========================')
    print(f"Usuário: {usuarioCorrente['nome']}\n")
    print('1. Editar Perfil de ONG')
    print('2. Meus Agendamentos')
    print('3. Histórico de Excedentes buscados')
    print('4. Buscar excedentes') 
    print('5. Alterar Senha')
    print('0. Logout')

def mostra_home_estabelecimento():
    print('==========================')
    print('||  HOME ESTABELECIMENTO ||')
    print('==========================')
    print(f"Usuário: {usuarioCorrente['nome']}\n")
    print('1. Editar perfil de Estabelecimento')
    print('2. Meus agendamentos')
    print('3. Meus excedentes') 
    print('4. Cadastrar Excedente')
    print('5. Minhas doações')
    print('6. Alterar Senha') 
    print('0. Logout')


while True:
    mostra_tela_inicial()
    opcaoInicial = input('Insira a opção desejada: ')
    
    match opcaoInicial:
        case "1":
            usuarios = estabelecimentos + ongs
            usuarioCorrente = usuario.fluxo_login(usuarios)
            
            if usuario.is_ong(usuarioCorrente, ongs):
                while True:
                    # ong        
                    mostra_home_ONG()
                    opcaoLogadoOng = input('Informe a opção desejada: ')
                    match opcaoLogadoOng:
                        case "1":   
                            ong.fluxo_editar_informacoes_ong(usuarioCorrente, ongs)
                        case "2":
                            while True:
                                agendamento.tela_mostra_meus_agendamentos_pendentes_ong(usuarioCorrente, agendamentos, excedentes, estabelecimentos)
                                agendamento.tela_menu_agendamentos()
                                opcaoAgendamentos = input('Informe a opção desejada: ')
                                match opcaoAgendamentos:
                                    case "1":
                                        agendamento.fluxo_cancela_agendamento(agendamentos, usuarioCorrente, excedentes)
                                    case "0":
                                        limpa_a_tela()
                                        break
                                    case _:
                                        limpa_a_tela()
                                        print('Opção inválida, tente novamente!')
                        case "3":
                            agendamento.tela_mostra_meus_agendamentos_efetuados_ong(usuarioCorrente, agendamentos, excedentes, estabelecimentos)
                        case "4":
                            while True:
                                excedente.lista_excedentes_disponiveis_como_ong(estabelecimentos, excedentes)
                                excedente.mostra_menu_excedentes_ong()
                                opcaoExcedente = input('Informe a opção desejada: ')
                                match opcaoExcedente:
                                    case "1":
                                        excedente.fluxo_registra_agendamento(agendamentos, excedentes, usuarioCorrente)
                                    case "0":
                                        limpa_a_tela()
                                        break
                                    case _:
                                        limpa_a_tela()
                                        print('Opção inválida, tente novamente!')
                        case "5":
                            usuario.fluxo_altera_senha_ong(usuarioCorrente['id'], ongs)
                        case "0":
                            usuarioCorrente = []
                            limpa_a_tela()
                            print('Deslogado com sucesso!')
                            break
                        case _:
                            limpa_a_tela()
                            print('Opção inválida, tente novamente!')
            else:
                    # estabelecimento
                while True:
                    mostra_home_estabelecimento()
                    opcaoLogadoEstabelcimento = input('Informe a opção desejada: ')
                    match opcaoLogadoEstabelcimento:
                        case "1":
                            estabelecimento.fluxo_editar_informacoes(usuarioCorrente, estabelecimentos)
                        case "2":
                            while True:
                                agendamento.tela_mostra_meus_agendamentos_pendentes_estabelecimento(usuarioCorrente, agendamentos, excedentes, ongs)
                                agendamento.tela_menu_agendamentos()
                                opcaoAgendamentos = input('Informe a opção desejada: ')
                                match opcaoAgendamentos:
                                    case "1":
                                        agendamento.fluxo_cancela_agendamento(agendamentos, usuarioCorrente)
                                    case "0":
                                        limpa_a_tela()
                                        break
                                    case _:
                                        limpa_a_tela()
                                        print('Opção inválida, tente novamente!')
                        case "3":
                            excedente.lista_excedentes_disponiveis_e_agendados(usuarioCorrente, excedentes)
                        case "4":
                            excedente.fluxo_cadastra_excedente(usuarioCorrente, excedentes)
                        case "5":
                            agendamento.tela_mostra_meus_agendamentos_pendentes_estabelecimento(usuarioCorrente, agendamentos, excedentes, ongs)
                        case "6":
                            usuario.fluxo_altera_senha_estabelecimento(usuarioCorrente['id'], estabelecimentos)
                        case "0":
                            usuarioCorrente = []
                            limpa_a_tela()
                            print('Deslogado com sucesso!')
                            break
                        case _:
                            limpa_a_tela()
                            print('Opção inválida! Tente novamente!')
                            break
        case "2":
            usuario.cadastrar_ong(ongs)
        case "3":    
            usuario.cadastrar_estabelecimento(estabelecimentos)
        case "0":
            print('Programa terminado!')
            break
        case _:
            limpa_a_tela()
            print('Opcao inválida! Tente novamente!')




