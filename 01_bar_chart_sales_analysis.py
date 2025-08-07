import pandas as pd
import matplotlib.pyplot as plt
data = {'Product': ['Laptop', 'Mobile', 'Tablet', 'Monitor'],
        'Sales': [250, 450, 120, 300]}

df = pd.DataFrame(data)
plt.figure(figsize=(8,5))
plt.bar(df['Product'], df['Sales'])
plt.title('Product Sales Analysis')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()
