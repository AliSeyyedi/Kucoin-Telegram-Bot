import headers as H
import requests
import account
import json

import time
import pybase64 as base64
import hmac
import account
import hashlib

endpoint = '/api/v1/margin/lend'
method = 'POST'

def PlaceEthLendOrder():
  params = {
  'currency'      : 'ETH' ,
  'size'          : '0.05' ,
  'dailyIntRate'  : '0.002',
  'term'          : '7'
  }
  data = json.dumps(params)
  headers = H.getHeaders(method, endpoint+data)
  PlaceEthLendOrder = requests.post(account.url + '/api/v1/margin/lend', headers=headers, data=data).json()
  PlaceEthLendOrder = (PlaceEthLendOrder.get('data'))
  PlaceEthLendOrder = json.dumps(PlaceEthLendOrder)
  PlaceEthLendOrder = json.loads(PlaceEthLendOrder)
  PlaceEthLendOrder = PlaceEthLendOrder["orderId"]
  PlaceEthLendOrder = str(PlaceEthLendOrder)
  return PlaceEthLendOrder
