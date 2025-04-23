import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

date_sales = df.groupby('Date')['Amount'].sum().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(date_sales.index, date_sales.values, marker='o', linestyle='-', color='b')
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
