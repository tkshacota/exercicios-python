# ==============================================================================
# PROJETO: Classificação de Espécies de Flores Iris com TensorFlow / Keras
# DISCIPLINA: Linguagem de Programação - Unidade 4 (Aula 4 - Machine Learning)
# BIBLIOTECAS: TensorFlow, Keras, Scikit-Learn, Pandas, NumPy
# ==============================================================================

import os

# Configuração de variáveis de ambiente para suprimir logs verbosos do TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Importação das bibliotecas essenciais para manipulação de arrays e dados
import numpy as np
import pandas as pd

# Importação dos módulos do Scikit-Learn para carga de dados, particionamento e normalização
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Importação dos módulos do TensorFlow/Keras para construção da Rede Neural Artificial
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

# ------------------------------------------------------------------------------
# 1. CARGA E EXPLORAÇÃO DO CONJUNTO DE DADOS IRIS
# ------------------------------------------------------------------------------
# Carrega o dataset Iris contendo 150 amostras com 4 características botânicas cada
iris = load_iris()
x = iris.data    # Matriz com as 4 features: comp/larg de sépalas e pétalas
y = iris.target  # Vetor com as classes numéricas: 0 (Setosa), 1 (Versicolor), 2 (Virginica)

print(f"Total de amostras: {x.shape[0]} | Características por amostra: {x.shape[1]}")

# ------------------------------------------------------------------------------
# 2. PRÉ-PROCESSAMENTO, DIVISÃO E NORMALIZAÇÃO DOS DADOS
# ------------------------------------------------------------------------------
# Divide a base em 80% para treino (120 amostras) e 20% para teste (30 amostras)
# stratify=y assegura que a distribuição de cada classe seja idêntica em ambos os conjuntos
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Inicializa o normalizador z-score (média 0 e desvio padrão 1)
scaler = StandardScaler()
# Aplica o ajuste e transformação nos dados de treino
x_train = scaler.fit_transform(x_train)
# Aplica apenas a transformação nos dados de teste para evitar vazamento de dados (data leakage)
x_test = scaler.transform(x_test)

print(f"Treinamento: {x_train.shape[0]} amostras | Teste: {x_test.shape[0]} amostras")

# ------------------------------------------------------------------------------
# 3. CONSTRUÇÃO DA REDE NEURAL ARTIFICIAL (ARQUITETURA SEQUENTIAL)
# ------------------------------------------------------------------------------
model = Sequential([
    # Camada de entrada explícita recebendo os 4 atributos preditores
    Input(shape=(4,)),
    # Primeira camada oculta densa com 16 neurônios e função de ativação ReLU
    Dense(16, activation="relu"),
    # Segunda camada oculta densa com 8 neurônios e função de ativação ReLU
    Dense(8, activation="relu"),
    # Camada de saída com 3 neurônios (um para cada espécie) e ativação Softmax
    Dense(3, activation="softmax")
])

# Compilação do modelo definindo o otimizador Adam, a função de perda e a métrica de acurácia
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ------------------------------------------------------------------------------
# 4. TREINAMENTO DO MODELO COM OS DADOS DE TREINO
# ------------------------------------------------------------------------------
# Treina a rede neural ao longo de 50 épocas completas, com lotes de 8 amostras
history = model.fit(
    x_train,
    y_train,
    epochs=50,
    batch_size=8,
    verbose=0
)

# ------------------------------------------------------------------------------
# 5. AVALIAÇÃO DE DESEMPENHO NO CONJUNTO DE TESTE
# ------------------------------------------------------------------------------
# Calcula a perda e a acurácia nos dados de teste nunca antes vistos pelo modelo
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"\nAvaliação do Modelo nos Dados de Teste:")
print(f"• Perda (Loss): {loss:.4f}")
print(f"• Acurácia (Accuracy): {accuracy * 100:.2f}%")

# ------------------------------------------------------------------------------
# 6. INFERÊNCIA E COMPARAÇÃO DE PREVISÕES
# ------------------------------------------------------------------------------
# Realiza previsões probabilísticas para as primeiras 5 flores de teste
previsoes_prob = model.predict(x_test[:5], verbose=0)

# Extrai o índice da classe com a maior probabilidade predita
classes_previstas = np.argmax(previsoes_prob, axis=1)

print("\nComparação de Previsões (Primeiras 5 amostras de teste):")
nomes_flores = iris.target_names  # ['setosa', 'versicolor', 'virginica']

for i in range(5):
    real = nomes_flores[y_test[i]]
    previsto = nomes_flores[classes_previstas[i]]
    status = "OK" if real == previsto else "FALHA"
    print(f"Flor {i+1}: Real = {real:<10} | Previsto = {previsto:<10} [{status}]")