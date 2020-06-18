import requests
import yfinance as yf
from numpy import mean
import datetime



####################### Getting Purchased At Date from Endpoint 1 ############################
API = {"X-Api-Key": "YX%d6$7waWCQ#G6u8$@BlC%WQ!WPJAGsy3_vl4N9XB7C9Mo23cP56Jl!HZrQhsW6"}
res = requests.get('https://sheet.best/api/sheets/c4004fdb-71a4-479c-866f-9f810072a9b3',headers=API)
response = res.json()
purchasedAt= int(response[1]["purchasedAt"])
date = datetime.datetime.fromtimestamp(purchasedAt/1000.0)
date = date.strftime('%Y-%m-%d')



############################# Getting data for TICKER ################################
HUBS = yf.Ticker('HUBS')
data=HUBS.history(start="2019-06-06", end="2020-05-06",interval="1wk")
data2=HUBS.history(start="2020-05-06", end="2020-06-06",interval="1wk")


############################ Dropping Not a Number Values ############################
data=data.dropna()              #To drop NaN values
data2=data2.dropna()            #To drop NaN values


############################ Printing the received Data ##############################
print(data['Close'])
print(data2['Close'])


######################## Calculating average for last 1 month ########################
average=mean(data2['Close'])
print(average)




################################# Plotting The Graph #######################################
import matplotlib.pyplot as plt


plt.title("HUBS: 06/06/2019-06/06/2020", fontsize=16)
plt.ylabel('Close')
plt.xlabel('Date')
plt.tick_params(labelright=True)
data['Close'].plot()
data2['Close'].plot(label="Last 1 Month")


plt.axhline(y=average,label="One month Average", linestyle='--',color="black")
plt.axvline(x=date,label="Buy Date",color="red")
legend = plt.legend(loc='best',title="Measure Names")
plt.show()
