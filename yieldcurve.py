import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import datetime

# 1. Paramètres

start_date = "2018-01-01"
end_date = datetime.datetime.today()


# 2. Télécharger les taux US depuis FRED
# -----------------------------
# DGS2 = 2 Year Treasury
# DGS10 = 10 Year Treasury

df = pdr.DataReader(["DGS2", "DGS10"], "fred", start_date, end_date)

df = df.dropna()


# 3. Calcul de la pente (spread)
# -----------------------------
df["Spread_10Y_2Y"] = df["DGS10"] - df["DGS2"]


# 4. Visualisation
# -----------------------------

# Graphique des taux
plt.figure(figsize=(10,6))
plt.plot(df.index, df["DGS2"], label="2Y Treasury")
plt.plot(df.index, df["DGS10"], label="10Y Treasury")
plt.title("US Yield Curve (2Y vs 10Y)")
plt.ylabel("Yield (%)")
plt.legend()
plt.grid(True)
plt.show()

# Graphique du spread
plt.figure(figsize=(10,6))
plt.plot(df.index, df["Spread_10Y_2Y"])
plt.axhline(0, linestyle="--")
plt.title("Yield Curve Spread (10Y - 2Y)")
plt.ylabel("Spread (%)")
plt.grid(True)
plt.show()

# 5. Interprétation simple
# -----------------------------
latest_spread = df["Spread_10Y_2Y"].iloc[-1]

print(f"Spread actuel (10Y - 2Y) : {latest_spread:.2f}%")

if latest_spread > 0:
    print("Courbe normale : croissance anticipée.")
elif latest_spread < 0:
    print("Courbe inversée : signal potentiel de récession.")
else:
    print("Courbe plate : incertitude économique.")

    spread = yield_10y - yield_2y
plt.plot(spread)
plt.axhline(0, linestyle='--')