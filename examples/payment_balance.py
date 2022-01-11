from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'

params = {'merchant_id': '13'}

params['signature'] = sign('/balance', 'GET', params, api_secret)

client = ClientPaymentSDK()
result = client.balance(params)

print(result)
