

def getHeaders(method, endpoint):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + method + endpoint
    signature = base64.b64encode(hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
    headers = {
    'KC-API-KEY': main.api_key,
    'KC-API-SIGN': signature,
    'KC-API-TIMESTAMP': str(now),
    'KC-API-PASSPHRASE': passphrase,
    'KC-API-KEY-VERSION': "1",
    'Content-Type': 'application/json'
    }
    return headers