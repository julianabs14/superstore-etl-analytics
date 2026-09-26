import pandas as pd

def extrair_dados(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin1")
    print(f"[EXTRACT] {df.shape[0]} linhas, {df.shape[1]} colunas carregadas.")
    return df

if __name__ == "__main__":
    df = extrair_dados("data/raw/superstore.csv")
    print(df.head())