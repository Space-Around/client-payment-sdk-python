from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': 50,
    'merchant_id': 15,
    'order': '067dbec6-719c-11ec-9e37-0242ac130061',
    'product_id': 15,
}

params['signature'] = sign('/init', 'POST', params, api_secret)
client = ClientPaymentSDK()
result = client.init(params)

print(result.url)
