import os
limpa_a_tela = lambda: os.system('cls')

def tela_mostra_meus_agendamentos_pendentes_ong(ong, DbAgendamentos, DbExcedente, DbEstabelecimento):
    meusAgendamentos = []
    for agendamento in DbAgendamentos:
        if agendamento['idOng'] == ong['id'] and agendamento['status'] == 'agendado':
            meusAgendamentos.append(agendamento)
        
    if meusAgendamentos == []:
        print('Você não possui agendamentos!')
    else:
        
        for x, agendamento in enumerate(meusAgendamentos):
            idExcedente = agendamento['idExcedente']
            excedente = DbExcedente[idExcedente]
            estabelecimento = DbEstabelecimento[excedente['idEstabelecimento']]
            print('\n----------------------------------------')
            print(f"       Id do Agendamento: #{agendamento['id']}")
            print(f"Excedente:               {excedente['nome']}")
            print(f"Marcado para:            {agendamento['data']}")
            print(f"Endereço para coleta:    {estabelecimento['endereco']}")
            print(f"Tipo de coleta:          Alimento {excedente['tipo']}")
            print(f"Status agendamento:      {agendamento['status']}")
            print(f"Quantidade de alimento:  {excedente['qtdGramas']} gramas")
            print(f"Descricao:               {excedente['descricao']}")
            print('----------------------------------------')
            print()

def tela_mostra_meus_agendamentos_efetuados_ong(ong, DbAgendamentos, DbExcedente, DbEstabelecimento):
    meusAgendamentos = []
    for agendamento in DbAgendamentos:
        if agendamento['idOng'] == ong['id'] and agendamento['status'] == 'efetuado':
            meusAgendamentos.append(agendamento)
        
    if meusAgendamentos == []:
        print('Você não possui agendamentos efetuados!')
    else:
        
        for x, agendamento in enumerate(meusAgendamentos):
            idExcedente = agendamento['idExcedente']
            excedente = DbExcedente[idExcedente]
            estabelecimento = DbEstabelecimento[excedente['idEstabelecimento']]
            print('\n----------------------------------------')
            print(f"       Id do Agendamento: #{agendamento['id']}")
            print(f"Excedente:               {excedente['nome']}")
            print(f"Marcado para:            {agendamento['data']}")
            print(f"Endereço para coleta:    {estabelecimento['endereco']}")
            print(f"Tipo de coleta:          Alimento {excedente['tipo']}")
            print(f"Status agendamento:      {agendamento['status']}")
            print(f"Quantidade de alimento:  {excedente['qtdGramas']} gramas")
            print(f"Descricao:               {excedente['descricao']}")
            print('----------------------------------------')
            print()

def tela_menu_agendamentos():
    print('==========================')
    print('||   MEUS AGENDAMENTOS  ||')
    print('==========================')
    print('1. Cancelar Agendamento')
    print('0. Voltar')
            
def fluxo_cancela_agendamento(dbAgendamentos, usuario, DbExcedentes):
    while True:

        agendamentoId = int(input('Informe qual agendamento deseja cancelar: '))
        if agendamentoId < 0 or agendamentoId > len(dbAgendamentos):
            limpa_a_tela()
            print('Opção inválida, tente novamente!')
            break
        else:
            agendamento = dbAgendamentos[agendamentoId] 
            if agendamento['idOng'] != usuario['id'] and agendamento['idEstabelecimento'] != usuario['id']:
                limpa_a_tela()
                print('Não foi encontrado um agendamento com esse na sua lista de agendamentos!')
                break
            elif agendamento['status'] != 'agendado': 
                limpa_a_tela()
                print('O agendamento informado já foi cancelado ou efetuado, tente novamente!')
                break
            else:
                    agendamento['status'] = 'cancelado'
                    DbExcedentes[agendamento['idExcedente']]['status'] = 'disponivel'
                    dbAgendamentos[agendamento['id']] = agendamento
                    limpa_a_tela()
                    print('Agendamento cancelado com sucesso!')
                    break

def tela_mostra_meus_agendamentos_pendentes_estabelecimento(estabelecmento, DbAgendamentos, DbExcedente, DbOngs):
    meusAgendamentos = []
    limpa_a_tela()
    for agendamento in DbAgendamentos:
        idExcedente = agendamento['idExcedente']
        excedente = DbExcedente[idExcedente]
        if excedente['idEstabelecimento'] == estabelecmento['id'] and agendamento['status'] == 'agendado':
            meusAgendamentos.append(agendamento)
    if meusAgendamentos == []:
        print('Você não possui agendamentos!')
    else:
        
        for agendamento in meusAgendamentos:
            idExcedente = agendamento['idExcedente']
            excedente = DbExcedente[idExcedente]
            ong = DbOngs[agendamento['idOng']]
            print('\n----------------------------------------')
            print(f"       Id do Agendamento: #{agendamento['id']}")
            print(f"Excedente             :               {excedente['nome']}")
            print(f"Marcado para          :  {agendamento['data']}")
            print(f"Ong Responsável       :  {ong['nome']}")
            print(f"Tipo de coleta        :  {excedente['tipo']}")
            print(f"Status agendamento    :  {agendamento['status']}")
            print(f"Quantidade de alimento:  {excedente['qtdGramas']} gramas")
            print(f"Descricao             :  {excedente['descricao']}")
            print('----------------------------------------')
            print()

def tela_mostra_meus_agendamentos_efetuados_ong(ong, DbAgendamentos, DbExcedente, DbEstabelecimento):
    limpa_a_tela()
    meusAgendamentos = []
    for agendamento in DbAgendamentos:
        if agendamento['idOng'] == ong['id'] and agendamento['status'] == 'efetuado':
            meusAgendamentos.append(agendamento)
        
    if meusAgendamentos == []:
        print('Você não possui agendamentos completados!')
    else:
        
        for x, agendamento in enumerate(meusAgendamentos):
            idExcedente = agendamento['idExcedente']
            excedente = DbExcedente[idExcedente]
            estabelecimento = DbEstabelecimento[excedente['idEstabelecimento']]
            print('\n----------------------------------------')
            print(f"       Id do Agendamento: #{agendamento['id']}")
            print(f"Excedente:               {excedente['nome']}")
            print(f"Marcado para:            {agendamento['data']}")
            print(f"Endereço para coleta:    {estabelecimento['endereco']}")
            print(f"Tipo de coleta:          Alimento {excedente['tipo']}")
            print(f"Status agendamento:      {agendamento['status']}")
            print(f"Quantidade de alimento:  {excedente['qtdGramas']} gramas")
            print(f"Descricao:               {excedente['descricao']}")
            print('----------------------------------------')
            print()
