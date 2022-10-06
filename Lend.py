def PlaceEthLendOrder():
  params = {
    'currency'      : 'ETH' ,
    'size'          : 'All' ,
    'dailyIntRate'  : '0.002',
    'term'          : '7'
  }
  data_json = json.dumps(params)
  now = int(time.time() * 1000)
  str_to_sign = str(now) + 'POST' + '/api/v1/margin/lend' + data_json
  signature = base64.b64encode(hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
  passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
  headers = {
    'KC-API-KEY': api_key,
    'KC-API-SIGN': signature,
    'KC-API-TIMESTAMP': str(now),
    'KC-API-PASSPHRASE': api_passphrase,
    'KC-API-KEY-VERSION': '1',
    'Content-Type': 'application/json'
  }
  PlaceEthLendOrder = requests.post(url + '/api/v1/margin/lend',data=data_json, headers=headers).json()
  PlaceEthLendOrder = (PlaceEthLendOrder.get('data'))
  PlaceEthLendOrder = json.dumps(PlaceEthLendOrder)
  PlaceEthLendOrder = json.loads(PlaceEthLendOrder)
  PlaceEthLendOrder = PlaceEthLendOrder["orderId"]
  PlaceEthLendOrder = str(PlaceEthLendOrder)
  print(PlaceEthLendOrder)
  return PlaceEthLendOrder
