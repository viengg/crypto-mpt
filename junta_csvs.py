import pandas as pd
import glob
from functools import reduce

TIPO_DADOS = "acoes"

path = f"dados\\{TIPO_DADOS}_yahoo_atualizadas\\"
nome_arquivos = glob.glob(path+"*.csv")
print(f"{len(nome_arquivos)} arquivos encontrados!")

dfs = []
for arquivo in nome_arquivos:
    simbolo = arquivo.split("\\")[-1].split(".")[0]

    df = pd.read_csv(arquivo)[["Date", "Adj Close"]]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.rename(columns={"Adj Close": simbolo}).set_index("Date")
    dfs.append(df)

merged_df = reduce(lambda left, right: pd.merge(left, right, on=["Date"], how="left"), dfs)
print(merged_df.head())
merged_df.to_csv(f"dados_{TIPO_DADOS}.csv")