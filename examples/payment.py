from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '100',
    'merchant_id': '13',
    'order': 'fb11ff6c-7145-11ec-9e37-0242ac130032',
    'product_id': '15'
}

params['signature'] = sign('/init', params, api_secret)

client = ClientPaymentSDK(None, api_secret)
html = client.init(params)

print(html)