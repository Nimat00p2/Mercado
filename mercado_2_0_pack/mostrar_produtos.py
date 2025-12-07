
from mercado_2_0_pack.utilitarios import (
    limpar_tela,
    pesquisar_codigo,
    formatacao_total,
    produtos,
    marcas,
    TIPOS,
    CATEGORIAS,
)


def mostrar_produtos():

    def tudo_venda_estoque():
        opcoes = {
            'tudo': (None, False, False),
            'venda': (None, True, False),
            'estoque': (None, False, True)
        }
        while True:
            opcao = input('Tudo  |  Venda  |  Estoque\n').lower().replace(' ', '')
            limpar_tela()
            if opcao not in opcoes:
                print('Opção errada')
                continue
            variavel_0, variavel_1, variavel_2 = opcoes[opcao]
            return variavel_0, variavel_1, variavel_2
    
    def tipo_marca_categoria_nome():
            opcoes = {
                'tipo': TIPOS,
                'marca': marcas,
                'categoria': CATEGORIAS,
                'nome': ({produto['nome'] for produto in produtos})
            }
            while True:
                opcao = input('Tipo  |  Marca  |  Nome  |  Categoria\n').lower().replace(' ', '')
                limpar_tela()
                if opcao not in opcoes:
                    print('Opção errada')
                    continue
                tipo = opcoes[opcao]
                return tipo, opcao
    
    def mostrar_todos_tudo(variavel_1, variavel_2):
        total_tudo = sum(formatacao_total(produto, variavel_1, variavel_2) for produto in produtos)
        print(f'\nValor Total dos produtos:{total_tudo:.2f}$')
    
    def mostrar_todos_apenas(variavel_1, variavel_2):
        
        tipo, opcao = tipo_marca_categoria_nome()
        while True:
            nome = input(f'{' | '.join(tipo)}\n').lower().title().replace(' ', '-')
            limpar_tela()
            if not nome in tipo: 
                print(f'Não existe {nome}')
                continue
            total_tudo = sum(formatacao_total(produto, variavel_1, variavel_2) for produto in produtos if nome == produto[opcao])
            if total_tudo != 0: 
                print(f'\nValor Total dos produtos:{total_tudo:.2f}$')
                return
            print(f'Não possui {nome}')
            return

    def mostrar_um():
        produto, codigo = pesquisar_codigo()
        if codigo:
            formatacao_total(produto)
            return
        print('Porduto não encontrado...')
    
    while True:
        opcao = input(
            '1- Mostrar Todos os Produtos\n'
            '2- Mostrar Todos os Produtos Filtrados\n'
            '3- Mostrar um Produto\n'
            '4- Voltar\n'
        )
        if opcao == '1':
            variavel_0, variavel_1, variavel_2 = tudo_venda_estoque()
            mostrar_todos_tudo(variavel_1, variavel_2)
        elif opcao == '2':
            variavel_0, variavel_1, variavel_2 = tudo_venda_estoque()
            mostrar_todos_apenas(variavel_1, variavel_2)
        elif opcao == '3':
            mostrar_um()
        elif opcao == '4':
            return
        else:
            print('Opção errada')
            continue

