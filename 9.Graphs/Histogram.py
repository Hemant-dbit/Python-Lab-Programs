import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate_Sales.csv')

plt.figure(figsize=(16, 5))
df['Product'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Frequency of Chocolate Products Sold')
plt.xlabel('Product')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
