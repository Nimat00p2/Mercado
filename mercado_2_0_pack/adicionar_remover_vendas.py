
from utilitarios import (
    limpar_tela,
    numero_int_deci,
    pesquisar_codigo,
    formatacao_total,
)


def adicionar_remover_vendas():
    produto, codigo = pesquisar_codigo()
    if not codigo:
        return
    opcoes = {
        'remover': ('venda', 'estoque', 'Reembolso com sucesso...'),
        'vender': ('estoque', 'venda', 'Venda com sucesso...')
    }
    while True:
        formatacao_total(produto)
        opcao = input('Deseja: "remover" | "vender"\n').lower().replace(' ', '')
        limpar_tela()
        if opcao not in opcoes:
            print('Opção invalida')
            continue
        variavel_1, variavel_2, texto = opcoes[opcao]
        if produto[variavel_1] == 0:
            print(f'Sem {variavel_1}')
            return
        valor_maximo = produto[variavel_1]
        valor = numero_int_deci(int, f'quantas vendas de {produto['nome']} | {variavel_1} disponivel {produto[variavel_1]}', 'Quantidade', valor_maximo, 1)
        produto[variavel_1] -= valor
        produto[variavel_2] += valor
        print(texto)
        formatacao_total(produto)
        return
