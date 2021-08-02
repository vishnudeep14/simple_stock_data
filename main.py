from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.cryptocurrencies import CryptoCurrencies

api_key='AMQ79GFML2H6Z5ZV'
fd=FundamentalData(key=api_key,output_format='pandas')
data=fd.get_income_statement_annual('INFY')
print(data[0].T)

cr=CryptoCurrencies(key=api_key,output_format='pandas')
cd=cr.get_digital_currency_weekly('ETH','INR')
print(cd)

ts= TimeSeries(key=api_key,output_format='pandas')
data_ts,meta_data=ts.get_intraday(symbol='INFY',interval='1min',outputsize='full')
print(data_ts)

period=60
ti=TechIndicators(key=api_key,output_format='pandas')
data_ti,meta_data_ti=ti.get_sma(symbol='INFY',interval='1min',time_period=period,series_type='close')




df1=data_ti
df2=data_ts['4. close'].iloc[period-1::]
df2.index=df1.index
total=pd.concat([df1,df2],axis=1)
print(total)
total.plot()
plt.show()




