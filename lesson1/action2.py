# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:51:42 2020

@author: Administrator
"""
#action2
from pandas import Series,DataFrame
import pandas as pd
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print('各科平均分',df.mean())
print('各科最低分',df.min())
print('各科最高分',df.max())
print('各科成绩的方差',df.var())
print('各科成绩的标准差',df.std())
df['总分']=df.sum(axis=1)
print(df.sort_values('总分',ascending=False))

