# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:58:53 2021

@author: HuYuan
"""


#汽车消费城市划分
#使用Kmeans 进行聚类(cluster)
from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np
import pandas as pd

# 数据加载
data = pd.read_csv('./car_data.csv',encoding='gbk')
#print(data)
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数", "百户拥有汽车量"]]
#print(train_x)
# 规范化到[0,1]空间，把所有数值统一量纲
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv',index=False)
#print(train_x)

# 使用kmeans进行聚类
kmeans = KMeans(n_clusters=4)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
#合并聚类结果，插入原始数据中
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
#将结果导出到csv文件中
result.to_csv("car_data_result.csv",index=False)

###使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans,AgglomerativeClustering 
import matplotlib.pyplot as plt
model=AgglomerativeClustering(linkage='ward',n_clusters=3)
#fit+predict
y=model.fit_predict(train_x)
print(y)
linkage_matrix=ward(train_x)
dendrogram(linkage_matrix)
plt.show()
### 手肘法确定K-Means的族数K
sse = []
for k in range(1, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
