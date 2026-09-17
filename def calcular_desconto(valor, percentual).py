def calcular_desconto(valor, percentual):
    """Calcula o valor final com desconto aplicado."""
    if percentual < 0 or percentual > 100:
        return None  # Retorna None se o percentual for inválido
    desconto = valor * (percentual / 100)
    return valor - desconto


def registrar_venda(produto, valor_final):
    """Registra uma venda aplicando o desconto e retornando o valor final."""
    return f">>venda registrada: {produto} - Valor final: {valor_final:.2f}"


arredondar = lambda x: round(x, 2)  # Função lambda para arredondar valores
total_vendas = 0  # Variável global para armazenar o total de vendas
total_de_vendas_por_produto = (
    {}
)  # Dicionário para armazenar a quantidade de vendas por produto
produtos_vendidos = []  # Lista para armazenar os produtos vendidos
qtd_vendas = 0  # Variável global para armazenar a quantidade de vendas
produtos_para_reabastecer = [
    "arroz",
    "feijão",
    "macarrão",
]  # Lista para armazenar produtos que precisam ser reabastecidos

while True:
    print("\n=== Sistema de Vendas ===")
    print("1. Registrar venda")
    print("2. Consultar total de vendas")
    print("3. Produtos para reabastecer")
    print("4. Fechar caixa")
    opcao = input("Escolha uma opção: ")

    if opcao == "0" or opcao == "4":
        print("fechando caixa...")
        break
    elif opcao == "1":
        produto = input("Nome do produto: ")
        valor = float(input("Valor do produto: "))
        percentual = float(input("Percentual de desconto: "))
        valor_final = calcular_desconto(valor, percentual)

        if valor_final is None:
            print("desconto inválido. O valor deve estar entre 0 e 100.")
            continue

        valor_final = arredondar(valor_final)
        total_vendas += valor_final
        qtd_vendas += 1
        total_de_vendas_por_produto[produto] = (
            total_de_vendas_por_produto.get(produto, 0) + 1
        )
        print(registrar_venda(produto, valor_final))
    elif opcao == "2":
        print(f"Total de vendas: {qtd_vendas}")
        print(f"total faturado: R${total_vendas:.2f}")
        print("Vendas por produto:")
        for produto, total in total_de_vendas_por_produto.items():
            print(f"- {produto}: {total}")
    elif opcao == "3":
        print("Produtos para reabastecer:")
        for produto in produtos_para_reabastecer:
            print(f"- {produto}")
    else:
        print("Opção inválida. Tente novamente.")
