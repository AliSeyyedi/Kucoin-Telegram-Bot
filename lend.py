import headers as H
import requests
import account
import json

endpoint = '/api/v1/margin/lend'
method = 'POST'

def PlaceEthLendOrder():
  params = {
    'currency'      : 'ETH' ,
    'size'          : 'All' ,
    'dailyIntRate'  : '0.002',
    'term'          : '7'
  }
  data = json.dumps(params)
  headers = H.getHeaders(method, endpoint+data)
  PlaceEthLendOrder = requests.post(account.url + endpoint, data=data, headers=headers).json()
  print(PlaceEthLendOrder)
  # PlaceEthLendOrder = (PlaceEthLendOrder.get('data'))
  # PlaceEthLendOrder = json.dumps(PlaceEthLendOrder)
  # PlaceEthLendOrder = json.loads(PlaceEthLendOrder)
  # PlaceEthLendOrder = PlaceEthLendOrder["orderId"]
  # PlaceEthLendOrder = str(PlaceEthLendOrder)
  return PlaceEthLendOrder
