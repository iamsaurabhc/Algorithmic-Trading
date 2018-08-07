#%%
# Load the data
import quandl
quandl.ApiConfig.api_key = 'scKH99KZRUe1Eej-PX9Y'
tataMotors = quandl.get('NSE/TATAMOTORS')
#%%
print tataMotors.columns

#%%
tataMotors['Pivot'] = (tataMotors['High'] + tataMotors['Close'] + tataMotors['Low']) / 3 

#%%
tataMotors['Resistence1'] = ( 2 * tataMotors['Pivot'] ) - tataMotors['Low']
tataMotors['Support1'] = ( 2 * tataMotors['Pivot'] ) - tataMotors['High']

tataMotors['Resistence2'] = tataMotors['Pivot'] + (tataMotors['Resistence1'] - tataMotors['Support1'])
tataMotors['Support2'] = tataMotors['Pivot'] - (tataMotors['Resistence1'] - tataMotors['Support1'])

#%%
import keras