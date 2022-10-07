import headers as H
import requests
import account
import json

endpoint =  '/api/v1/margin/lend/trade/unsettled?currency=ETH&currentPage=1&pageSize=50'
method = 'GET'

def getUnsettledOrders():
    headers = H.getHeaders(method, endpoint)
    getUnsettledOrders = requests.get(account.url + endpoint, headers=headers).json()
    getUnsettledOrders = (getUnsettledOrders.get('data'))
    getUnsettledOrders = getUnsettledOrders["items"]
    output = ''
    for i in range (0 ,len(getUnsettledOrders)):
        orders = getUnsettledOrders[i]
        orders = json.dumps(orders)
        orders = json.loads(orders)
        currency        = str(orders['currency'])
        size            = str(orders['size'])
        accruedInterest = str(orders['accruedInterest'])
        repaid          = str(orders['repaid'])
        dailyIntRate    = str(orders['dailyIntRate'])
        maturityTime    = int(orders['maturityTime'])
        maturityTime    = maturityTime / 1000
        tz = pytz.timezone('Asia/Tehran')
        maturityTime    = str(datetime.utcfromtimestamp(maturityTime).strftime('%Y-%m-%d %H:%M:%S'))
        output = ('\n\n'+ str(i+1)+ '.\ncurrency: '+ currency+ '\nSize: '+ size+ '\nAccrued Interest: '+ accruedInterest + '\nRepaid: '+ repaid+ '\nDaily Int Rate: '+ dailyIntRate+ '\nMaturity Time: '+ maturityTime)
    return output
