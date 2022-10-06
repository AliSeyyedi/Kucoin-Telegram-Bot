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
  data_json = json.dumps(params)
  newendpoint = endpoint + data_json
  headers = H.getHeaders(method, newendpoint)
  PlaceEthLendOrder = requests.post(account.url + endpoint,data=data_json, headers=headers).json()
  print(PlaceEthLendOrder)
  # PlaceEthLendOrder = (PlaceEthLendOrder.get('data'))
  # PlaceEthLendOrder = json.dumps(PlaceEthLendOrder)
  # PlaceEthLendOrder = json.loads(PlaceEthLendOrder)
  # PlaceEthLendOrder = PlaceEthLendOrder["orderId"]
  # PlaceEthLendOrder = str(PlaceEthLendOrder)
  return PlaceEthLendOrder
