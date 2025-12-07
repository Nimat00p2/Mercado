
from utilitarios import *

def remover_produto():
    produto, codigo = pesquisar_codigo()
    if codigo:
        print(f'Produto {produto['nome']} removido com sucesso...')
        produtos.remove(produto)
        codigos_existentes.remove(codigo)
    return