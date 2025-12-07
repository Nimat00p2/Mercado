
from mercado_2_0_pack.utilitarios import (
    limpar_tela,
    numero_int_deci,
    pesquisar_codigo,
    formatacao_total,
)


def alterar_preco_estoque():

    def preco_estoque():
        opcoes = {
                'preco': (float, 'preço', 999.99, 0.01),
                'estoque': (int,   'estoque', 999,     0)
            }
        while True:
            opcao = input('Estoque | Preco\nIrforme o que deseja alterar: ').lower().replace(' ', '')
            limpar_tela()
            if opcao not in opcoes:
                print('Opção invalida')
                continue
            tipo, nome, valor_maior, valor_menor = opcoes[opcao]
            valor = numero_int_deci(tipo, nome, nome, valor_maior, valor_menor)
            return valor, opcao

    produto, codigo = pesquisar_codigo()
    if codigo:
        formatacao_total(produto)
        valor, opcao = preco_estoque()
        produto[opcao] = valor
        print(f'{opcao.title()} de {produto['nome']} foi alterado com sucesso...')

    return
