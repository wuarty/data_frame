import pandas as pd
import numpy as np
import glob
import os
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data_frame/dados.csv")


novos = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Carlos"],
    "idade": [26, 28, 30, 25, 32],
    "cidade": [
        "Vitória",
        "Belo Horizonte",
        "Rio de Janeiro",
        "São Paulo",
        "Porto Alegre",
    ],
    "gasto_alimentacao": [680, 700, 600, 800, 900],
    "gasto_transporte": [150, 170, 200, 150, 220],
    "gasto_lazer": [160, 190, 150, 200, 300],
}

df = pd.concat([df, pd.DataFrame(novos)], ignore_index=True)


df = df.drop_duplicates(subset=["nome"], keep="first")
df = df.sort_values(by="nome").reset_index(drop=True)
df["id"] = df.index + 1


df.to_csv("data_frame/dados.csv", index=False)


gasto_total = df["gasto_alimentacao"] + df["gasto_transporte"] + df["gasto_lazer"]
df["gasto_total"] = gasto_total
media_gasto_total = df["gasto_total"].mean()
print(f"Média do gasto total: {media_gasto_total:.2f}")

df["gasto_alimentacao"].sum()
gasto_medio_alimentacao = df["gasto_alimentacao"].mean()
print(f"Gasto médio com alimentação: {gasto_medio_alimentacao:.2f}")
gasto_medio_transporte = df["gasto_transporte"].mean()
print(f"Gasto médio com transporte: {gasto_medio_transporte:.2f}")
gasto_medio_lazer = df["gasto_lazer"].mean()
print(f"Gasto médio com lazer: {gasto_medio_lazer:.2f}")

sns.barplot(x="nome", y="gasto_total", data=df)
plt.title("Gasto Total por Pessoa")
plt.xlabel("Nome")
plt.ylabel("Gasto Total")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
