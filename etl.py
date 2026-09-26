import pandas as pd

def extrair_dados(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin1")
    print(f"[EXTRAIR] {df.shape[0]} linhas, {df.shape[1]} colunas carregadas.")
    return df

def transformacao_de_dados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(subset=["Order ID", "Sales"])

    df = df.rename(columns={
        "Order ID": "id_pedido",
        "Order Date": "data_pedido",
        "Ship Date": "data_envio",
        "Ship Mode": "modo_envio",
        "Customer Name": "nome_cliente",
        "Segment": "segmento",
        "Region": "regiao",
        "Category": "categoria",
        "Sub-Category": "subcategoria",
        "Product Name": "nome_produto",
        "Sales": "vendas",
        "Quantity": "quantidade",
        "Discount": "desconto",
        "Profit": "lucro",
    })

    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["data_envio"] = pd.to_datetime(df["data_envio"], errors="coerce")

    df["vendas"] = df["vendas"].round(2)
    df["lucro"] = df["lucro"].round(2)

    df["dias_entrega"] = (df["data_envio"] - df["data_pedido"]).dt.days

    df["regiao"] = df["regiao"].str.strip().str.title()
    df["categoria"] = df["categoria"].str.strip().str.title()

    print(f"[TRANSFORMAR] {df.shape[0]} linhas após limpeza.")
    return df

def carregar_dados(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    print(f"[CARREGAR] Dados salvos em {path}")

if __name__ == "__main__":
    df = extrair_dados("data/raw/superstore.csv")
    df = transformacao_de_dados(df)
    carregar_dados(df, "data/processed/superstore_clean.csv")