# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:53:09 2026

@author: Sahil
"""

import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv(r'D:\Sem 6\BI Practical\Coffe_sales.csv')

coffe_revenue=(df.groupby('coffee_name')['money'].sum().sort_values(ascending=False).reset_index())

plt.figure(figsize=(14,10))
plt.bar(coffe_revenue['coffee_name'],coffe_revenue['money'])
plt.xticks(rotation=45)
plt.xlabel("cooffee name")
plt.ylabel("Money")
plt.tight_layout()
plt.savefig("revenue_of_cooffee.png")

plt.close()

weekdayr=(df.groupby("Weekday")["money"].sum().sort_values(ascending=False).reset_index())
plt.figure(figsize=(5,8))
plt.bar(weekdayr["Weekday"],weekdayr["money"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Weekday.png")
plt.close()