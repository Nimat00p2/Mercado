
from mercado_2_0_pack.utilitarios import (
    sys,
    limpar_tela,
)

from mercado_2_0_pack.mostrar_produtos import mostrar_produtos
from mercado_2_0_pack.adicionar_produto import adicionar_produto
from mercado_2_0_pack.remover_produto import remover_produto
from mercado_2_0_pack.adicionar_remover_marca import adicionar_remover_marca
from mercado_2_0_pack.adicionar_remover_vendas import adicionar_remover_vendas
from mercado_2_0_pack.alterar_preco_estoque import alterar_preco_estoque

while True:
    print('\n--- Sistema de Mercado ---\n')
    opcao = input(
        '1- Adicionar Produto\n'
        '2- Remover Produto\n'
        '3- Adicionar ou Remover Marca\n'
        '4- Adicionar ou Remover Vendas\n'
        '5- Alterar Preco ou Estoque\n'
        '6- Mostrar Produtos\n'
        '7- Sair\n\n'
        'Opcão: '
    )
    limpar_tela()
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        remover_produto()
    elif opcao == '3':
        adicionar_remover_marca()
    elif opcao == '4':
        adicionar_remover_vendas()
    elif opcao == '5':
        alterar_preco_estoque()
    elif opcao == '6':
        mostrar_produtos()
    elif opcao == '7':
        sys.exit()
    else:
        print('Opção errada')
        continue
