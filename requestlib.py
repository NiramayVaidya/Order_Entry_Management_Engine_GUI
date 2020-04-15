import requests, json

buyURL = "http://localhost:5000/orders/buy"
sellURL = "http://localhost:5000/orders/sell"
modURL = "http://localhost:5000/orders/modify"
statusURL = "http://localhost:5000/orders/status"

"""
example call for buyRequest:

data = readJSONFile(format.json)
response = buyRequest(data)

Here response is in 
[
    {
    "errno" : "value",
    "error" : "value",
    }
]
format
"""

def readJSONFile(filename):
    """
    input parameter is the name of json object file outputted via SQL
    """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data


def buyRequest(dataObj):
    """
    input parameter is 
    the object outputted from readJSONFile
    or
    any python object in the buyFormat
    """
    URL = buyURL
    payload = dataObj
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    resp = requests.post(URL, json=payload, headers=headers)
    print(resp.text)
    retData = resp.json()
    return retData

def sellRequest(dataObj):
    """
    input parameter is 
    the object outputted from readJSONFile
    or
    any python object in the sellFormat
    """
    URL = sellURL
    payload = dataObj
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    resp = requests.post(URL, json=payload, headers=headers)
    print(resp.text)
    retData = resp.json()
    return retData

def modRequest(dataObj):
    """
    input parameter is 
    the object outputted from readJSONFile
    or
    any python object in the modFormat
    """
    URL = modURL
    payload = dataObj
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    resp = requests.post(URL, json=payload, headers=headers)
    print(resp.text)
    retData = resp.json()
    return retData

def orderStatusPing(transactionID, exchange):
    """
    input parameters are transactionID, exchange
    """
    URL = statusURL
    dataObj = [{"transactionID" : str(transactionID), "exchange" : str(exchange)}]
    payload = dataObj
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    resp = requests.post(URL, json=payload, headers=headers)
    print(resp.text)
    retData = resp.json()
    return retData


def main():
    pass

if __name__ == "__main__":
    main()
    pass
