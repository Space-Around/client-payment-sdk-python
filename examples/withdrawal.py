from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '100',
    'merchant_id': '13',
    'order': '067dbec6-719c-11ec-9e37-0242ac130017',
    'pan': '4242424242424242'
}

params['signature'] = sign('/withdrawal_request', 'GET', params, api_secret)

client = ClientPaymentSDK(None, api_secret)
result = client.withdrawal(params)

print(result)
