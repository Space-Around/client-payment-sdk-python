from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '90',
    'merchant_id': '15',
    'order': '067dbec6-719c-11ec-9e37-0242ac130040',
    'pan': '4111111111111111'
}

params['signature'] = sign('/withdrawal_request', 'GET', params, api_secret)

client = ClientPaymentSDK(None, api_secret)
result = client.withdrawal(params)

print(result)
