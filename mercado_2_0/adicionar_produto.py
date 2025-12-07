
from utilitarios import (
    random,
    limpar_tela,
    numero_int_deci,
    nome_informa,
    produtos,
    codigos_existentes,
    marcas,
    TIPOS,
    CATEGORIAS,
    MEDIDAS,
)

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

