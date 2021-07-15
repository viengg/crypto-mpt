import pandas as pd
import glob
import os
from functools import reduce

path = "dados/criptos_yahoo"
os.chdir(path)
nome_arquivos = glob.glob("*.csv")
print(f"{len(nome_arquivos)} arquivos encontrados!")

dfs = []
for arquivo in nome_arquivos:
    simbolo = arquivo.split(".")[0]

    df = pd.read_csv(arquivo)[["Date", "Adj Close"]]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.rename(columns={"Adj Close": simbolo}).set_index("Date")
    dfs.append(df)

merged_df = reduce(lambda left, right: pd.merge(left, right, on=["Date"], how="left"), dfs)
print(merged_df.head())
merged_df.to_csv("dados_criptos.csv")