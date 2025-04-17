from xmlrpc.client import DateTime

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(
    host ='localhost',
    user= 'root',
    password='123456',
    database = 'ecommercesales'
)

query = "SELECT * FROM data;"
df= pd.read_sql(query,conn)
#print(df.isnull().sum())
#print(df['InvoiceNo'].duplicated().sum())
#print(df["InvoiceNo"].unique())

df["Description"] = df["Description"].str.lower() #change to lowercase
df["Description"] = df["Description"].str.strip() #remove extra spaces
df["InvoiceDate"]= pd.to_datetime(df["InvoiceDate"], format='%d/%m/%Y %H:%M')
df['Week'] = df['InvoiceDate'].dt.to_period('W').dt.to_timestamp()
df['Hour'] = df['InvoiceDate'].dt.hour

df["Country"].replace({"Unted Kingdom": "United Kingdom"}, inplace=True)

Total_revenue = "SELECT SUM(InvoiceTotal) as total_revenue FROM data"
df2 = pd.read_sql(Total_revenue,conn)
print(df2)

total_orders = "SELECT COUNT(InvoiceNo) as total_orders FROM data"
df3= pd.read_sql(total_orders,conn)
print(df3)

total_customers= "SELECT COUNT(DISTINCT CustomerID) as total_customers FROM data"
df4= pd.read_sql(total_customers,conn)
print(df4)

average_order_value = "SELECT AVG(InvoiceTotal) as avg_order_value FROM data"
df5 = pd.read_sql(average_order_value,conn)
print(df5)

average_revenue_per_customer = "SELECT CustomerID, AVG(InvoiceTotal) FROM data GROUP BY CustomerID"
df6 = pd.read_sql(average_revenue_per_customer,conn)
print(df6)

top_selling = "SELECT StockCode, SUM(Quantity) as count FROM data GROUP BY StockCode ORDER BY count DESC LIMIT 10"
df7 = pd.read_sql(top_selling,conn)
print(df7['StockCode'])

revenue_by_product = "SELECT StockCode, SUM(InvoiceTotal) FROM data GROUP BY StockCode"
df8 = pd.read_sql(revenue_by_product,conn)
print(df8)

sales_by_country = "SELECT Country, SUM(InvoiceTotal) as sum FROM data GROUP BY Country"
df9 = pd.read_sql(sales_by_country,conn)
print(df9)

plt.bar(df7['StockCode'],df7['count'],color="y")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Stock Code")
plt.ylabel("Quantity")
plt.show()

country = df9['Country']
sales = df9['sum']
plt.pie(sales,labels=country)
plt.title("Sales by Country")
plt.show()

'''
df_weekly= df.groupby('Week').agg(weekly_sales=('InvoiceTotal', 'sum')).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_weekly, x='Week', y='weekly_sales', marker='o', color='steelblue')
plt.title('Weekly Sales Trend', fontsize=16)
plt.xlabel('Week', fontsize=12)
plt.ylabel('Total Sales (£)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
'''

hourly_sales = df.groupby('Hour').agg(total_sales=('InvoiceTotal', 'sum')).reset_index()
hourly_sales['Hour'] = hourly_sales['Hour'].astype(str)

plt.figure(figsize=(10, 5))
sns.barplot(data=hourly_sales, x='Hour', y='total_sales', palette='coolwarm')
plt.title('Sales by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

product_stats = df.groupby('Description').agg({
    'Quantity': 'sum',
    'InvoiceTotal': 'sum'
}).reset_index()

# Rename for clarity
product_stats.columns = ['Product', 'TotalQuantity', 'TotalRevenue']

plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=product_stats,
    x='TotalQuantity',
    y='TotalRevenue',
    hue='TotalRevenue',
    palette='viridis',
    size='TotalRevenue',
    sizes=(20, 200),
    alpha=0.7
)

plt.title('Product Segmentation: Revenue vs Quantity')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv('ecommerce_sales_cleaned.csv', index=False)

conn.close()

