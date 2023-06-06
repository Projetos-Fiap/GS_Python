from ast import While
from datetime import datetime
import os
limpa_a_tela = lambda: os.system('cls')

def converter_data_para_string(data):
    hora = data.strftime("%H:%M")
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    
    data_string = f"{hora}-{dia}/{mes}/{ano}"
    return data_string

def converter_string_para_data(data_string):
    try:
        data = datetime.strptime(data_string, "%H:%M-%d/%m/%Y")
        return data
    except ValueError:
        print("Formato de data inválido.")
        return None

def verificar_formato_data(data_string):
    partes = data_string.split("-")
    
    if len(partes) != 2:
        return False
    
    hora_minuto = partes[0].split(":")
    dia_mes_ano = partes[1].split("/")
    
    if len(hora_minuto) != 2 or len(dia_mes_ano) != 3:
        return False
    
    hora = hora_minuto[0]
    minuto = hora_minuto[1]
    dia = dia_mes_ano[0]
    mes = dia_mes_ano[1]
    ano = dia_mes_ano[2]
    
    if not hora.isdigit() or not minuto.isdigit() or not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return False
    
    hora = int(hora)
    minuto = int(minuto)
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or dia < 1 or dia > 31 or mes < 1 or mes > 12:
        return False
    
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    
    if mes == 2:
        if dia > 29 or (dia == 29 and not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))):
            return False
    
    return True

def fluxo_cadastra_excedente(estabelecimento, DbExcedentes):
    limpa_a_tela()
    while True:
        nome = input("Insira o nome do excedente: ")
        if nome[0] == ' ' or nome == '':
            print('O nome não pode ser nulo e nem começar com espaços!')
        else:
            break
    
    while True:
        tipo = input("Insira o tipo de excedente (frio ou quente): ")
        if tipo != 'frio' and tipo != 'quente':
            print('Valor inválido, tente novamente! ')
        else:
            break
    
    while True:
        descricao = input("Insira uma descrição para o excedente: ")
        if descricao[0] == ' 'or descricao == '':
            print('A descrição não pode ser nula e nem começar com espaços!')
        else:
            break
    
    while True:
        qtdGramas = int(input("Insira a quantidade de alimento (em gramas): "))
        if qtdGramas<=100:
            print('A quantidade mínima para doação é de 100 gramas! Tente novamente')
        else:
            break
    
    while True:
        dataDeVencimento = input("Insira uma data de vencimento para o alimento (hh:mm-dd/mm/aaaa): ")
        if not verificar_formato_data(dataDeVencimento):
            print('Data no formato inválido! Tente novamente:')
        elif converter_string_para_data(dataDeVencimento) < datetime.now():
            print('Data de vencimento não pode ser menor que a data atual')
        else:
            break
        
    while True:
        dataInicioRetirada = input("A partir de que dia e horas o excedente ficará disponível para coleta (hh:mm-dd/mm/aaaa)? ")
        if not verificar_formato_data(dataInicioRetirada):
            print('Data no formato inválido! Tente novamente:')
        elif converter_string_para_data(dataInicioRetirada) < datetime.now():
            print('Data não pode ser menor que a data atual')
        else:
            break

    while True:
        dataFimRetirada = input("Até que dia e horas o excedente ficará disponível para coleta (hh:mm-dd/mm/aaaa)? ")
        if not verificar_formato_data(dataFimRetirada):
            print('Data no formato inválido! Tente novamente:')
        elif converter_string_para_data(dataFimRetirada) < datetime.now():
            print('Data não pode ser menor que a data atual! Tente novamente')
        elif converter_string_para_data(dataFimRetirada) <= converter_string_para_data(dataInicioRetirada):
            print('Data não pode ser menor que a data a partir da qual o excedente ficará disponível para coleta! Tente novamente')
        else:
            break

    excedente = {
        'id': len(DbExcedentes),
        'idEstabelecimento': estabelecimento['id'],
        'nome': nome,
        'descricao': descricao,
        'qtdGramas': qtdGramas,
        'tipo': tipo,
        'dataVencimento': dataDeVencimento,
        'status': 'disponivel',
        'dataInicioRetirada': dataInicioRetirada,
        'dataFimRetirada': dataFimRetirada
    }

    DbExcedentes.append(excedente)
    print('Excedente cadastrado com sucesso!')

