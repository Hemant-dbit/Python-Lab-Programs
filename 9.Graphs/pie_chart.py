import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
country_sales = df.groupby('Country')['Amount'].sum()

plt.figure(figsize=(8, 8))
country_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title("Total Sales Distribution by Country")
plt.ylabel("")
plt.tight_layout()
plt.show()
