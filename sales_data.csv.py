# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_analysis.csv')
# correct filename

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display DataFrame shape
print("\nShape of the DataFrame:")
print(df.shape)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Total sales by Product
sales_by_product = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Plot sales by product
sales_by_product.plot(kind='bar', title='Total Sales by Product', ylabel='Sales', xlabel='Product', color='skyblue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Plot sales by region
sales_by_region.plot(kind='bar', title='Total Sales by Region', ylabel='Sales', xlabel='Region', color='orange')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Filtering rows - show only Product A sales
product_a_sales = df[df['Product'] == 'Product A']
print("\nSales data for Product A:")
print(product_a_sales)

# Demonstrate loc and iloc
print("\nUsing loc to access row with index 0:")
print(df.loc[0])

print("\nUsing iloc to access first row:")
print(df.iloc[0])