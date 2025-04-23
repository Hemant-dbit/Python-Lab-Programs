import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

plt.figure(figsize=(8, 5))
plt.boxplot(df['Amount'])
plt.title("Boxplot of Sales Amount")
plt.ylabel("Amount ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
