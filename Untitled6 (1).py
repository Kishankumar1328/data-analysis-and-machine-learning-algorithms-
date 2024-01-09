#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


df=pd.read_csv("E:\IBM\covid_vaccine_statewise - covid_vaccine_statewise (1).csv")
df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.dtypes


# In[7]:


df.isnull()


# In[10]:


df["First Dose Administered"].fillna(df["First Dose Administered"].mode()[0],inplace=True)


# In[11]:


df.dropna().values


# In[12]:


df.describe().T


# In[13]:


df.info()


# In[14]:


df["Sessions"].hist()


# In[16]:


df.groupby("State")


# In[ ]:




