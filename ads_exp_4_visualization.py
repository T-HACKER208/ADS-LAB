# -*- coding: utf-8 -*-
"""ADS EXP 4-Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lF56Nt6iqgfsa9uhPdMYLOMTL3fS2gK_
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)

"""Read Csv File"""

df=pd.read_csv("tips-expt4.csv")

df.head()

"""Preprocessing"""

df.isnull().sum()

df.describe()

df.tip.describe()

"""Five Number Summary For Bill and Tip"""

bill = df.total_bill
print("Maximum Bill : ",np.max(bill))
print("Minimum Bill : ",np.min(bill))
print("Standard Deviation : ",np.std(bill))
print("Median : ",np.median(bill))
print("Mean : ",np.mean(bill))

tip = df.tip
print("Maximum Bill : ",np.max(tip))
print("Minimum Bill : ",np.min(tip))
print("Standard Deviation : ",np.std(tip))
print("Median : ",np.median(tip))
print("Mean : ",np.mean(tip))

"""Exploratory Data Analysis

"""

sb.countplot(x='sex',data=df)
sb.despine()

print(df.sex.value_counts())

sb.countplot(x='sex',data=df,hue='smoker',palette='viridis')

plt.figure(figsize=(8,6))
plt.title('Tips Per Day Of Week')
sb.countplot(x=df['day'],color='purple')

sb.catplot(x='day',data=df,hue='sex',palette='ch:.25',kind='count')

sb.distplot(df['tip'])

g=sb.distplot(df.tip,kde=False)
g.set_title('Tip Amount Histogram')

"""Outliers In bill column"""

plt.figure(figsize=(20,5))
sb.boxplot(x=bill,color='b')

"""Outliers In tip column"""

plt.figure(figsize=(20,5))
sb.boxplot(x=tip,color='g')

"""IQR Value"""

bill_tip=pd.DataFrame(df,columns=['total_bill','tips','size'])

print(bill_tip)

print("IQR For Total Bill : ",stats.iqr(bill))
print("IQR For Tip : ",stats.iqr(tip))

sb.relplot(x='total_bill',y='tip',data=df,col='time',hue='smoker',size='size')

plt.figure(figsize=(12,10))
sb.scatterplot(data=df,x='total_bill',y="tip",hue="sex")

sb.lmplot(x='total_bill',y='tip',data=df,col='time',hue='smoker')

sb.catplot(x='day',y='tip',data=df,kind='swarm')

sb.catplot(x='time',y='tip',data=df,height=6,kind='bar',palette='muted')

sb.catplot(x='day',y='tip',data=df,kind='violin')

sb.pairplot(df,hue='sex')

"""Correlation Matrix"""

corr_matrix=df[["total_bill","tip","size"]].corr()
ax=sb.heatmap(data=corr_matrix,annot=True,vmax=1,vmin=-1,center=0)
bottom,top=ax.get_ylim()
ax.set_ylim(bottom + 0.5,top - 0.5)

from sklearn.preprocessing import LabelEncoder
labelencoder_df = LabelEncoder()
df['sex']=labelencoder_df.fit_transform(df['sex'])
df['smoker']=labelencoder_df.fit_transform(df['smoker'])
df['day']=labelencoder_df.fit_transform(df['day'])
df['time']=labelencoder_df.fit_transform(df['time'])
df.head()

corr_matrix=df.corr()
ax=sb.heatmap(data=corr_matrix,annot=True,vmax=1,vmin=-1,center=0)
bottom,top=ax.get_ylim()
ax.set_ylim(bottom + 0.5,top - 0.5)