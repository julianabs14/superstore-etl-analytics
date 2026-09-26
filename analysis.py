import pandas as pd

df = pd.read_csv("data\processed\superstore_clean.csv")

print("--- Vendas por categoria ---")
print(df.groupby("categoria")["vendas"].sum().sort_values(ascending=False))

print("\n--- Lucro médio por região ---")
print(df.groupby("regiao")["lucro"].mean().round(2))

print("\n--- Top 5 produtos mais vendidos (qtd) ---")
print(df.groupby("nome_produto")["quantidade"].sum().sort_values(ascending=False).head(5))

print("\n--- Tempo médio de entrega por região ---")
print(df.groupby("regiao")["dias_entrega"].mean().round(1))

