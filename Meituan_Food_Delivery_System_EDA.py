#!/usr/bin/env python
# coding: utf-8

# ![Description of image](https://miro.medium.com/v2/resize:fit:1200/1*9Dghz51bt8C-nNFMkyokMw.png)
# 

# ## Introduction
# In this phase we are doing EDA for the datasets of Meituan food delivery system. 
# The content of the notebook will be executed on the three data files first

# ### Loading packages

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## File No.1 "dispatch waybill meituan.csv" Analysis
# - This dataset contains information about the orders available for dispatch at a given time

# ### Loading file 

# In[2]:


df_wb = pd.read_csv("C://Users//yymahmoudali//Downloads//DS_Task//dispatch_waybill_meituan.csv")
df_wb.head()


# In[3]:


"""
dt : Date of dispatch
dispatch_time : Unix timestamp when the order was considered for assignment
order_id : Unique anonymized ID of the order
"""


# ### Data overview

# In[4]:


# Get the count of rows
record_count = len(df_wb)
print(f"Total records: {record_count}")


# In[5]:


# Data Overview 
print("Dataset Info:\n")
df_wb.info()


# In[6]:


print("\nStatistical Summary:\n")
print(df_wb.describe())


# ### Data cleaning

# In[7]:


# Remove the "Unnamed" column cause it does not hold important data
df_wb = df_wb.drop(columns=['Unnamed: 0'])

# Check for duplicates
duplicates = df_wb.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")


# ### Types conversion

# In[8]:


# Convert 'dt' into a proper date format
df_wb['dt'] = pd.to_datetime(df_wb['dt'], format='%Y%m%d')

# Convert 'dispatch_time' from Unix timestamp to human-readable date-time format
df_wb['dispatch_time'] = pd.to_datetime(df_wb['dispatch_time'], unit='s')


# In[9]:


# Show if there is nulls
print("\nMissing Values:\n", df_wb.isnull().sum())


# In[10]:


# No missing Values!


# In[11]:


#Show unique values of the columns 
print("\nUnique Values:\n", df_wb.nunique())


# In[12]:


df_wb.head()


# ### Visualizations

# In[34]:


# Distribution of orders by date
plt.figure(figsize=(15, 10))
df_wb['dt'].value_counts().sort_index().plot(kind='bar', color='#FFDB58')
plt.title('Orders Count by Date')
plt.xlabel('Date')
plt.ylabel('Orders Count')
plt.xticks(ticks=range(len(df_wb['dt'].value_counts())), 
           labels=df_wb['dt'].value_counts().sort_index().index.strftime('%Y-%m-%d'),
           rotation=45)
plt.show()


# In[29]:


colured = "#87CEEB" 
plt.figure(figsize=(10, 6))
df_wb['dispatch_hour'] = df_wb['dispatch_time'].dt.hour
sns.countplot(x='dispatch_hour', data=df_wb, color=colured)
plt.title('Distribution of Dispatch Times by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Count')
plt.show()


# In[15]:


