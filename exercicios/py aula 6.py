import numpy as np

participantes = [
    {
        "nome": "Alice",
        "localizacao": "Brasil",
        "afiliacao": "Universidade A",
        "interesses": ["Inteligência Artificial", "Aprendizado de Máquina"],
    },
    {
        "nome": "Bob",
        "localizacao": "Eua",
        "afiliacao": "Universidade B",
        "interesses": ["Computação Gráfica", "Aprendizado de Máquina"],
    },
    {
        "nome": "Charlie",
        "localizacao": "Canadá",
        "afiliacao": "Universidade C",
        "interesses": ["Ciência da Computação", "Sistemas de Informação"],
    },
    {
        "nome": "Diana",
        "localizacao": "Brasil",
        "afiliacao": "Universidade A",
        "interesses": ["Inteligência Artificial", "Robótica"],
    },
    {
        "nome": "Eve",
        "localizacao": "Eua",
        "afiliacao": "Universidade B",
        "interesses": ["Segurança da Informação", "Criptografia"],
    },
]

participantes_regiao = set()
for participante in participantes:
    participantes_regiao.add(participante["localizacao"])


print(f"Regiões representadas: {', '.join(participantes_regiao)}")

afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

for afiliacao, nomes in afiliacoes.items():
    print(f"Afiliação: {afiliacao}")
    for nome in nomes:
        print(f"  - {nome}")

areas_de_interesse = np.array(
    [
        interesse
        for participante in participantes
        for interesse in participante["interesses"]
    ]
)
interesses_unicos, contagem_interesses = np.unique(
    areas_de_interesse, return_counts=True
)
area_mais_popular = interesses_unicos[np.argmax(contagem_interesses)]
print(f"Área de interesse mais popular: {area_mais_popular}")
