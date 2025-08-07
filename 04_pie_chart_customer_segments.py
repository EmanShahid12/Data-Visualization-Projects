import matplotlib.pyplot as plt

segments = ['Retail', 'Wholesale', 'Online', 'Others']
values = [40, 30, 20, 10]
plt.pie(values, labels=segments, autopct='%1.1f%%', startangle=140)
plt.title('Customer Segments Distribution')
plt.tight_layout()
plt.show()
