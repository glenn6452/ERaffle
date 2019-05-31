#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np
import pandas as pd


# In[66]:


df = pd.read_csv('sample.csv')
df.head()


# In[67]:


# Declartion of the Dataset per RDS POS
RDS00001=df.loc[df['pos_code']=='RDS00001']
RDS00002=df.loc[df['pos_code']=='RDS00002']
RDS00003=df.loc[df['pos_code']=='RDS00003']
RDS00004=df.loc[df['pos_code']=='RDS00004']
RDS00005=df.loc[df['pos_code']=='RDS00005']
RDS00006=df.loc[df['pos_code']=='RDS00006']
RDS00007=df.loc[df['pos_code']=='RDS00007']
RDS00008=df.loc[df['pos_code']=='RDS00008']
RDS00009=df.loc[df['pos_code']=='RDS00009']
RDS00010=df.loc[df['pos_code']=='RDS00010']
RDS00011=df.loc[df['pos_code']=='RDS00011']
RDS00012=df.loc[df['pos_code']=='RDS00012']
RDS00013=df.loc[df['pos_code']=='RDS00013']
RDS00014=df.loc[df['pos_code']=='RDS00014']
RDS00015=df.loc[df['pos_code']=='RDS00015']
RDS00016=df.loc[df['pos_code']=='RDS00016']


# In[68]:


#Declaring the ticket_code to be evaluated for the raffle 
RDS00001_ENTRIES=RDS00001.ticket_code
RDS00002_ENTRIES=RDS00002.ticket_code
RDS00003_ENTRIES=RDS00003.ticket_code
RDS00004_ENTRIES=RDS00004.ticket_code
RDS00005_ENTRIES=RDS00005.ticket_code
RDS00006_ENTRIES=RDS00006.ticket_code
RDS00007_ENTRIES=RDS00007.ticket_code
RDS00008_ENTRIES=RDS00008.ticket_code
RDS00009_ENTRIES=RDS00009.ticket_code
RDS00010_ENTRIES=RDS00010.ticket_code
RDS00011_ENTRIES=RDS00011.ticket_code
RDS00012_ENTRIES=RDS00012.ticket_code
RDS00013_ENTRIES=RDS00013.ticket_code
RDS00014_ENTRIES=RDS00014.ticket_code
RDS00015_ENTRIES=RDS00015.ticket_code
RDS00016_ENTRIES=RDS00016.ticket_code


# In[69]:


#Declaring the ticket_code to be evaluated for the raffle 
RDS00001_ENTRIES=RDS00001.ticket_code
RDS00002_ENTRIES=RDS00002.ticket_code
RDS00003_ENTRIES=RDS00003.ticket_code
RDS00004_ENTRIES=RDS00004.ticket_code
RDS00005_ENTRIES=RDS00005.ticket_code
RDS00006_ENTRIES=RDS00006.ticket_code
RDS00007_ENTRIES=RDS00007.ticket_code
RDS00008_ENTRIES=RDS00008.ticket_code
RDS00009_ENTRIES=RDS00009.ticket_code
RDS00010_ENTRIES=RDS00010.ticket_code
RDS00011_ENTRIES=RDS00011.ticket_code
RDS00012_ENTRIES=RDS00012.ticket_code
RDS00013_ENTRIES=RDS00013.ticket_code
RDS00014_ENTRIES=RDS00014.ticket_code
RDS00015_ENTRIES=RDS00015.ticket_code
RDS00016_ENTRIES=RDS00016.ticket_code


# In[70]:


# Declaring the winners for each RDS POS
#RDS00001_WINNERS=np.random.choice(RDS00001_ENTRIES, 2, replace=False)
RDS00002_WINNERS=np.random.choice(RDS00002_ENTRIES, 2, replace=False)
#RDS00003_WINNERS=np.random.choice(RDS00003_ENTRIES, 2, replace=False)
#RDS00004_WINNERS=np.random.choice(RDS00004_ENTRIES, 2, replace=False)
#RDS00005_WINNERS=np.random.choice(RDS00005_ENTRIES, 2, replace=False)
#RDS00006_WINNERS=np.random.choice(RDS00006_ENTRIES, 2, replace=False)
#RDS00007_WINNERS=np.random.choice(RDS00007_ENTRIES, 2, replace=False)
#RDS00008_WINNERS=np.random.choice(RDS00008_ENTRIES, 2, replace=False)
#RDS00009_WINNERS=np.random.choice(RDS00009_ENTRIES, 2, replace=False)
#RDS00010_WINNERS=np.random.choice(RDS00010_ENTRIES, 2, replace=False)
RDS00011_WINNERS=np.random.choice(RDS00011_ENTRIES, 2, replace=False)
#RDS00012_WINNERS=np.random.choice(RDS00012_ENTRIES, 2, replace=False)
#RDS00013_WINNERS=np.random.choice(RDS00013_ENTRIES, 2, replace=False)
#RDS00014_WINNERS=np.random.choice(RDS00014_ENTRIES, 2, replace=False)
#RDS00015_WINNERS=np.random.choice(RDS00015_ENTRIES, 2, replace=False)
#RDS00016_WINNERS=np.random.choice(RDS00016_ENTRIES, 2, replace=False)


# In[ ]:





# In[71]:


ALL_WINNERS = np.concatenate((#RDS00001_WINNERS,
RDS00002_WINNERS,
#RDS00003_WINNERS,
#RDS00004_WINNERS,
#RDS00005_WINNERS,
#RDS00006_WINNERS,
#RDS00007_WINNERS,
#RDS00008_WINNERS,
#RDS00009_WINNERS,
#RDS00010_WINNERS,
RDS00011_WINNERS#,
#RDS00012_WINNERS,
#RDS00013_WINNERS,
#RDS00014_WINNERS,
#RDS00015_WINNERS,
#RDS00016_WINNERS
),axis=0)
ALL_WINNERS


# In[72]:


RDS00011_WINNERS


# In[73]:


winners = df.loc[df['ticket_code'].isin(ALL_WINNERS)]
winners


# In[74]:


winners.to_csv('winners.csv')


# In[ ]:




