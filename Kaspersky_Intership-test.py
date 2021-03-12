#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math  
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pathlib
from pathlib import Path

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

df = pd.read_csv('content_es_2020.csv')
df2 = df.drop(columns = ['id', 'group_id', 'enterprise_group_id', 'stream_name', 'group_count', ], axis = 'columns')
df2


# In[2]:


#описание количества наблюдений, среднее, стандартное отклонение, максимальное и минимальное значения по файлу:
df.describe()


# In[26]:


al = df2.describe().drop(index = 'count', columns = ['clicks_total','clicks_tw'])
plt.figure()
al.plot.area(stacked=False, figsize=(20,20))


# In[4]:


#нахождение медианы по столбцам таблицы
mn = df2.median()
plt.figure(figsize=(10,10))
mn.plot.bar()
df2.median()


# In[5]:


#нахождение среднего по столбцам таблицы
mn = df2.mean()
plt.figure(figsize=(10,10))
mn.plot.bar()
df2.mean()


# In[6]:


#нахождение стандартного отклонения по столбцам таблицы
mn = df2.std()
plt.figure(figsize=(10,10))
mn.plot.bar()
df2.std()


# In[7]:


#нахождение максимума по столбцам таблицы
mx = df2.max().drop(index = ['approval_date_iso8601'])
plt.figure(figsize=(10,10))
mx.plot.bar()
mx


# In[8]:


#нахождение минимума по столбцам таблицы
mn = df2.min().drop(index = ['approval_date_iso8601'])
plt.figure(figsize=(10,10))
mn.plot.bar()
mn


# In[9]:


#топ10 человек, которыми были одобрены статьи
df["approved_by_name"].value_counts()[0:10]


# In[10]:


#топ10 человек, которые предложили данные статьи
df["suggested_by_name"].value_counts()[0:10]


# In[ ]:




