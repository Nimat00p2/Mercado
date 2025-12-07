
import os
import random
import sys

# LIMPAR TERMINAL
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Feito para verifica se o numero escrito é inteiro ou decimal e retorna o resultado
def numero_int_deci(tipo, informacao, informacao_2, valor_maior, valor_menor):
    while True:
        try:
            valor = tipo(input(f'Informe {informacao}: ').replace(' ', '').replace(',', '.'))
            limpar_tela()
        except ValueError:
            print('Informe apenas numeros...')
            continue
        if valor > valor_maior or valor < valor_menor:
            print(f'{informacao_2.title()} invalido...')
            continue
        return valor

# Feitos para evitar repetição
def nome_informa(informacao):
    while True:
        nome = input(f'Informe o nome{informacao}: ').lower().title().replace(' ', '-')
        limpar_tela()
        if nome == '': 
            print('Porfavor, Informe o nome...') 
            continue 
        return nome

def pesquisar_codigo():
    codigo = str(numero_int_deci(int, 'codigo', 'codigo', 9999, 0))
    limpar_tela()
    produto = next((produto for produto in produtos if produto['codigo'] == codigo), None)
    if produto:
        return produto, codigo
    print('Produto não encontrado...')
    return None, False

def formatacao_total(produto, vendas=False, estoque=False):
    
    def formatacao(produto, total, texto):
        print(
        f'Nome:{produto['nome']}   Marca:{produto['marca']}   Validade:{produto['validade']}   Codigo:{produto['codigo']}\n'
        f'Tipo:{produto['tipo']} {produto['quantidade']}'
        f'Preço:{produto['preco']}   Estoque:{produto['estoque']}   Venda:{produto['venda']}   {texto}{total:.2f}$\n'
        f'{'-' * 100}'
        )
    
    if vendas:
        total = produto['preco'] * produto['venda']
        texto = 'Total de Vendas:'
    elif estoque:
        total = produto['preco'] * produto['estoque']
        texto = 'Total de Estoque:'
    else:
        total = (produto['preco'] * produto['estoque']) + (produto['preco'] * produto['venda'])
        texto = 'Total:'
    formatacao(produto, total, texto)
    return total


produtos = []
marcas_existentes = set()
codigos_existentes = set()
marcas = []
TIPOS = ['Caixa', 'Lata', 'Pote', 'Sache', 'Pacote', 'Unidade', 'Frasco', 'Garrafa', 'Cartela', 'Bandeja', 'Tubo']
CATEGORIAS = ['Limpeza', 'Alimento', 'Brinquedo', 'Bebida', 'Adulto', 'Frios', 'Congelado', 'Higiene', 'Utilidade']
MEDIDAS = ['Kg', 'G', 'L', 'Ml', 'Un']

