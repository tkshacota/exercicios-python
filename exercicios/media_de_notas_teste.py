notas = [7.5, 8.0, 6.5, 9.0, 7.0]


def calcular_media(notas):
    return sum(notas) / len(notas)


media = calcular_media(notas)
arredondar_media = lambda valor: round(valor, 2)
media_arredondada = arredondar_media(media)
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"
print("Notas:", notas)
print("Média arredondada:", media_arredondada)
print("Situação:", situacao)
