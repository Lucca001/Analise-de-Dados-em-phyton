import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar os dados do arquivo CSV
data = pd.read_csv('dados_furacao.csv')

# Dividir os dados em features (X) e rótulos (y)
X = data.drop('furacao', axis=1)
y = data['furacao']

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar um modelo de classificação (Random Forest)
model = RandomForestClassifier()

# Treinar o modelo
model.fit(X_train, y_train)

# Prever rótulos para o conjunto de teste
y_pred = model.predict(X_test)

# Calcular a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')