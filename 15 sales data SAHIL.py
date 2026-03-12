# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:02:58 2026

@author: Sahil
"""

import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("D:\Sem 6\BI Practical\Dataset.csv")
print(df.head(5))

total_sales=df['Sales'].sum()
print(total_sales)

total_profit=df['Profit'].sum()
print(total_profit)

product_sales=(df.groupby("Product")["Sales"].sum().reset_index())
print(product_sales)

profit_category=(df.groupby("Category")["Profit"].sum().reset_index())
print(profit_category)

plt.figure(figsize=(8,10))
plt.bar(product_sales["Product"],product_sales["Sales"])
plt.xticks(rotation=45)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Pic.png")
plt.close()

plt.figure(figsize=(8,10))
plt.bar(profit_category["Category"],profit_category["Profit"])
plt.xticks(rotation=45)
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("Pic1.png")
plt.close()
