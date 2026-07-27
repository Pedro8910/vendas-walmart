#projeto de vendas do walmart
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Walmart_Sales.csv')
print(df.shape)
print(df.dtypes)
print(df.isna().sum())  # confirmar que não há nulos

#Converter a data (está em DD-MM-AAAA, vira MM-DD-AAAA):
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Weekly_Sales'] = df['Weekly_Sales'].round(2)
df['Temperature'] = df['Temperature'].round(0).astype(int)
df['Fuel_Price'] = df['Fuel_Price'].round(2)
df['CPI'] = df['CPI'].round(3)
df['Unemployment'] = df['Unemployment'].round(3)

#Ordenar por loja (crescente) e depois por data (crescente)
df = df.sort_values(['Store', 'Date']).reset_index(drop=True)

#Converter a data de volta pro formato texto pedido (MM-DD-AAAA), só no final
df['Date'] = df['Date'].dt.strftime('%m-%d-%Y')

print(df.isna().sum())

#Salve o resultado limpo
df.to_csv('Walmart_Sales_clean.csv', index=False)

#Quais feriados afetam mais as vendas?
# reconverta Date pra datetime pra extrair mês
df['Date_dt'] = pd.to_datetime(df['Date'], format='%m-%d-%Y')
df['Month'] = df['Date_dt'].dt.month
holidays = df[df['Holiday_Flag'] == 1]
print(holidays.groupby('Month')['Weekly_Sales'].mean())

#Lojas com menor/maior desemprego
df.groupby('Store')['Unemployment'].mean().sort_values()

#Correlação CPI x Vendas Semanais (geral e por Holiday_Flag)
print(df['CPI'].corr(df['Weekly_Sales']))
print(df[df['Holiday_Flag']==0][['CPI','Weekly_Sales']].corr())
print(df[df['Holiday_Flag']==1][['CPI','Weekly_Sales']].corr())

#Fuel Price
df[['Weekly_Sales','Temperature','Fuel_Price','CPI','Unemployment']].corr()

# Estilo dos gráficos
sns.set(style="whitegrid")

#Gráfico 1 – Média de Vendas por Mês
# Converter a data novamente
df['Date_dt'] = pd.to_datetime(df['Date'], format='%m-%d-%Y')

# Criar coluna do mês
df['Month'] = df['Date_dt'].dt.month

# Média das vendas por mês
media_mes = df.groupby('Month')['Weekly_Sales'].mean()

# Criar gráfico
plt.figure(figsize=(10,5))

plt.bar(media_mes.index, media_mes.values)

plt.title('Média das Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Média das Vendas')

plt.xticks(range(1,13))
plt.show()

#Gráfico 2 – Scatter Plot (CPI × Weekly Sales)
plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x='CPI',
    y='Weekly_Sales',
    hue='Holiday_Flag',
    palette='Set1'
)

plt.title('CPI x Weekly Sales')
plt.xlabel('CPI')
plt.ylabel('Weekly Sales')

plt.legend(title='Holiday Flag')
plt.show()