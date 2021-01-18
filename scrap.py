import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

def StockPrice(Company_Name):
    
    # Company_Name = input()

    url = 'http://www.nepalstock.com/todaysprice?stock-symbol=' + Company_Name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    s = soup.find(id='home-contents').getText().split('\n\n\n')
    
    data = s[5]

    data_array = data.split('\n')
    if(data_array[0] == 'No Data Available!'):
        return 'Enter valid keyword!'
    data_array.remove(data_array[0])
    data_array.remove(data_array[len(data_array)-1])

    lis = []

    lis.append(data_array[1])
    lis.append(data_array[2])
    lis.append(data_array[3])
    lis.append(data_array[4])
    lis.append(data_array[5])
    lis.append(data_array[6])
    lis.append(data_array[7])
    last = data_array[8]
    lis.append(last[:len(last)-1])

    Nam = s[5]
    NName = Nam.split('\n')
    Name = NName[1]
    
    dic = {"Company's_Name" : Name,
      "No_Of_Transaction": data_array[1],
      "Max_Price": data_array[2],
      "Min_Price":data_array[3],
      "Closing_Price":data_array[4],
      "Trade_Shares":data_array[5],
      "Amount":data_array[6],
      "Previous_Closing":data_array[7],
      "Difference":last[:len(last)-1]}
    
    return dic
    
#print(StockPrice())
