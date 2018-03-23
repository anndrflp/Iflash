class Pessoa(object):

    def __init__(self):
        self.nome = 'Anderson'
        self.idade = 20
        print('Const. chamado com sucesso')

    def imprime(self):
        print('Ola meu nome : %s e eu tenho %d' % (self.nome, self.idade))

anderson = Pessoa()
anderson.imprime()
Pessoa()