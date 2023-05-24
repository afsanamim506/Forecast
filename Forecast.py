#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv(r'E:\Anaconda 3\Forecast.csv')


# In[5]:


df


# In[ ]:





# In[6]:


for i in range(1, len(df)):
    previous_forecast = df.loc[i-1, 'Forecast']
    previous_demand = df.loc[i-1, 'Demand']
    current_forecast = previous_forecast + 0.1 * (previous_demand - previous_forecast)
    df.loc[i, 'Forecast'] = current_forecast


# In[ ]:





# In[9]:


df.to_csv('Forecast.csv', index=False)


# In[10]:


df


# In[ ]:




