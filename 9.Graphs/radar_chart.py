import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Chocolate_Sales.csv')
average_boxes = df.groupby('Product')['Boxes Shipped'].mean().reset_index()
top_products = average_boxes.nlargest(5, 'Boxes Shipped')

labels = top_products['Product'].tolist()
values = top_products['Boxes Shipped'].tolist()

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Average Boxes Shipped by Product (Top 5)', size=15)
plt.tight_layout()
plt.show()
