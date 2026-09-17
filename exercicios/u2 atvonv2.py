import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel

    def __str__(self):
        return (
            f"Título: {self.titulo} | Autor: {self.autor} | "
            f"Gênero: {self.genero} | Disponíveis: {self.quantidade_disponivel}"
        )


livros_cadastrados = []


def cadastrar_livro(lista, titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    lista.append(novo_livro)
    return novo_livro


def listar_livros(lista):
    if not lista:
        print("Nenhum livro cadastrado.")
        return
    for livro in lista:
        print(f"- {livro}")


def buscar_livro_por_titulo(lista, titulo_buscado):
    for livro in lista:
        if livro.titulo.lower() == titulo_buscado.lower():
            return livro
    return None


def gerar_grafico_por_genero(lista):
    contagem_generos = {}
    for livro in lista:
        contagem_generos[livro.genero] = (
            contagem_generos.get(livro.genero, 0) + livro.quantidade_disponivel
        )

    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())

    plt.bar(generos, quantidades, color="royalblue")
    plt.xlabel("Gêneros")
    plt.ylabel("Quantidade")
    plt.title("Total de livros por gênero")
    plt.tight_layout()
    plt.show()


cadastrar_livro(livros_cadastrados, "Dom Casmurro", "Machado de Assis", "Romance", 5)
cadastrar_livro(livros_cadastrados, "1984", "George Orwell", "Ficção Científica", 3)
cadastrar_livro(livros_cadastrados, "O Hobbit", "J.R.R. Tolkien", "Fantasia", 7)
cadastrar_livro(livros_cadastrados, "Sapiens", "Yuval Noah Harari", "Não-ficção", 4)
cadastrar_livro(
    livros_cadastrados, "A Menina que Roubava Livros", "Markus Zusak", "Drama", 2
)

while True:
    print("\nBem-vindo(a) à biblioteca.")
    print("1. Cadastrar um livro")
    print("2. Listar livros disponíveis")
    print("3. Buscar livro pelo título")
    print("4. Gerar gráfico de livros por gênero")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        quantidade = int(input("Quantidade disponível: "))
        cadastrar_livro(livros_cadastrados, titulo, autor, genero, quantidade)
        print("Livro cadastrado com sucesso.")

    elif opcao == "2":
        listar_livros(livros_cadastrados)

    elif opcao == "3":
        titulo_buscado = input("Digite o título do livro: ")
        resultado = buscar_livro_por_titulo(livros_cadastrados, titulo_buscado)
        if resultado:
            print(f"Encontrado: {resultado}")
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        gerar_grafico_por_genero(livros_cadastrados)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
