import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

plt.figure(figsize=(10, 5))
plt.scatter(df['Boxes Shipped'], df['Amount'], color='blue', edgecolors='black', alpha=0.7)
plt.xlabel('Boxes Shipped')
plt.ylabel('Sales Amount ($)')
plt.title('Scatter Plot: Boxes Shipped vs. Sales Amount')
plt.grid(True)
plt.tight_layout()
plt.show()
