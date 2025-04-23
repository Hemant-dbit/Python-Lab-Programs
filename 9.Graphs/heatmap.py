import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

pivot_table = df.pivot_table(values='Amount', index='Country', columns='Product', aggfunc='sum', fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap of Total Sales by Country and Product")
plt.xlabel("Product")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
