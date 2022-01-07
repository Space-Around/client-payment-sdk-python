from client_payment_sdk import ClientPaymentSDK


api_secret = 'aa21444f3f71'
params = {
    'amount': '10',
    'order': 'order-00001',
    'merchant_id': '13',
    'product_id': '15'
}

client = ClientPaymentSDK(None, api_secret)
print(client.init(params))