from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'

params = {
    'merchant_id': '13',
    'order': 'fb11ff6c-7145-11ec-9e37-0242ac130032',
    'product_id': '15'
}

params['signature'] = sign('/status', 'GET', params, api_secret)

client = ClientPaymentSDK()
result = client.status(params)

print(result)
