from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'merchant_id': 15,
    'order': '067dbec6-719c-11ec-9e37-0242ac130196'
}

params['signature'] = sign('/withdrawal_request', 'GET', params, api_secret)

client = ClientPaymentSDK()
result = client.withdrawal_status(params)

print(f'status: {result.status}, withdrawal_request: {result.withdrawal_request}')