def lista_excedentes_disponiveis_e_agendados(estabelecimento, DbExcedentes):
    limpa_a_tela()
    print('===========================')
    print('||     MEUS EXCEDENTES   ||')
    print('===========================')

    excedentes = []
    for excedente in DbExcedentes:
        if excedente['idEstabelecimento'] == estabelecimento['id'] and(excedente['status'] == 'disponivel' or excedente['status'] == 'agendado'):
            excedentes.append(excedente)

    if excedentes == []:
        print("Você não possui excedentes disponíveis ou agendados cadastrados!")
    else:
        for excedente in excedentes:
            print('\n----------------------------------------')
            print(f"       Id do Excedente: #{excedente['id']}")
            print(f"Nome                   : {excedente['nome']}")
            print(f"Quantidade em gramas   : {excedente['qtdGramas']}")
            print(f"Tipo de excedente      : {excedente['tipo']}")
            print(f"Descrição              : {excedente['descricao']}")
            print(f"Data de vencimento     : {excedente['dataVencimento']}")
            print(f"Status do excedente    : {excedente['status']}")
            print(f"Intervalo de retirada  : das {excedente['dataInicioRetirada']} às {excedente['dataInicioRetirada']}")
            print('\n----------------------------------------')

def mostra_menu_excedentes_ong():
    print('==========================')
    print('||    MENU EXCEDENTES   ||')
    print('==========================')
    print('1. Agendar coleta de excedente')
    print('0. Votar')

def lista_excedentes_disponiveis_como_ong(DbEstabelecimentos, DbExcedentes):
    limpa_a_tela()
    print('==========================')
    print('||       EXCEDENTES     ||')
    print('==========================')
    excedentesDisponiveis = []
    for excedente in DbExcedentes:
        if excedente['status'] == 'disponivel':
            excedentesDisponiveis.append(excedente)
    
    if(excedentesDisponiveis == []):
        print('Não há excedentes para serem coletados perto de você!')

    else:
        for excedente in excedentesDisponiveis:
            estabelecimento = DbEstabelecimentos[excedente['idEstabelecimento']]
            print('\n----------------------------------------')
            print(f"       Id do Excedente: #{excedente['id']}")
            print(f"Nome                     : {excedente['nome']}")
            print(f"Quantidade em gramas     : {excedente['qtdGramas']}")
            print(f"Tipo de excedente        : {excedente['tipo']}")
            print(f"Descrição                : {excedente['descricao']}")
            print(f"Data de vencimento       : {excedente['dataVencimento']}")
            print(f"Status do excedente      : {excedente['status']}")
            print(f"Intervalo de retirada    : das {excedente['dataInicioRetirada']} às {excedente['dataInicioRetirada']}")
            print(f"Nome estabelecimento     : {estabelecimento['nome']}")
            print(f"Endereço estabelecimento : {estabelecimento['endereco']}")
            print('\n----------------------------------------')
            
def fluxo_registra_agendamento(DbAgendamentos, DbExcedentes, ong):
    while True:
        idExcedente = input('Informe o id do Excedente que deseja agendar uma coleta: ')
        try:
            idExcedente = int(idExcedente)
        except ValueError:
            print('Valor inválido, tente novamente!')
            continue

        if idExcedente < 0 or idExcedente >= len(DbExcedentes):
            print('Valor inválido, tente novamente!')
            continue
        else:
            excedente  = DbExcedentes[idExcedente]
            if(excedente['status'] != 'disponivel'):
                print('O excedente informado não está disponível para agendamentos, tente novamente!')
                continue
            else:
                excedente['status'] = 'agendado'
                DbExcedentes[excedente['id']] = excedente
                agendamento = {
                    'id': len(DbAgendamentos),
                    'idExcedente': excedente['id'],
                    'idOng': ong['id'],
                    'data': converter_data_para_string(datetime.now()),
                    'status': 'agendado'
                }

                DbAgendamentos.append(agendamento)
                print('Agendamento criado com sucesso!')
                break


