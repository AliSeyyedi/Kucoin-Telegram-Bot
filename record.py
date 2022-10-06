import headers as H

endpoint = '/api/v1/margin/lend/assets?currency=ETH'
method = 'GET'

def getRecord():
    headers = H.getHeaders(method, endpoint)
    getRecord = requests.get(url + endpoint, headers=headers).json()
    getRecord = (getRecord.get('data'))
    getRecord = getRecord[0]
    getRecord = json.dumps(getRecord)
    getRecord = json.loads(getRecord)
    currency            = str(getRecord['currency'])
    outstanding         = str(getRecord['outstanding'])
    filledSize          = str(getRecord['filledSize'])
    accruedInterest     = str(getRecord['accruedInterest'])
    realizedProfit      = str(getRecord['realizedProfit'])
    totallaccruedProfit = str("%.9f" %(float(getRecord['accruedInterest'])+float(getRecord['realizedProfit'])))
    totallaccruedProfitPercent = str((float(totallaccruedProfit)*100)/0.2)
    isAutoLend          = str(getRecord['isAutoLend'])
    output = (currency+ '\nOut Standing: '+ outstanding + '\nFilled Size: '+ filledSize+ '\nAccrued Interest: '+ accruedInterest+ '\nRealized Profit: '+ realizedProfit + '\nTotall Accrued Profit: '+ totallaccruedProfit + '\nTotall Accrued Profit %: '+ totallaccruedProfitPercent+ '\nIs Auto Lend: '+ isAutoLend)
    return output
