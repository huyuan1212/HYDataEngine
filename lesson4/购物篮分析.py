# -*- coding: utf-8 -*-
"""
Created on Wed May 19 21:54:25 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
from efficient_apriori import apriori
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
#print(data)
transactions=[]
#按照行进行遍历
for i in range(0,data.shape[0]):
    #记录一行transactions
    temp=[]
    #按照列进行遍历
    for j in range(0,data.shape[1]):
        if str(data.values[i,j])!='nan':
            temp.append(data.values[i,j])
        #print(temp)
        transactions.append(temp)
# 挖掘频繁项集和频繁规则
itemsets,rules=apriori(transactions,min_support=0.02,min_confidence=0.3)
print("频繁规则：",itemsets)
print("关联规则：",rules)