# Orders trend over time
plt.figure(figsize=(12, 6))
df_wb.groupby('dt').size().plot(marker='o', color='#FFDB58')
plt.title('Trend of Orders Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.show()


# In[16]:


# Step 4: Insights and Observations
# Write observations as comments or export results as needed
print("\nKey Insights:")
print("1.Orders count varies per day but the intensity of them is close for everyday.")
print("2.The entire dataset's dispatch times are being grouped under hour 3.")
print("3.The number of orders peaked on October 21st, followed by a sharp drop on October 22nd and a partial recovery on October 23rd.")


# ## File No.2 "dispatch_rider_meituan.csv" Analysis
# - This dataset contains dispatch information, including rider locations, dispatch times, courier IDs, and assigned waybills 
# 

# ### Loading file
# 

# In[17]:


df_r = pd.read_csv("C://Users//yymahmoudali//Downloads//DS_Task//dispatch_rider_meituan.csv")
df_r.head()


# In[18]:


"""
dispatch_rider_meituan.csv
dt: Date of dispatch
rider_lat : Latitude of the courier at dispatch time 
rider_lng : Longitude of the courier at dispatch time 
dispatch_time : 'Unix timestamp' when the dispatch system considered this rider
courier_waybills : List of orders "order num" currently being carried by the courier
courier_id : Unique ID of the courier
"""


# ### Data overview

# In[19]:


# Get the count of rows
record_count = len(df_r)
print(f"Total records: {record_count}")


# In[20]:


print("Dataset Info:\n")
df_r.info()


# In[21]:


print("\nStatistical Summary:\n")
print(df_r.describe())


# ### Data cleaning

# In[22]:


print("\nMissing Values:\n", df_r.isnull().sum())


# In[23]:


#Show unique values of the columns 
print("\nUnique Values:\n", df_r.nunique())


# In[25]:


# Remove the "Unnamed" column cause it does not hold important data
df_r = df_r.drop(columns=['Unnamed: 0'])

# Check for duplicates
duplicates = df_r.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")


# ### Types Conversion

# In[27]:


# Convert 'dt' into a proper date format
df_r['dt'] = pd.to_datetime(df_r['dt'], format='%Y%m%d')

# Convert 'dispatch_time' from Unix timestamp to human-readable date-time format
df_r['dispatch_time'] = pd.to_datetime(df_r['dispatch_time'], unit='s')

# Process 'courier_waybills' to convert from string to list
df_r['courier_waybills'] = df_r['courier_waybills'].apply(eval)


# ### visulizations

# In[30]:


colured = "#87CEEB" 
plt.figure(figsize=(10, 6))
df_wb['dispatch_hour'] = df_r['dispatch_time'].dt.hour
sns.countplot(x='dispatch_hour', data=df_r, color=colured)  # Single yellow color
plt.title('Distribution of Dispatch Times by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Count')
plt.show()


# In[33]:


# Count of couriers dispatched daily
plt.figure(figsize=(15, 10))
df_r.groupby('dt')['courier_id'].nunique().plot(kind='bar', color='#FFDB58')
plt.title('Number of Couriers Dispatched Daily')
plt.xlabel('Date')
plt.ylabel('Number of Couriers')
plt.xticks(ticks=range(len(df_r['dt'].value_counts())), 
           labels=df_r['dt'].value_counts().sort_index().index.strftime('%Y-%m-%d'),
           rotation=45)
plt.show()


# In[37]:


# Rider location scatter plot
plt.figure(figsize=(15, 10))
plt.scatter(df_r['rider_lng'], df_r['rider_lat'], alpha=0.5, c='#FFDB58')
plt.title('Geographic Distribution of Rider Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# In[59]:


print("\nKey Insights:")
print("1. Distribution of Dispatch Times by Hour: Orders peak during specific hours, likely aligning with meal times")
print("2. Number of Orders by Dispatch Day: Daily order volumes appear consistent, indicating stable demand patterns.")
print("3. Geospatial Distribution: High-density clusters of pickup or delivery locations suggest urban hotspots for orders")


# ## File No.3 "all_waybill_info_meituan_0322.csv" Analysis
# - contains detailed information about food delivery orders in Meituan’s system. Each row represents a waybill, which is a record of an order's journey from the restaurant to the customer.

# ### Loading file

# In[40]:


df_orders = pd.read_csv("C://Users//yymahmoudali//Downloads//DS_Task//all_waybill_info_meituan_0322.csv")
df_orders.head()


# ### Data overview

# In[44]:


record_count = len(df_orders)
print(f"Total records: {record_count}")
print("\nStatistical Summary:\n")
print(df_orders.describe())


# In[41]:


display(df_orders.info())


# ### Data cleaning

# In[45]:


print("\nMissing Values:\n", df_orders.isnull().sum())
#Show unique values of the columns 
print("\nUnique Values:\n", df_orders.nunique())
# Remove the "Unnamed" column cause it does not hold important data
df_orders = df_orders.drop(columns=['Unnamed: 0'])

# Check for duplicates
duplicates = df_orders.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")


# ### Types Conversion

# In[42]:


# Convert timestamps to datetime format
for col in ['order_push_time', 'platform_order_time', 'dispatch_time', 'grab_time', 'fetch_time', 'arrive_time']:
    df_orders[col] = pd.to_datetime(df_orders[col], unit='s')


# ### Visulaizations

# In[52]:


# Plot distributions of order processing times
plt.figure(figsize=(15, 10))
sns.histplot(df_orders['dispatch_time'], bins=50, kde=True)
plt.title('Distribution of Dispatch Time')
plt.xlabel('Dispatch Time')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# In[54]:


# Plot distributions of order processing times
plt.figure(figsize=(10, 5))
sns.histplot(df_orders['dispatch_time'], bins=50, kde=True)
plt.title('Distribution of Dispatch Time (Zoomed)')
plt.xlabel('Dispatch Time')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.xlim([df_orders['dispatch_time'].quantile(0.01), df_orders['dispatch_time'].quantile(0.99)])
plt.show()


# In[58]:


plt.figure(figsize=(10, 5))
sns.histplot(df_orders['dispatch_time'], bins=50, kde=True)
plt.title('Distribution of Dispatch Time (Zoomed)')
plt.xlabel('Dispatch Time')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.xlim([df_orders['dispatch_time'].quantile(0.01), df_orders['dispatch_time'].quantile(0.99)])
plt.show()


# In[60]:


print("\nKey Insights:")
print("1. Dispatch times are concentrated within specific time ranges, with most activity aligning with peak operational hours.")
print("2. confirming the concentration around specific periods (such as meal times).")
print("3. Highlighting specific high-demand intervals within the dataset.")


# In[ ]:




