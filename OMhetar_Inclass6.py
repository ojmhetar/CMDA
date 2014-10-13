# coding: utf-8
# In[3]:
import pandas as ps
# In[4]:
import requests
# In[5]:
import json
# In[22]:
import pytables               
# In[65]:
import random
# In[72]:
import numpy as np
# In[20]:
t1 = ps.read_csv("C:\Users\ojmhetar\Downloads\work_comma.csv")
# In[7]:
t2 = ps.read_table("C:\Users\ojmhetar\Downloads\work_tab.txt")
# In[8]:
t2
# In[9]:
r = requests.get("https://api.github.com/events")
# In[10]:
r
# In[11]:
t = r.json()
# In[12]:
t
# In[13]:
fields = ['id', 'created_at', 'public', 'repo']
# In[14]:
data_fr = ps.DataFrame(t, columns=fields)
# In[15]:
data_fr.to_pickle('DF_pickle')
# In[16]:
ps.read_pickle("DF_pickle")
# In[26]:
store=ps.HDFStore(data_fr)
# In[ ]:
store['obj1']
# In[25]:




#Inclass Part 2
# In[28]:
project = ps.read_csv("OlympicAthletes_0.csv")
# In[32]:
project.describe()
    
# In[34]:
num=[43, 43, 55, 13, 489, 3, 5]
# In[36]:
blue=[34, 24, 65, 43, 32, 41, 90]
# In[58]:
categorical=(num, blue)
# In[59]:
ps.value_counts(categorical)
# In[46]:
pref= {43: 'like', 65:'like', 13:'like', 489:'like', 3:'dislike', 5:'dislike'}
# In[47]:
categorical['pref']=categorical['num'].map(pref)
# In[48]:
categorical
# In[54]:
categorical.map([45,34,21,65,33,33])
# In[61]:
project2 = project.rename(columns = {'Year': 'Competition Year', 'Total Medals':'Total'})
                
                
# In[62]:
project2.describe()
# In[73]:
sampler = np.random.permutation(4314)
# In[74]:
sampler2 = np.random.permutation(4314)
# In[75]:
fifty_df = project2.take(sampler)
# In[76]:
fifty2_df = project2.take(sampler2)
# In[77]:
fifty3_df = fifty_df.combine_first(fifty2_df)
# In[78]:
fifty3_df.drop_duplicates()
# In[79]:
fifty3_df
#I still have %50 of rows left, all 4314 exist. 