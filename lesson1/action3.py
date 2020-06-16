# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
#action1
sum=0
for number in range(2,101,2):
    sum=sum+number
print(sum)

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

#action3
import pandas as pd
result=pd.read_csv('car_complain.csv')
result=result.drop(columns=['problem']).join(result.problem.str.get_dummies(','))
df=result.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数:',df.sort_values('count',ascending=False))
df1=result.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数:',df1.sort_values('count',ascending=False))
df2=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean()
print('平均车型投诉总数:',df2.sort_values('count',ascending=False))