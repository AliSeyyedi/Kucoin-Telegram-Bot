import requests
import account

endpoint = '/api/v1/margin/market?currency=ETH&term=7'

def getEthRate():
  EthRate = requests.get(account.url + endpoint).json()
  EthRate = (EthRate.get('data'))
  EthRate = EthRate[0]
  EthRate = json.dumps(EthRate)
  EthRate = json.loads(EthRate)
  EhtRate = EthRate["dailyIntRate"]
  EhtRate = str(EhtRate)
  return EhtRate
