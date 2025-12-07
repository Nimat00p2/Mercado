
import os
import random
import sys

'''
Ideias Tiradas

em gerar codigo removi "codigo = 'PR' + codigo"

nas listas removinome_existentes = set()

'''
'''
Melhorias

em pesquisar codigo modifiquei:
for produto in produtos:
    if codigo == produto['codigo']:
        return produto, codigo
print('Produto não encontrado...')
return None, False
para generator

em numero int e deci modifiquei:
variavel = input(f'Informe {informacao}: ').replace(' ', '').replace(',', '.')
limpar_tela()
    try:
        valor = tipo(variavel)
para direto do try

em gerar codigo modiquei:
for _ in range(4): 
    codigo += str(random.randint(0, 9)) 
    if codigo in codigos_existentes: 
        continue 
    codigos_existentes.add(codigo) 
    return codigo
para um generator

reescrevi o codigo de marcas
if opcao in opcoes:
    marca_lista, marca_existe, verifica, texto = opcoes[opcao]
    nome = nome_informa(' da marca')
    if not verifica:
        if nome in marcas_existentes:
            adicionar_remover_marca(marca_lista, marca_existe, nome, texto)
            return
    if verifica:
        if nome in marcas_existentes:
            print(f'{nome} ja existe')
            return
        adicionar_remover_marca(marca_lista, marca_existe, nome, texto)
        return
    print('Marca não existe')
    continue
print('Opção invalida')
continue
para melhor leitura

em adicionar_vendas, preco_estoque, tipo_marca_categoria_nome modifiquei
coloquei no inicio if opcao not in opcoes: e removi ele do final

em mostrar produto e mostrar por marca eu modifiquei
total_tudo = 0 
for produto in produtos: 
    total = formatacao(produto) 
    total_tudo += total 
para um generator

em mostrar produto eu adicionei a opção de estoque tudo e venda

em formatacao separei o de apenas vendas e total
'''
'''
Utilitarios
'''

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

'''
Principais listas
'''

produtos = []
marcas_existentes = set()
codigos_existentes = set()
marcas = []
TIPOS = ['Caixa', 'Lata', 'Pote', 'Sache', 'Pacote', 'Unidade', 'Frasco', 'Garrafa', 'Cartela', 'Bandeja', 'Tubo']
CATEGORIAS = ['Limpeza', 'Alimento', 'Brinquedo', 'Bebida', 'Adulto', 'Frios', 'Congelado', 'Higiene', 'Utilidade']
MEDIDAS = ['Kg', 'G', 'L', 'Ml', 'Un']


'''
Remover depois
'''
marcas.append('Boa-Vista')
marcas.append('Top1')
marcas.append('Real')
marcas_existentes.add('Boa-Vista')
marcas_existentes.add('Top1')
marcas_existentes.add('Real')
codigos_existentes.add('1111')
codigos_existentes.add('2222')
codigos_existentes.add('3333')
produtos.append({'nome': 'Feijao', 'marca': 'Real', 'validade': 'Sem Validade', 'quantidade': '1_Un', 'preco': 9.88, 'estoque': 1, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 2, 'codigo': '1111'})
produtos.append({'nome': 'Arroz', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '1.0_Kg', 'preco': 8.54, 'estoque': 15, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 0, 'codigo': '2222'})
produtos.append({'nome': 'Omo', 'marca': 'Real', 'validade': 'Sem Validade', 'quantidade': '500_G', 'preco': 19.85, 'estoque': 21, 'tipo': 'Caixa', 'categoria': 'Limpeza','venda': 0, 'codigo': '3333'})
produtos.append({'nome': 'Omolux', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '500_G', 'preco': 29.55, 'estoque': 31, 'tipo': 'Caixa', 'categoria': 'Limpeza','venda': 4, 'codigo': '4444'})
produtos.append({'nome': 'Milho', 'marca': 'Real', 'validade': 'Sem Validade', 'quantidade': '2.0_Kg', 'preco': 3.67, 'estoque': 45, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 0, 'codigo': '5555'})
produtos.append({'nome': 'Milho', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '4.0_Kg', 'preco': 4.54, 'estoque': 32, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 5, 'codigo': '6666'})
produtos.append({'nome': 'Cacase', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '4.0_Kg', 'preco': 18.54, 'estoque': 75, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 0, 'codigo': '7777'})
produtos.append({'nome': 'Omo', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '9.0_Kg', 'preco': 8.04, 'estoque': 65, 'tipo': 'Pacote', 'categoria': 'Alimento','venda': 0, 'codigo': '8888'})
produtos.append({'nome': 'Cacas', 'marca': 'Top1', 'validade': 'Sem Validade', 'quantidade': '4.0_Kg', 'preco': 3.54, 'estoque': 0, 'tipo': 'Caixa', 'categoria': 'Limpeza','venda': 0, 'codigo': '9999'})


