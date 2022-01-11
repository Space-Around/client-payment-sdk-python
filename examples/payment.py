from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '90',
    'merchant_id': '15',
    'order': '067dbec6-719c-11ec-9e37-0242ac130040',
    'product_id': '15'
}

params['signature'] = sign('/init', 'POST', params, api_secret)
client = ClientPaymentSDK()
response = client.init(params)

print(response)
