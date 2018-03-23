import Pessoa

def menuprincipal():

    print('Navegue pelo menu:' )
    print('1 - Gerar ordem de serviço ')
    print('2 - Cadastrar pessoa')

    navegacao = int(input())

    if navegacao == 1:
        print('Sair')
    else:

        pp = Pessoa()
        pp.idade = 20
        print(pp.idade)

menuprincipal()


