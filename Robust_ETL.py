#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import re as re
import unicodedata

from datetime import datetime
from time import gmtime, strftime

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


# In[2]:


#Create a dataframe to read clean file
try:
    df_CLEAN = pd.read_csv(r'C:\Users\mmolepo\Desktop\BluNova\Assessments\Data Engineer\data_engineer_clean_set.csv',
                         encoding="utf-8")
except Exception as e:
    print("Error occered while opening the file: \n", e)


# In[3]:


#Create a dataframe to read dirty file
try:
    df_DIRTY = pd.read_csv(r'C:\Users\mmolepo\Desktop\BluNova\Assessments\Data Engineer\data_engineer_dirty_set_1.csv',
                         encoding="UTF-8")
except Exception as e:
    print("Error occered while opening the file: \n", e)


# In[4]:


# The first is to reorder the columns
df_NEW_DIRTY = df_DIRTY[['tran_id', 'first_name', 'last_name', 'tran_date', 'gender', 'value', 'tran_hash', 'tran_lat', 'tran_long', 'tran_type', 'tran_status']]


# In[5]:


#The rename the column value to tran_value. Using dataframe
df_NEW_DIRTY = df_NEW_DIRTY.rename(columns={'value': 'tran_value'})


# In[6]:


#Change the decimal of tran_value to two decimal place

def getTwoDecimal (value):
    if (value is None): #Even nan value will cause an error. I'll try to handle it, just being precautious. 
        return None 
    else:
        return round(value, 2) #Normal value
    

#Round the column values to two
fields = ['tran_value'] #If we have another that need to be convert to 2 decimal we can add it.
for col in fields:
    df_NEW_DIRTY[col] = df_NEW_DIRTY[col].map(lambda x: getTwoDecimal(x))


# In[7]:


#Change the date format to yyyy/mm/dd and import datetime to change the format od the date.

def changeDateFormat(date_format):
    if (date_format is None or date_format == 'nan'):
        return None
    else:
        date_format = datetime.strptime(date_format,'%m/%d/%Y').strftime('%Y/%m/%d')
        return date_format
    
df_NEW_DIRTY['tran_date'] = df_NEW_DIRTY['tran_date'].map(lambda date: changeDateFormat(str(date))) #Normalize date to string


# In[8]:


#Change gender code to the actual string by creating mapping using a function.
def getGenderString(code):
    if (code is None):
        return code
    elif (code == 'F' or code == 'f'):
        code = "Female"
        return code
    elif (code == 'M' or code == 'm'):
        code ='Male'
        return code
    else:
        return code
    

df_NEW_DIRTY['gender'] = df_NEW_DIRTY['gender'].map(lambda g: getGenderString(g))       


# In[9]:


#Drop null value in coulmns with null values
df_NEW_DIRTY = df_NEW_DIRTY.dropna(subset=['first_name', 'last_name', 'tran_date', 'tran_value', 'tran_type'])


# In[10]:


df_NEW_DIRTY = df_NEW_DIRTY[df_NEW_DIRTY['tran_status'] < 6] #filter out status above five.


# In[11]:


series = df_NEW_DIRTY['tran_type']
df_NEW_DIRTY['tran_type'] =  [s.encode('ascii', 'ignore').strip()
                              for s in series.str.decode('unicode_escape')]


# In[12]:


df_NEW_DIRTY.to_csv(r'C:\Users\mmolepo\Desktop\BluNova\Assessments\Data Engineer\new_data_engineer_dirty_set_1.csv',
                         encoding="utf-8")

