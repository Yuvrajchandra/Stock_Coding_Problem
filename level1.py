import requests
from numpy import mean
import yfinance as yf
import time
API1 = {"X-Api-Key": "YX%d6$7waWCQ#G6u8$@BlC%WQ!WPJAGsy3_vl4N9XB7C9Mo23cP56Jl!HZrQhsW6"}    #API key for Endpoint 1
API2= {"X-Api-Key": "F5%wnQP97E6ffD_RVzef!!3z-C@ue#uU#%RO0masY_uYPIM3R10$m2Ebrl0qKSPI"}     #API key for Endpoint 2


res = requests.get('https://sheet.best/api/sheets/c4004fdb-71a4-479c-866f-9f810072a9b3',headers=API1)

response = res.json()
length = len(response)      #To find total items from data received from get request
ticker_names=[]             #LIST to store all ticker names
purchase_price=[]           #LIST to store purchase price of all TICKER
average_close_price=[]      #LIST to store average closing price of each TICKER for each month

for i in range(length):
        ticker_names.append(response[i]['ticker'])
        purchase_price.append(int(response[i]["purchasePrice"]))
print("Data received from get request:")
print(res.text)
# print(ticker_names)
# print(purchase_price)

###################################  MICROSOFT ###############################################
MSFT = yf.Ticker('MSFT')
close_MSFT=MSFT.history(start="2020-05-16", end="2020-06-16",interval="1d")
avg_close_MSFT=mean(close_MSFT['Close'])
# print(avg_close_MSFT)
average_close_price.append(avg_close_MSFT)

###################################  HUBS ###############################################
HUBS = yf.Ticker('HUBS')
close_HUBS=HUBS.history(start="2020-05-16", end="2020-06-16",interval="1d")
avg_close_HUBS=mean(close_HUBS['Close'])
# print(avg_close_HUBS)
average_close_price.append(avg_close_HUBS)

###################################  CRM ###############################################
CRM = yf.Ticker('CRM')
close_CRM=CRM.history(start="2020-05-16", end="2020-06-16",interval="1d")
avg_close_CRM=mean(close_CRM['Close'])
# print(avg_close_CRM)
average_close_price.append(avg_close_CRM)

###################################  WORK ###############################################
WORK = yf.Ticker('WORK')
close_WORK=WORK.history(start="2020-05-16", end="2020-06-16",interval="1d")
avg_close_WORK=mean(close_WORK['Close'])
# print(avg_close_WORK)
average_close_price.append(avg_close_WORK)

###################################  GOOGL ###############################################
GOOGL = yf.Ticker('GOOGL')
close_GOOGL=GOOGL.history(start="2020-05-16", end="2020-06-16",interval="1d")
avg_close_GOOGL=mean(close_GOOGL['Close'])
# print(avg_close_GOOGL)
average_close_price.append(avg_close_GOOGL)


# print(average_close_price)
print("Data posted through post request:")


for i in range (length):
    if purchase_price[i] > average_close_price[i]:
        timestamp = int(time.time()*1000.0)
        post_data={
        "name": "Yuvraj",
        "ticker": ticker_names[i],
        "purchasePrice": purchase_price[i],
        "average": average_close_price[i],
        "shouldSell": "false",
        "createdAt": timestamp
        }
        postrequest= requests.post("https://sheet.best/api/sheets/fec49be9-d3f0-4a08-bc38-5104ef9a2faf",headers=API2,data=post_data)

        print(postrequest.text)



    else:
        timestamp = int(time.time()*1000.0)
        post_data={
        "name": "Yuvraj",
        "ticker": ticker_names[i],
        "purchasePrice": purchase_price[i],
        "average": average_close_price[i],
        "shouldSell": "true",
        "createdAt": timestamp
        }
        postrequest= requests.post("https://sheet.best/api/sheets/fec49be9-d3f0-4a08-bc38-5104ef9a2faf",headers=API2,data=post_data)

        print(postrequest.text)
