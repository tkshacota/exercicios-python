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
    plt.xlabel("Categorias")
    plt.ylabel("Quantidade")
    plt.title("Grafico de Produtos")
    plt.tight_layout()
    plt.show()

cadastrar_produto(estoque,"Arroz 5kg", 26.90, "Alimentos", 45)
cadastrar_produto(estoque,"Feijão Preto 1kg", 7.50, "Alimentos", 30)
cadastrar_produto(estoque,"Detergente Líquido 500ml", 2.80, "Limpeza", 60)
cadastrar_produto(estoque,"Sabão em Pó 1kg", 14.90, "Limpeza", 25)
cadastrar_produto(estoque,"Suco de Laranja 1L", 8.50, "bebidas", 40)

while True:
    print("\nBem-vindo ao sistema do mercadinho")
    print("1 - Cadastrar um produto")
    print("2 - Listar um produtos")
    print("3 - Buscar um produto")
    print("4 - Gerar grafico")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    match opcao:
        case "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preco do produto: "))
            categoria = input("Digite o categoria do produto: ")
            quantidade = int(input("Digite o quantidade do produto: "))
            cadastrar_produto(estoque, nome, preco, categoria, quantidade)
            print("Produto cadastrado com sucesso!")
        case "2":
            listar_produtos(estoque)
        case "3":
            produto_buscado = input("Digite o nome do produto: ")
            resultado = buscar_produto(estoque, produto_buscado)
            if resultado:
                print(f"Produto cadastrado com sucesso: {resultado}")
            else:
                print("produto nao encontrado")
        case "4":
            gerar_grafico(estoque)
        case "5":
            break

