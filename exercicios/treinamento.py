from operator import truediv

import matplotlib.pyplot as plt


class produto:
    def __init__(self, nome, preco, categoria, quantidade):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade

    def __str__(self):
        return (
            f"Nome: {self.nome}, Preco: {self.preco}, "
            f"Categoria: {self.categoria}, Quantidade: {self.quantidade}"
        )


estoque = []


def cadastrar_produto(lista, nome, preco, categoria, quantidade):
    novo_produto = produto(nome, preco, categoria, quantidade)
    lista.append(novo_produto)
    return novo_produto


def listar_produtos(lista):
    if not lista:
        print("Nao existe esse produto")
        return
    for produto in lista:
        print(f"-{produto}")


def buscar_produto(lista, produto_buscado):
    for produto in lista:
        if produto.nome.lower() == produto_buscado.lower():
            return produto
    return None


def gerar_grafico(lista):
    contagem_de_produtos = {}
    for produto in lista:
        contagem_de_produtos[produto.categoria] = (
            contagem_de_produtos.get(produto.categoria, 0) + produto.quantidade
        )

    categorias = list(contagem_de_produtos.keys())
    quantidade = list(contagem_de_produtos.values())

    plt.bar(categorias, quantidade, color="purple")
    plt.show()

while True:
    print("\nBem-vindo ao sistema do mercadinho")
    print("1 - Cadastrar um produto")
    print("2 - Listar um produtos")
    print("3 - Buscar um produto")
    print("4 - Gerar grafico")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")