'''
Principais funções
'''

def adicionar_produto():

# Adicionar  m_t_c_m    m = marca / t = tipo / c = categoria / m = medida
    def adicionar_m_t_c_m(m_t_c_m, nome):
        while True:
            print(*m_t_c_m, sep=' | ')
            variavel = input(f'Informe {nome}: ').lower().title().replace(' ', '-')
            limpar_tela()
            if variavel in m_t_c_m:
                return variavel
            print(f'{nome.title()} inexistente...')

    def adicionar_validade():
        while True:
            validade = input('Possui validade?\nS ou N  ').title().replace(' ', '')
            limpar_tela()
            if validade == 'S':
                mes = numero_int_deci(int, 'mês da validade', 'mês da validade', 12, 1)
                ano = numero_int_deci(int, 'ano da validade', 'ano da validade', 2100, 2000)
                validade = str(mes) + '/' + str(ano)
                return validade
            elif validade == 'N':
                return 'Sem Validade'
            else:
                print('Opção invalida')
                continue

    def adicionar_quantidade():
        medida = adicionar_m_t_c_m(MEDIDAS, 'medida')
        if medida in ['Un', 'G', 'Ml']:
            tipo, valor_maior, valor_menor = int, 999, 1
        else:
            tipo, valor_maior, valor_menor = float, 999.999, 0.001
        valor = numero_int_deci(tipo, f'quantidade de {medida}', f'quantidade de {medida}', valor_maior, valor_menor)
        quantidade = str(valor) + '_' + medida
        return quantidade

    def gerar_codigo():
        while True:
            codigo = ''.join(str(random.randint(0, 9)) for _ in range(4))
            if codigo not in codigos_existentes:
                codigos_existentes.add(codigo)
                return codigo

    def criar_produto():
        return {
        'nome': nome_informa(' do produto'),
        'marca': adicionar_m_t_c_m(marcas, 'marca'),
        'validade': adicionar_validade(),
        'quantidade': adicionar_quantidade(),
        'preco': numero_int_deci(float, 'preço','preço', 999.99, 0.01),
        'estoque': numero_int_deci(int, 'estoque','estoque', 999, 0),
        'tipo': adicionar_m_t_c_m(TIPOS, 'tipo'),
        'categoria': adicionar_m_t_c_m(CATEGORIAS, 'categoria'),
        'venda': 0,
        'codigo': gerar_codigo()
        }

    novo_produto = criar_produto()
    produtos.append(novo_produto)
    print(f'{novo_produto['nome']} foi adicionado com sucesso...')

def remover_produto():
    produto, codigo = pesquisar_codigo()
    if codigo:
        print(f'Produto {produto['nome']} removido com sucesso...')
        produtos.remove(produto)
        codigos_existentes.remove(codigo)
    return

def adicionar_remover_marca():
    
    def aplicar(marca_lista, marca_existe, nome, texto):
        print(f'{nome} {texto}')
        marca_lista(nome)
        marca_existe(nome)
        return

    print(*marcas, sep=' | ')
    opcoes = {
        'remover': (marcas_existentes.remove, marcas.remove, False, 'removido com sucesso...'),
        'adicionar': (marcas_existentes.add, marcas.append, True, 'adicionado com sucesso...')
    }
    while True:
        opcao = input('\nDeseja: "remover" | "adicionar"\n').lower().replace(' ', '')
        limpar_tela()
        if opcao not in opcoes:
            print('Opção invalida')
            continue
        marca_lista, marca_existe, verifica, texto = opcoes[opcao]
        nome = nome_informa(' da marca')
        existe = nome in marcas_existentes
        if verifica and existe:
            print(f'{nome} já existe...')
            return
        if not verifica and not existe:
            print('Marca não existe...')
            return
        aplicar(marca_lista, marca_existe, nome, texto)
        return

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

'''
Sistema Principal
'''

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
