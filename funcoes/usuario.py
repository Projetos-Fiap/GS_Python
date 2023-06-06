from operator import contains
import os
limpa_a_tela = lambda: os.system('cls')

def cadastrar_ong(DbOngs):
    limpa_a_tela()
    nome = input('Digite o nome da ONG: ')
    descricao = input('Digite uma descricao: ')
    endereco = input('Digite o endereço: ')

    emailInvalido = True
    email = ''
    while emailInvalido: 
        email = input('Digite o email da ONG: ')
        for user in DbOngs:
            if user['email'] == email:
                print('Este email já está sendo usado! Tente Novamente')
            
        emailInvalido = False
        
    while True:
        senha = input('Digite o senha do usuário: ')
        confirmeSenha = input('Confirme a senha do usuário: ')
        if(senha != confirmeSenha):
            limpa_a_tela()
            print('As Senhas não conferem! Tente novamente')
        else:
            break

    user = {
        'nome':  nome,
        'email': email,
        'senha': senha,
        'descricao': descricao,
        'endereco': endereco,
        'id': len(DbOngs),
    }
    limpa_a_tela()
    print('Usuário criado com sucesso!')
    DbOngs.append(user)

def cadastrar_estabelecimento(DbEstabelecimentos):
    limpa_a_tela()
    nome = input('Digite o nome do Estabelecimento: ')
    descricao = input('Digite uma descricao: ')
    endereco = input('Digite o endereço: ')

    emailInvalido = True
    email = ''
    while emailInvalido: 
        email = input('Digite o email do usuário: ')
        for user in DbEstabelecimentos:
            if user['email'] == email:
                print('Este email já está sendo usado! Tente Novamente')
            
        emailInvalido = False
        
    while True:
        senha = input('Digite o senha do usuário: ')
        confirmeSenha = input('Confirme a senha do usuário: ')
        if(senha != confirmeSenha):
            limpa_a_tela()
            print('As Senhas não conferem! Tente novamente')
        else:
            break

    user = {
        'nome':  nome,
        'email': email,
        'senha': senha,
        'descricao': descricao,
        'endereco': endereco,
        'id': len(DbEstabelecimentos),
    }
    limpa_a_tela()
    print('Usuário criado com sucesso!')
    DbEstabelecimentos.append(user)

def fluxo_login(DbUsuarios):
    while True:
        email = input('Insira o email: ')
        senha = input('Inisra a senha: ')

        for user in DbUsuarios:
            if(user['email'] == email):
                if(user['senha'] == senha):
                    limpa_a_tela()
                    print('Logado com Sucesso!')
                    return user
                else:
                    limpa_a_tela()
                    print('Senha incorreta! Tente Novamente!')
                    break
        limpa_a_tela()
        print('Usuário não encontrado! Tente Novamente!')

def fluxo_altera_senha_ong(idUser, DbOngs):
    limpa_a_tela()
    senhaAtual = input("Informe sua senha atual: ")
    if DbOngs[idUser]['senha'] != senhaAtual:
        print('Senha incorreta!')
    else:
        novaSenha = input('Informe uma nova senha: ')
        confirmaNovaSenha = input('Confirme a nova senha: ')
        if novaSenha != confirmaNovaSenha:
            limpa_a_tela()
            print('As senhas não conferem!')
        else:
            DbOngs[idUser]['senha'] = novaSenha
            limpa_a_tela()
            print('Nova senha cadastrada!')

def fluxo_altera_senha_estabelecimento(idUser, DbEstabelecimentos):
    limpa_a_tela()
    senhaAtual = input("Informe sua senha atual: ")
    if DbEstabelecimentos[idUser]['senha'] != senhaAtual:
        print('Senha incorreta!')
    else:
        novaSenha = input('Informe uma nova senha: ')
        confirmaNovaSenha = input('Confirme a nova senha: ')
        if novaSenha != confirmaNovaSenha:
            limpa_a_tela()
            print('As senhas não conferem!')
        else:
            DbEstabelecimentos[idUser]['senha'] = novaSenha
            limpa_a_tela()
            print('Nova senha cadastrada!')

def is_ong(usuario, DbOngs):
    return usuario in DbOngs