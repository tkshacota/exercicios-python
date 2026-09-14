idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
    produtos = 20

    while produtos > 0:
        quantos = int(input("Quantos produtos você deseja comprar? "))

        if quantos <= produtos:
            produtos -= quantos
            print(
                f"Você comprou {quantos} produtos. Restam {produtos} produtos disponíveis."
            )
        else:
            print("Desculpe, não temos produtos suficientes em estoque.")
            print(f"Temos apenas {produtos} produtos disponíveis.")

        repeat = input("Deseja fazer outra compra? (s/n): ")
        if repeat.lower() != "s":
            break
        if produtos == 0:
            print("Todos os produtos foram vendidos.")
            break
else:
    print("Você é menor de idade e não pode consumir bebidas alcoólicas.")

exit()
