
from mercado_2_0_pack.utilitarios import (
    pesquisar_codigo,
    produtos,
    codigos_existentes,
)

def remover_produto():
    produto, codigo = pesquisar_codigo()
    if codigo:
        print(f'Produto {produto['nome']} removido com sucesso...')
        produtos.remove(produto)
        codigos_existentes.remove(codigo)

    return
