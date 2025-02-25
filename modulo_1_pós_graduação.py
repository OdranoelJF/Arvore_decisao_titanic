# -*- coding: utf-8 -*-
"""Modulo 1 Pós-Graduação.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B1DMbxq2EfUGVidNSWkZS3LOO1qAgKoz

**Pedindo para IA importar a base de dados do Titanic**
"""

# prompt: importe a base de dados do titanic

import pandas as pd

# Substitua 'titanic.csv' pelo nome correto do arquivo se necessário
try:
  df = pd.read_csv('titanic.csv')
  print("Dados do Titanic importados com sucesso!")
except FileNotFoundError:
  print("Erro: Arquivo 'titanic.csv' não encontrado. Certifique-se de que o arquivo está no mesmo diretório ou forneça o caminho correto.")
except Exception as e:
  print(f"Ocorreu um erro ao importar os dados: {e}")

"""**Pedindo pra IA gerar a base de dados em CSV para eu subir no Notebook**"""

# prompt: me de a base de dados como .csv

# Salvando o DataFrame como um arquivo CSV
try:
    df.to_csv('titanic.csv', index=False)  # index=False evita salvar o índice do DataFrame
    print("Arquivo 'titanic.csv' criado com sucesso!")
except NameError:
    print("Erro: O DataFrame 'df' não foi definido. Certifique-se de que o arquivo 'titanic.csv' foi importado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo CSV: {e}")

"""**Pedindo para IA ler os dados e armazenar em um dataframe**"""

# prompt: Leia os Dados e armazene .csv em um dataframe

import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Lê o arquivo "titanic.csv" e armazena em um DataFrame
titanic_df = pd.read_csv("titanic.csv")

# Exibe as últimas 5 linhas do DataFrame por padrao (mas pode escolher quantas linhas quer ver usando (titanic_df.tail(10)  Mostra as últimas 10 linhas))
titanic_df.tail()

"""**Pedindo para IA verificar dados nulos**"""

# prompt: verifique se a base de dados tem campos nulos, sumarizando o total de nulos em cada coluna

# Verifica a quantidade de valores nulos em cada coluna
null_counts = titanic_df.isnull().sum()

# Exibe o resumo dos valores nulos
print("Valores nulos em cada coluna:")
null_counts

"""**Pedindo para IA substituir valores nulos por media de idade dos passageiros**"""

# prompt: Substitua o valor nulo da coluna Age com a media das idades dos passageiros

# Calcula a média da idade, ignorando os valores nulos
mean_age = titanic_df['age'].mean()

# Preenche os valores nulos na coluna 'Age' com a média calculada
titanic_df['age'].fillna(mean_age, inplace=True)

# Verifica novamente a quantidade de valores nulos na coluna 'Age' para confirmar a substituição
print("\nValores nulos na coluna 'age' após a substituição:")
print(titanic_df['age'].isnull().sum())

# Exibe as primeiras linhas do DataFrame para visualizar as alterações (opcional)
print("\nPrimeiras linhas do DataFrame após a substituição:")
titanic_df.head()

"""**Pedindo para IA selecionar as features para treino**"""

# prompt: Selecionar features para treino

import pandas as pd
# Seleciona as features (colunas) relevantes para o modelo
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
X = titanic_df[features]

# Converte colunas categóricas em numéricas usando one-hot encoding
X = pd.get_dummies(X, columns=['sex', 'embarked'], drop_first=True)

# Define a variável alvo (coluna 'survived')
y = titanic_df['survived']

print(X.head())
print(y.head())

"""**Pedindo para IA dividir os dados de treino e teste**



"""

# prompt: Dividir os dados entre treino (80%) e teste (20%)

from sklearn.model_selection import train_test_split

# Divide os dados em conjuntos de treinamento e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Exibe as dimensões dos conjuntos de treinamento e teste
print("Dimensões do conjunto de treinamento (X_train):", X_train.shape)
print("Dimensões do conjunto de teste (X_test):", X_test.shape)
print("Dimensões do conjunto de treinamento (y_train):", y_train.shape)
print("Dimensões do conjunto de teste (y_test):", y_test.shape)

"""**Pedindo para IA criar uma Arvore de Decisao**"""

# prompt: Criar o modelo de Árvore de Decisão com profundidade máxima 20

from sklearn.tree import DecisionTreeClassifier

# Cria o modelo de Árvore de Decisão com profundidade máxima 20
decision_tree_model = DecisionTreeClassifier(max_depth=20, random_state=42)

"""**Treinar o Modelo**"""

# prompt: Treinar o modelo com os dados de treino

# Treina o modelo com os dados de treinamento
decision_tree_model.fit(X_train, y_train)

"""**Pedindo para IA avaliar a acuracia nos dados de Treino**"""

# prompt: Avaliar o modelo nos dados de treino

from sklearn.metrics import accuracy_score

# Faz previsões nos dados de treinamento
y_pred_train = decision_tree_model.predict(X_train)

# Calcula a acurácia do modelo nos dados de treinamento
accuracy_train = accuracy_score(y_train, y_pred_train)

# Imprime a acurácia do modelo nos dados de treinamento
print(f"Acurácia do modelo nos dados de treinamento: {accuracy_train}")

"""**Pedindo para IA avaliar a acuracia nos dados de Teste**"""

# prompt: Avaliar o modelo nos dados de teste (dados novos)

# Faz previsões nos dados de teste
y_pred_test = decision_tree_model.predict(X_test)

# Calcula a acurácia do modelo nos dados de teste
accuracy_test = accuracy_score(y_test, y_pred_test)

# Imprime a acurácia do modelo nos dados de teste
print(f"Acurácia do modelo nos dados de teste: {accuracy_test}")

"""**Pedindo para IA fazer previsoes nos dados de Teste**"""

# prompt: Fazer previsões nos dados de teste

# Faz previsões nos dados de teste
y_pred_test = decision_tree_model.predict(X_test)

# Imprime as previsões
print("Previsões nos dados de teste:")
y_pred_test

"""**Pedindo para IA calcular a acuracia manualmente usando accuracy_score**"""

# prompt: Calcular a acurácia manualmente usando accuracy_score

# Calcula a acurácia manualmente
correct_predictions = 0
for i in range(len(y_test)):
    if y_test.iloc[i] == y_pred_test[i]:
        correct_predictions += 1

manual_accuracy = correct_predictions / len(y_test)
print(f"Acurácia calculada manualmente: {manual_accuracy}")

"""**Pedindo para IA mostrar a Estrutura da Arvore de Decisao**




"""

# prompt: Exibir a estrutura da árvore de decisão

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(decision_tree_model, filled=True, feature_names=X.columns, class_names=['Not Survived', 'Survived'], rounded=True)
plt.show()