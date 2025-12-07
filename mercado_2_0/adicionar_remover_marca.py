
from utilitarios import (
    limpar_tela,
    nome_informa,
    marcas_existentes,
    marcas,
)


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