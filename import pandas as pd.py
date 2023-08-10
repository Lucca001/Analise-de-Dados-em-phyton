import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('dados_meteorologicos.csv')

# Calcular a média de umidade
media_umidade = data['umidade'].mean()

# Definir um limiar de umidade para indicar possível chuva
limiar_umidade_chuva = 70  # Valor pode ser ajustado conforme necessário

# Verificar se a média de umidade está acima do limiar
if media_umidade > limiar_umidade_chuva:
    print("Há uma tendência de chuva com base na média de umidade.")
else:
    print("Não há indícios de chuva com base na média de umidade.")