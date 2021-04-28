

import pandas as pd
import numpy as np
import os
import csv



df=pd.read_csv('wallstreetbet.csv')
df1=pd.read_csv('WSB_comments.csv')
df2=pd.read_excel('Russell-3000-Stock-Tickers-List.xlsx')



from collections import Counter

tikers = list(df2['Ticker'])

def count_tickers(s):
    data = Counter(s.split()) #split string by space
    return {k:v for k,v in data.items() if k in tikers} # chooses only tickers
    
    
count_tickers("GME AA is blah GME").



result = {}
result_per_row_in_df = df1.apply(lambda x: count_tickers(x.body), axis=1) # count tickers in every line creating a list of dicts
for d in list(result_per_row_in_df):  #go ever each line == each dict
    for k,v in d.items(): # run through each item in dict
        result.setdefault(k, 0)
        result[k] += v



result

