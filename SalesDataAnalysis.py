import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns



sales_data=pd.read_csv("C:/Users/home/Desktop/Sales Data.csv")

# Printing the first five rows.
print(sales_data.head())

print(sales_data.info())

# Identifying sales trends over time.

products=sales_data["Product"]
sales=sales_data["Sales"]
time=sales_data["Hour"]

sales_trend_with_time= sales.corr(time)

print(sales_trend_with_time)

sns.lineplot(x="Hour",y="Sales",data=sales_data)
plt.show()



# Best Sale
best_sale= sales_data["Sales"].max()

print(best_sale)

# Top 90th percentile  Sales
top_sales=np.percentile(sales_data["Sales"],90)
print(top_sales)

# Let's only consider the  sales data above or equal to the mean value and plot them against each other to figure out the most sales.

best_sales=sales_data[sales_data["Sales"]>top_sales]
top_sales_column= sales_data[sales_data["Sales"]>top_sales]["Sales"]
top_products=best_sales["Product"]

print(top_sales_column)

top_selling= pd.DataFrame(best_sales,columns=["Order ID","Product","Quantity Ordered","Price Each","Order Date","Purchase Address","Month","Sales","City","Hour"])
print(top_selling)

fig=px.bar(best_sales,x="Product",y="Sales")
fig.update_traces(marker_color = 'green', marker_line_color = 'black',
                  marker_line_width = 2, opacity = 1)


fig.show()





# Best Sale
best_sale= sales_data["Sales"].max()

print(best_sale)

# Top 90th percentile  Sales
top_sales=np.percentile(sales_data["Sales"],90)
print(top_sales)

# Let's only consider the  sales data above or equal to the mean value and plot them against each other to figure out the most sales.

best_sales=sales_data[sales_data["Sales"]>top_sales]
top_sales_column= sales_data[sales_data["Sales"]>top_sales]["Sales"]
top_products=best_sales["Product"]

print(top_sales_column)

top_selling= pd.DataFrame(best_sales,columns=["Order ID","Product","Quantity Ordered","Price Each","Order Date","Purchase Address","Month","Sales","City","Hour"])
print(top_selling)

# Plot by Matplolib
plt.bar(top_products,top_sales_column)
plt.show()

sns.barplot(x="Product",y="Sales",data=best_sales)
plt.show()



# Calculating Revenue Metrices  such as total sales,etc.


total_sales=sales_data["Sales"].sum()

print(total_sales)

# So the total sales turns out to be  34492035.97.


# Determining the best month for sales.

best_sales_sales=best_sales["Sales"]
best_months=list(set(best_sales["Month"]))
print(best_months)

sns.barplot(x="Month",y="Sales",data=best_sales)
plt.show()


#City which sold the most products
best_sales_cities=  list(set(best_sales["City"]))
print(best_sales_cities)


# Plotting the best sales in cities.

sns.barplot(x="City",y="Sales",data="best_sales")
plt.show()



