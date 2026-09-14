filme = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]
print("Bem-vindo ao classificador de filmes:")
print("Aqui estão os filmes disponíveis para classificação:")
print("Escolha um número de 1 a 5 para classificar o filme:")
for filme in filme:
    classificacao = int(
        input(f"como voce classifica {filme}:de 1 a 5: (ou 0 para sair) ")
    )
    if classificacao == 0:
        print("Saindo do classificador de filmes.")
        break
    while classificacao < 1 or classificacao > 5:
        print("Classificação inválida. Digite um número de 1 a 5.")
        classificacao = int(
            input(f"como voce classifica {filme}:de 1 a 5: (ou 0 para sair) ")
        )
    print(f"Você classificou {filme} com nota {classificacao}.")
print("Obrigado por usar o classificador de filmes!")
