# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:14:21 2019

@author: Niran
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mlp
import matplotlib.pyplot as plt

ds=pd.read_csv("BlackFriday.csv")

ds.info()

#finding out total no of null values
ds.isnull().sum()

#droping null rows
df=ds.dropna()
df.describe()
#customer who purchased maximum
df["Purchase"].max()

#customer who purchased minimum
df["Purchase"].min()


df.groupby(['Gender', 'Marital_Status']).count()


df.groupby(['City_Category', 'Purchase']).mean()

def plot(group,column,plot):
    ax=plt.figure(figsize=(12,6))
    df.groupby(group)[column].sum().sort_values().plot(plot)
    
plot('Gender','Purchase','bar')

plot('Stay_In_Current_City_Years','Purchase','bar')

""""""""""""""""""""""""""""""""""""""""""""""""
fig1, ax1 = plt.subplots(figsize=(12,7))
df['Occupation'].value_counts().sort_values().plot('bar')

plot('Occupation','Purchase','bar')

plot('Product_Category_1','Purchase','barh')

plot('Product_Category_2','Purchase','barh')

plot('Product_Category_3','Purchase','barh')


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Purchase'].count().nlargest(10).sort_values().plot('barh')

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Purchase'].sum().nlargest(10).sort_values().plot('barh')



rs = np.random.RandomState(0)
df = pd.DataFrame(rs.rand(13, 13))
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')
print (corr)



''''''''''''''''''''''''''''''''''''''''''
fig1, ax1 = plt.subplots(figsize=(12,7))
sns.countplot(df['Age'],hue=df['Gender'])

plot('Age','Purchase','bar')

Obviously, we can consider that the 
target age group of our stores is the age group of 26-35 years,
 we have achieved sales of more than 3 billion in the age group of 26-45 years
''''''''''''''''''''''''''''''''''''''''''

fig1, ax1 = plt.subplots(figsize=(12,7))
sns.countplot(df['City_Category'],hue=df['Age'])
Unexpectedly, the highest sales do not come in the number of purchases,
 people from Area B have a greater purchasing power than others,
 and greater sales gained from people from Area C

''''''''''''''''''''''''''''''''''''''''''
plot('Stay_In_Current_City_Years','Purchase','bar')

We have worked hard in the past two years 
and have achieved a large percentage of sales from the new population of cities,
 but these figures indicate that the older city dwellers have less passion for our products.
 I do not know in fact look at it for yourselves why old city dwellers did not achieve higher sales of the population 
 New visitors or visitors from outside the city?
We have almost gained about 1.75 billion new city residents only!
''''''''''''''''''''''''''''''''''''''''''''''''''

new_df=df.copy()
new_df=new_df.drop(['User_ID','Product_ID'],axis=1)
plt.figure(figsize=(10,6))
sns.heatmap(new_df.corr(),annot=True,linewidths=0.3)

''''''''''''''''''''''''''''''''''''''''''''''''''''''
#today
plt.figure(figsize=(10,6))
sns.barplot(x='City_Category',y='Purchase',data=df,ci=0)

City category C has the highest purchase 
while city category A has the lowest purchase

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
plt.figure(figsize=(10,6))
sns.barplot(x='Occupation',y='Purchase',data=df,hue='Marital_Status',ci=0)

It can be estimated that a married person 
with Occupation 17 has the highest purchase and unmarried person with
 Occupation 12 has the highest purchase
 
''''''''''''''''''''''''''''''''''''''''''''''''''
plt.figure(figsize=(10,6))
sns.barplot(x='Product_Category_1',y='Purchase',data=df,ci=0)

In product category 1, 10th number product has the highest purchase
 while 4th number product has the least purchase.:
'''''''''''''''''''''''''''''''''''''''''''''''''
plt.figure(figsize=(10,6))
sns.barplot(x='Product_Category_2',y='Purchase',data=df,ci=0)

In product category 2, 10th number product has the highest purchase
while 7th number product has the least purchase.:
'''''''''''''''''''''''''''''''''''''''''''''''''
plt.figure(figsize=(10,6))
sns.barplot(x='Product_Category_3',y='Purchase',data=df,ci=0)

In product category 3, 3rd number product has the highest purchase 
while 0th number product has the least purchase
''''''''''''''''''''''''''''''''''''''''''''''''''
sns.boxplot('Product_Category_1','Purchase', data = df)
plt.show()






