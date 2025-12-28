import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Smartwatch'],
    'January': [50000, 40000, 20000, 10000, 15000],
    'February': [55000, 42000, 21000, 12000, 16000],
    'March': [60000, 45000, 25000, 14000, 18000]
}

df = pd.DataFrame(data)

df['Total Sales'] = df[['January', 'February', 'March']].sum(axis=1)

total_revenue = np.sum(df['Total Sales'])
average_sales = np.mean(df['Total Sales'])
top_product = df.loc[df['Total Sales'].idxmax()]

 
print(" SALES ANALYSIS REPORT ")
print(df)
print("\nTotal Revenue:", total_revenue)
print("Average Sales:", average_sales)
print("\nTop Selling Product:")
print(top_product)

plt.figure(figsize=(8,5))
plt.bar(df['Product'], df['Total Sales'], color='green')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df['Product'], df['Total Sales'], marker='o', linestyle='--')
plt.title("Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()
