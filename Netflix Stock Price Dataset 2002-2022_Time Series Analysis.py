#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np 
import seaborn as sns
import datetime as dt 
import matplotlib.pyplot as plt

df = pd.read_csv("D:/DATA ANALYST PORTFOLIO PROJECT/STOCK PRICE FORECAST/Netflix Stock Price Data set 2002-2022.csv")


# In[7]:


#CHECK DATA
df.info()


# In[8]:


#CHECK DATA
df.head()


# In[9]:


#CHECK DATA
df.describe()


# In[23]:


#TIME SERIES ANALYSIS
##1.VISUALIZE NETFLIX STOCK PRICE OVER TIME
plt.figure(figsize= (20,8))
sns.lineplot(data = df,
             x= 'Date',
             y= 'Close',
             color = 'green')
plt.title('NETFLIX STOCK PRICE OVER TIME')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.subplot().xaxis.set_major_locator(plt.MaxNLocator(40))
plt.xticks(rotation = 45, fontsize = 'small')
plt.grid()
plt.show()


# In[24]:


##2.VISUALIZE NETFLIX VOLUME OVER TIME
plt.figure(figsize=(20,8))
sns.barplot(data=df,
             x= 'Date',
             y= 'Volume',
             color= 'gold')
plt.title('NETFLIX VOLUME OVER TIME')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.subplot().xaxis.set_major_locator(plt.MaxNLocator(40))
plt.xticks(rotation = 45, fontsize = 'small')
plt.grid()
plt.show()


# In[25]:


##3. DAILY MARKET CAPITALIZATION OVER TIME
df['Market Cap'] = df['Open'] * df['Volume']
plt.figure(figsize=(20,8))
sns.lineplot(data=df,
            x= 'Date',
            y= 'Market Cap',
            color= 'purple')
plt.title('DAILY MARKET CAPITALIZATION OVER TIME')
plt.xlabel('Date')
plt.ylabel('Market Capitalization')
plt.subplot().xaxis.set_major_locator(plt.MaxNLocator(40))
plt.xticks(rotation = 45, fontsize = 'small')
plt.grid()
plt.show()


# In[18]:


##4. DAILY VOLTALITY OVER TIME
df['pre_Close'] = df['Close'].shift(1)
df['Voltality'] = df['Close']/df['pre_Close'] -1
df[['Close', 'pre_Close', 'Voltality']]


# In[26]:


plt.figure(figsize=(20,9))
sns.lineplot(data=df,
             x= 'Date',
             y= 'Voltality',
             color= 'cyan')
plt.title('DAILY VOLTALITY OVER TIME')
plt.xlabel('Date')
plt.ylabel('Voltality')
plt.xticks(rotation = 45, fontsize = 'small')
plt.subplot().xaxis.set_major_locator(plt.MaxNLocator(40))
plt.grid()
plt.show()


# In[20]:


##5. DAILY CUMULATIVE RETURN 
df['Return'] = df['Close'].pct_change()
df['Cumulative Return'] = (1+df['Return']).cumprod()
df[['Return', 'Cumulative Return']]


# In[35]:


plt.figure(figsize=(20,8))
sns.barplot(data=df,
            x= 'Date',
            y= 'Cumulative Return',
            color = 'green')
plt.title('DAILY CUMULATIVE RETURN OVER YEAR')
plt.xlabel('Date')
plt.ylabel('Cum Return')
plt.xticks(rotation = 45, fontsize = 'small')
plt.subplot().xaxis.set_major_locator(plt.MaxNLocator(30))
plt.grid()
plt.show()


# In[32]:


##6. AVERAGE MONTHLY RETURN
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

monthly_return = df.groupby(df['Month'])['Return'].mean().reset_index()

plt.figure(figsize=(20,8))
sns.barplot(data=monthly_return,
            x= 'Month',
            y= 'Return')
plt.title('AVERAGE MONTHLY RETURN')
plt.show()


# In[34]:


##7. AVERAGE YEARLY RETURN
df['Year'] = df['Date'].dt.year
yearly_return = df.groupby(df['Year'])['Return'].mean().reset_index()


plt.figure(figsize=(20,8))
sns.barplot(data=yearly_return,
            x= 'Year',
            y= 'Return')
plt.title('AVERAGE YEARLY RETURN')
plt.show()


# In[42]:


##8. AVERAGE RETURN BY WEEKDAY
df['Weekday'] = df['Date'].dt.weekday
yearly_return = df.groupby(df['Weekday'])['Return'].mean().reset_index()


plt.figure(figsize=(6,4))
sns.barplot(data=yearly_return,
            x= 'Weekday',
            y= 'Return')
plt.title('AVERAGE RETURN BY WEEKDAY')
plt.show()


# In[37]:


##9. MOVING AVERAGE 
df['MA for 10 days'] = df['Close'].rolling(10).mean()
df['MA for 20 days'] = df['Close'].rolling(20).mean()
df['MA for 50 days'] = df['Close'].rolling(50).mean()
df['MA for 100 days'] = df['Close'].rolling(100).mean()

plt.figure(figsize=(20,8))
df[['MA for 10 days', 'MA for 20 days', 'MA for 50 days', 'MA for 100 days', 'Adj Close']].plot(figsize = (20,8))
plt.title('MOVING AVERAGE AND ADJUST CLOSE PRICE')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




