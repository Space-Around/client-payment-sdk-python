from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': 10,
    'merchant_id': 15,
    'order': '241eeda4-7491-11ec-9c7f-0242ac130017',
    'product_id': 15
}

params['signature'] = sign('/init', 'POST', params, api_secret)
client = ClientPaymentSDK()
result = client.init(params)

print(f'url: {result.url}')
