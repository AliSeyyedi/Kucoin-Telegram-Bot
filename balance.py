import headers as H
import requests
import account
import json

endpoint = '/api/v1/accounts?currency=ETH&type=main'
method = 'GET'

def getBalance():
    headers = H.getHeaders(method, endpoint)
    Balance = requests.get(account.url + endpoint, headers=headers).json()
    Balance = (Balance.get('data'))
    Balance = Balance[0]
    Balance = json.dumps(Balance)
    Balance = json.loads(Balance)
    currency      = str(Balance['currency'])
    acctype       = str(Balance['type'])
    balance       = str(Balance['balance'])
    available     = str(Balance['available'])
    holds         = str(Balance['holds'])
    output = (currency+ '\nAcc typeg: '+ acctype + '\nBalance: '+ balance+ '\nAvailable: '+ available+ '\nHolds: '+ holds)
    return output
