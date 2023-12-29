#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("D:/DATA ANALYST PORTFOLIO PROJECT/STOCK PRICE FORECAST/Netflix Stock Price Data set 2002-2022.csv")


# In[2]:


get_ipython().system('pip install prophet')


# In[15]:


#PRICE FORECASTING BY PROPHET
from prophet import Prophet
from prophet.plot import plot
from prophet.plot import add_changepoints_to_plot

##Split Date
df['Date'] = pd.to_datetime(df['Date'])
min_date = pd.to_datetime(df['Date']).min()
max_date = pd.to_datetime(df['Date']).max()

split_date = '2019-12-31'


train_time = df['Date'] <= split_date
test_time = df['Date'] > split_date

##Rename columns: 'Date' as datastamp (ds) and 'Close' as target variable (y)
train_data = df[train_time][['Date', 'Close']].rename(columns = {'Date' : 'ds', 'Close' : 'y'})
test_data = df[test_time][['Date', 'Close']].rename(columns = {'Date' : 'ds', 'Close' : 'y'})

#Fit model
model = Prophet()
model.fit(train_data)

#Generate Prediction using fitting model
future = model.make_future_dataframe(periods= 3650)
forecast = model.predict(future)
print(forecast)


# In[19]:


#Visualize the prediction
fig = model.plot(forecast)
plt.scatter(train_data['ds'],
            train_data['y'],
            color = 'blue',
            label = 'Train Data')
plt.scatter(test_data['ds'],
            test_data['y'],
            color = 'orange',
            label = 'Test Data')
a = add_changepoints_to_plot(fig.gca(), model, forecast)
plt.title('Netflix Stock Price Forecast with Prophet')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()


# In[ ]:




