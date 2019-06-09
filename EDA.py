#!/usr/bin/env python
# coding: utf-8

# In[66]:


# importing the required libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().system(' pip install plotly --upgrade')
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)


# In[6]:


# Importing BenefitsCostSharing dataset

BCS_df = pd.read_csv("BenefitsCostSharing.csv")


# In[7]:


# Displaying the first 10 rows of our dataset

BCS_df.head(10)


# In[11]:


# Replacing empty records with NaN

BCS_df = BCS_df.fillna(np.nan)

# Looking for the null values

BCS_df.isnull().sum()


# In[17]:


# Checking the total number of rows in our dataset

len(BCS_df)


# In[16]:


# Unique Benefits in the dataset

BCS_df.BenefitName.nunique()


# In[18]:


# Summarizing our dataset

BCS_df.describe()


# In[21]:


# Top Benefits Year Wise

BCS_df[["BusinessYear", "BenefitName"]].groupby('BusinessYear').describe()


# In[22]:


# Analyzing the benefits State wise

BCS_df[["StateCode","BenefitName"]].groupby('StateCode').count().sort_values('BenefitName')


# In[26]:


# Unique States

State_unique = BCS_df.StateCode.unique()
State_unique


# In[30]:


# Creating a new array for Visualization

BCS_array = []
for state in State_unique:
    BCS_state = len(BCS_df[BCS_df["StateCode"]== state])
    BCS_array.append(BCS_state)

BCS_array


# In[41]:


BCS_new = pd.DataFrame(
        { 'State' : State_unique,
         'Count' : BCS_array
        })

BCS_new = BCS_new.sort_values("Count", ascending=False).reset_index(drop=True)

f, ax = plt.subplots(figsize=(15, 15))
ax.set_yticklabels(State_unique, rotation='horizontal', fontsize='large')
g = sb.barplot(y = BCS_new.State, x = BCS_new.Count)
plt.show


# In[117]:


scl = [
    [0.0, 'rgb(255,228,225)'],
    [0.2, 'rgb(255,182,193)'],
    [0.4, 'rgb(255,174,185)'],
    [0.6, 'rgb(238,162,173)'],
    [0.8, 'rgb(205,140,149)'],
    [1.0, 'rgb(139,95,101)']
]


data = dict(type = 'choropleth',
           locations = BCS_new['State'],
           locationmode = 'USA-states',
           colorscale = scl,
            text = BCS_new['State'],
            marker = dict (line = dict(color = 'rgb(255,255,255)',width=2)),
           z = BCS_new['Count'],
           colorbar = {'title':'No of Benefit plans'})

layout = dict(title = 'Benefit Plans across different States of USA',
         geo=dict(scope = 'usa',showlakes = True,lakecolor='rgb(85,173,240)')) 

choromap2 = go.Figure(data = [data],layout=layout)
iplot(choromap2)

