import requests
import json

def marketvalue(symbl):
    keys =["title","tradecompany","nooftransaction","maxprice","minprice","closingprice","tradedshares","amount","previousclosing","difference"]
    response = requests.get("https://webscraping-nepalstock.herokuapp.com/companyprice.php?symbol={}".format(symbl))
    print(response.status_code)
    data = response.json()
    load_data=json.dumps(data)
    new=json.loads(load_data)
    result = ""
    for i in range(len(keys) - 1):
        if(i):
            result += keys[i]
            result += " : "
            result += new[0][keys[i]]
            result += "\n"
    result += keys[-1] + " : "
    tempS = len(new[0][keys[-1]])
    result += new[0][keys[-1]][:tempS-6]
    return result