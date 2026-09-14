def calcular_media(notas):
    return sum(notas) / len(notas)  # funcao para calcular a media das notas


nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")  # input do nome do usuario e print de boas vindas

notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)  # lista para armazenar as notas do usuario

resultado = calcular_media(notas)
print(f"Sua média é: {resultado:.2f}")
print(f"Notas: {notas}")
print(
    f"situacao: {'Aprovado' if resultado >= 7 else 'Reprovado'}"
)  # calculo da media e print do resultado, notas e situacao do usuario
if resultado >= 7:
    print("Parabéns! Você foi aprovado.")
else:
    print(
        "Infelizmente, você foi reprovado."
    )  # resultado final com mensagem de aprovacao ou reprovacao
