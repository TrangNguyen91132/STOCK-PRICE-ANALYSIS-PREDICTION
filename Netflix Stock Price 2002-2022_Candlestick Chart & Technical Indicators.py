#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system(' pip install plotly')


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.graph_objects as go


df = pd.read_csv("D:/DATA ANALYST PORTFOLIO PROJECT/STOCK PRICE FORECAST/Netflix Stock Price Data set 2002-2022.csv")
df


# In[11]:


#Calculate Simple Moving Average (SMA) for 30 days
df['SMA for 30 days'] = df['Close'].rolling(30).mean()

#Calculate Cumulative Moving Average (CMA) for 30 days
df['CMA for 30 days'] = df['Close'].expanding(30).mean()

#Calculate Exponential Moving Average (EMA) for 30 days
df['EMA for 30 days'] = df['Close'].ewm(30).mean()


# In[27]:


candlestick = go.Candlestick(x = df['Date'],
                             open = df['Open'],
                             high = df['High'],
                             low = df['Low'],
                             close = df['Close'],
                             increasing_line_color = 'green',
                             decreasing_line_color = 'red')
sma = go.Scatter(x= df['Date'],
                 y= df['SMA for 30 days'],
                 yaxis= "y1",
                 name= "SMA",
                 line_color = 'cyan')
ema = go.Scatter(x= df['Date'],
                 y = df["EMA for 30 days"],
                 name = "EMA",
                 line_color = 'purple')
cma = go.Scatter(x= df['Date'],
                 y= df['CMA for 30 days'],
                 name= 'CMA',
                 line_color = "lime")
fig = go.Figure(data = [candlestick, sma, ema, cma])
fig.update_layout( width = 1000, height = 600,
                title = 'Netflix Stock_Candlestick', 
                  yaxis_title = 'NFLX Stock')
fig.show()


# In[18]:


#Calculate Relative Strength Index (RSI) for 30 days
change = df['Close'].diff()
change.dropna(inplace=True)

## Create 2 copies of Closing Price
change_up = change.copy()
change_down = change.copy()

change_up[change_up < 0] = 0
change_down[change_down > 0] = 0

##Calculate the rolling average of avg_up and avg_dn for 30 days
avg_up_30days = change_up.rolling(30).mean()
avg_down_30days = change_down.rolling(30).mean().abs()

##Calculate RSI
df['RSI'] = avg_up_30days * 100 / (avg_up_30days + avg_down_30days)
print(rsi)


# In[24]:


# Create two charts on the same figure.
plt.figure(figsize=(20,8))
ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)

# Plot the closing price on the first chart
ax1.plot(df['Date'],
         df['Close'],
         color = 'orange')
ax1.set_ylabel('Stock Price')
ax1.set_title('Netflix Close Price', loc= 'left', y=0.85, x=0.02, fontsize='medium')
ax1.xaxis.set_major_locator(plt.MaxNLocator(30))
ax1.tick_params(axis='x', labelrotation=45, labelsize=8)
ax1.grid(True)

# Plot the RSI on the second chart
ax2.plot(df['Date'], df['RSI'],
         color = 'cyan', linewidth = 1)
ax2.set_title('Relative Strength Index', loc= 'left', y=0.85, x=0.02, fontsize='medium')
ax2.set_ylabel('RSI')
ax2.xaxis.set_major_locator(plt.MaxNLocator(30))
ax2.tick_params(axis='x', labelrotation=45, labelsize=8)
ax2.grid(True)

# Add two horizontal lines, signalling the buy and sell ranges.
# Oversold
ax2.axhline(30, linestyle='--', linewidth=1.5, color='green')
# Overbought
ax2.axhline(70, linestyle='--', linewidth=1.5, color='red')
ax2.grid(True)
plt.show()


# In[ ]:




