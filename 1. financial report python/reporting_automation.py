import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données financières
df = pd.read_csv("data/financial_data.csv")

# Nettoyage et transformation des données
df.dropna(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values("Date", inplace=True)

# Calculs financiers
df["Revenue Growth"] = df["Revenue"].pct_change()
summary = df.groupby("Category")["Revenue"].sum().reset_index()

# Génération de visualisations
plt.figure(figsize=(10, 5))
sns.barplot(x="Category", y="Revenue", data=summary)
plt.title("Revenus par catégorie")
plt.savefig("outputs/revenue_by_category.png")

# Export des résultats
df.to_csv("outputs/cleaned_financial_data.csv", index=False)
print("Reporting automatisé terminé. Fichiers exportés dans outputs/")
