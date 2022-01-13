from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': 50,
    'merchant_id': 15,
    'order': '241eeda4-7491-11ec-9c7f-0242ac130017',
    'product_id': 15,
    'pan': '4111111111111111',
    'expire_month': '01',
    'expire_year': '25',
    'cvc': '1',
    'notification_url': 'https://72c7-193-243-174-37.ngrok.io/webhooks'
}

params['signature'] = sign('/init', 'POST', params, api_secret)
client = ClientPaymentSDK()
result = client.init(params)

print(f'url: {result.url}, from_data: {result.form_data}')