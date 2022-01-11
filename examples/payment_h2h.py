from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '100',
    'merchant_id': '13',
    'order': 'fb11ff6c-7145-11ec-9e37-0242ac130022',
    'product_id': '15',
    'pan': '4111111111111111',
    'expire_month': '01',
    'expire_year': '25',
    'cvc': '1'
}

params['signature'] = sign('/init', 'POST', params, api_secret)

client = ClientPaymentSDK()
result = client.init(params)

print(result)
