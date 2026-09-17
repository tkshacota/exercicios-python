import matplotlib.pyplot as plt

meses = [
    "Jan",
    "Fev",
    "Mar",
    "Abr",
]
vendas = [1000, 1500, 2000, 2500]
plt.bar(meses, vendas, color="blue")
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.title("Vendas por Mês")
plt.show()
