import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
country_sales = df.groupby('Country')['Amount'].sum()

plt.figure(figsize=(10, 6))
country_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Country")
plt.xlabel("Country")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
