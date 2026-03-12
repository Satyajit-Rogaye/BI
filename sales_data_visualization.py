import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("Sales_data.csv")

total_sales=df['TotalPrice'].sum()
#print(total_sales)
product_sales=(df.groupby("Product")['TotalPrice'].sum().reset_index())
#print(product_sales)


#Pie Chart
Total_Payment_Method=df['PaymentMethod'].value_counts()
print(Total_Payment_Method)
labels=Total_Payment_Method.index
print(labels)
explode=(0,0.1,0,0,0)

laptop_data=df[df['Product']=='Laptop']
region_sales=laptop_data.groupby('Region')['Quantity'].sum()

phone_data=df[df['Product']=='Phone']
salesperson_data=phone_data.groupby('CustomerType')['Quantity'].sum()

plt.bar(product_sales['Product'],product_sales['TotalPrice'],color="red")
plt.title("Total Product Price ")
plt.xlabel("Product Name")
plt.ylabel("Total Price")
plt.show()

plt.figure(figsize=(8,10))
plt.pie(Total_Payment_Method,autopct='%1.1f%%',labels=labels,explode=explode,shadow=True,startangle=90)
plt.legend()
plt.title("Payment Method Distribution")
plt.show()

region_sales.plot(kind='bar',color='green')
plt.ylabel('Quantity')
plt.title("Laptop Quantity Sales over region")
plt.show()

salesperson_data.plot(kind='bar',color='orange')
plt.ylabel('Quantity')
plt.title('How Much Phone Sales by Customer ')
plt.show()

fig,ax=plt.subplots(2,2,figsize=(15,10))
fig.suptitle("Data Visualization")
ax[0,0].bar(product_sales['Product'],product_sales['TotalPrice'],color="red")
ax[0,0].set_title("Total Product Price ")
ax[0,0].set_xlabel("Product Name")
ax[0,0].set_ylabel("Total Price")


ax[0,1].pie(Total_Payment_Method,autopct='%1.1f%%',labels=labels,explode=explode,shadow=True,startangle=90)
ax[0,1].legend(loc='lower right',bbox_to_anchor=(1,1))
ax[0,1].set_title("Payment Method Distribution")

region_sales.plot(kind='bar',color='green',ax=ax[1,0])
ax[1,0].set_ylabel('Quantity')
ax[1,0].set_title("Laptop Quantity Sales over region")


salesperson_data.plot(kind='bar',color='orange',ax=ax[1,1])
ax[1,1].set_ylabel('Quantity')
ax[1,1].set_title('How Much Phone Sales by Customer ')
plt.tight_layout()
plt.show()



