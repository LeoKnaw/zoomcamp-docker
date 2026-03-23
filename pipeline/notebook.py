#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[46]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
df_iter = pd.read_csv(url, chunksize=100000, iterator=True)


# In[47]:


from tqdm.auto import tqdm


# In[49]:


get_ipython().system('uv add sqlalchemy')


# In[50]:


get_ipython().system('uv add psycopg2-binary')


# In[51]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[52]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[54]:


for df in tqdm(df_iter):
    df.to_sql(name="yellow_Taxi", con=engine, if_exists="append")


# In[ ]:




