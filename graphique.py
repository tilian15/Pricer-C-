import pandas as pd
import matplotlib.pyplot as plt

# Charger les données pour Delta Hedging
data_delta = pd.read_csv("delta_hedging.csv")

# Charger les données pour Delta-Gamma Hedging
data_delta_gamma = pd.read_csv("delta_gamma_hedging.csv")

# Créer une figure
plt.figure(figsize=(10, 6))

# Tracer la stratégie Delta Hedging
plt.plot(data_delta["Step"], data_delta["Portfolio Value"], label="Portfolio Value (Delta Hedging)", color="blue")
plt.plot(data_delta["Step"], data_delta["Stock Price"], label="Stock Price", color="green", linestyle="--")

# Tracer la stratégie Delta-Gamma Hedging
plt.plot(data_delta_gamma["Step"], data_delta_gamma["Portfolio Value"], label="Portfolio Value (Delta-Gamma Hedging)", color="red")

# Ajouter des titres et légendes
plt.title("Comparison of Delta Hedging and Delta-Gamma Hedging")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
