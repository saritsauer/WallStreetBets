#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import csv


# In[2]:


df=pd.read_csv('WSB_post.csv')
df1=pd.read_csv('WSB_comments.csv')
df2=pd.read_excel('Russell-3000-Stock-Tickers-List.xlsx')


# In[3]:


df1.head()


# In[4]:


from datetime import datetime

df['Dates'] = pd.to_datetime(df['timestamp']).dt.date

df1['Dates'] = pd.to_datetime(df1['timestamp']).dt.date



# In[5]:


df1


# In[6]:


dates = df['Dates'].unique()
for i in df['Dates'].unique():
    print (i)


# In[7]:



from collections import Counter

tikers = list(df2['Ticker'])

def count_tickers(s,the_date):
    data = Counter(s.split()) #split string by space
    return {(the_date,k):v for k,v in data.items() if k in tikers} # chooses only tickers
    
    
#count_tickers("GME AA is blah GME")


# In[8]:



result = {}
result_per_row_in_df = df1.apply(lambda x: count_tickers(x.body, x.Dates), axis=1) # count tickers in every line creating a list of dicts
for d in list(result_per_row_in_df):  #go ever each line == each dict
    for k,v in d.items(): # run through each item in dict
        result.setdefault(k, 0)
        result[k] += v

flattened = []
for k,v in result.items():
    flattened.append([k[0], k[1], v])
pdf1 = pd.DataFrame(flattened, columns=['Date', 'Ticker', 'Count'])
x = pdf1.sort_values(["Date", "Count"], ascending=False).head(20)


# In[9]:


x.to_csv('comments_ticker_count.csv')


# In[10]:


x


# In[ ]:





# In[ ]:




