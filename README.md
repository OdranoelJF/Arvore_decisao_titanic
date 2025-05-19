# 🚢 Titanic Decision Tree 

Este repositório contém um modelo de **Machine Learning** que utiliza uma **Árvore de Decisão** para prever a sobrevivência dos passageiros do Titanic.

## 📌 Sobre o Projeto
O projeto inclui:

### 📊 **Carregamento e Tratamento de Dados**
✔ Carrega o dataset Titanic 
✔ Trata valores nulos (`Age` com a média, remove `Embarked` nulo)  
✔ Converte variáveis categóricas em números   
✔ Seleciona as colunas que serão usadas para prever a sobrevivência  
✔ Divide os dados em treino e teste (80% / 20%)   

###  **Treinamento da Árvore de Decisão**
✔ Cria uma árvore de decisão com `max_depth=20`   
✔ Treina o modelo com os dados de treino  
✔ Calcula a acurácia do modelo nos dados de treino   

###  **Avaliação do Modelo**
✔ Avalia o modelo nos dados de teste (dados novos)   
✔ Faz previsões para os passageiros de teste   
✔ Calcula a acurácia manualmente usando `accuracy_score` 

###  **Visualização da Estrutura da Árvore**
✔ Exibe a estrutura da árvore de decisão graficamente 

---

## 🛠 Tecnologias Utilizadas
- **Python** 
- **Pandas** 
- **Scikit-Learn** 
- **Matplotlib** 
- **Seaborn** 

---

## 🚀 Como Executar

1. **Instale as Dependencias:**
   ```bash
   pip install pandas scikit-learn matplotlib seaborn

2. **Execute o script:**
   ```bash
   python nome_do_script.py

##  Resumo do Modelo 
🔹 O modelo atual traz um overfitting (97.89% no treino vs. 79.89% no teste).

##  Melhorias Futuras
🔹 Reduzir a profundidade da árvore (max_depth=5) para melhorar a generalização.
🔹 Ajustar hiperparâmetros (min_samples_split, min_samples_leaf) para evitar overfitting.
🔹 Testar outros modelos, como Random Forest ou XGBoost, para melhorar o desempenho.

##   Contribuição
Se quiser contribuir, fique à vontade para abrir um Pull Request ou sugerir melhorias. 


