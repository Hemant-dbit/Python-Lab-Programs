import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

plt.figure(figsize=(8, 6))
corr = df[['Amount', 'Boxes Shipped']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
