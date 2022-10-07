import headers as H
import requests
import account
import json
from datetime import datetime

endpoint = '/api/v1/margin/lend/trade/settled?currency=ETH&currentPage=1&pageSize=50'
method = 'GET'

def getSettledOrders():
    headers = H.getHeaders(method, endpoint)
    getSettledOrders = requests.get(account.url + endpoint, headers=headers).json()
    getSettledOrders = (getSettledOrders.get('data'))
    getSettledOrders = getSettledOrders["items"]
    output = ''
    for i in range (0 ,len(getSettledOrders)):
        orders = getSettledOrders[i]
        orders = json.dumps(orders)
        orders = json.loads(orders)
        currency        = str(orders['currency'])
        size            = str(orders['size'])
        interest        = str(orders['interest'])
        repaid          = str(orders['repaid'])
        dailyIntRate    = str(orders['dailyIntRate'])
        settledAt       = int(orders['settledAt'])
        settledAt    = settledAt / 1000
        # tz = pytz.timezone('Asia/Tehran')
        settledAt    = str(datetime.utcfromtimestamp(settledAt).strftime('%Y-%m-%d %H:%M:%S'))
        output = output + ('\n\n'+ str(i+1)+ '.\nCurrency: ' + currency+ '\nSize: '+ size+ '\nInterest: '+ interest + '\nRepaid: '+ repaid+ '\nDaily Int Rate: '+ dailyIntRate+ '\nSettled At: '+ settledAt)
    return output
