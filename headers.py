import time
import pybase64 as base64
import hmac
import account
import hashlib

def getHeaders(method, endpoint, data):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + method + endpoint + data
    signature = base64.b64encode(hmac.new(account.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    headers = {
    'KC-API-KEY': account.api_key,
    'KC-API-SIGN': signature,
    'KC-API-TIMESTAMP': str(now),
    'KC-API-PASSPHRASE': account.api_passphrase,
    'KC-API-KEY-VERSION': "1",
    'Content-Type': 'application/json'
    }
    return headers
