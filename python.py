#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Data wrangling
# ## Data gathering

# In[2]:


df = pd.read_csv('mcdonalds_dataset.csv')
df.head()


# ## Data assessing

# In[21]:


df.info()


# In[4]:


df.duplicated().sum()


# In[5]:


df.isna().sum()


# In[6]:


df['last_checked'] = df['last_checked'].str.extract('(\d+)').astype(int)


# In[7]:


df.head()


# In[8]:


df[df['city'].isna()]


# ## Data cleaning

# In[9]:


df.drop(columns='alt', inplace=True)


# In[10]:


df.info()


# In[11]:


df.rename(columns={'dot' : 'status'}, inplace=True)


# # Exploring data

# In[12]:


df.describe()


# In[13]:


df['country'].value_counts()


# In[14]:


df.groupby(['is_broken', 'is_active']).count()


# In[15]:


print('Number of inactive working machines:',df.query('is_active == False and is_broken == False').count()[1])


# In[16]:


print('Number of broken machines:',df.is_broken.sum())


# In[17]:


df.groupby('country').sum()


# In[18]:


dbroken = (d['is_broken'] / d['is_active'])*100


# In[19]:


dbroken.plot()
plt.title = 'percentage of broken machines'


# In[20]:


df.to_csv('mcdonalds_dataset_mod.csv')

