# aula 1

x = 10
nome = "Marcelo"
nota = 8, 5
inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(inscricao))

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"A média das notas é: {media}")

if media >= 6:
    print("Parabéns! Você foi aprovado.")
else:
    print("Infelizmente, você foi reprovado.")
