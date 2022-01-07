from client_payment_sdk import ClientPaymentSDK


api_secret = 'aa21444f3f71'
params = {
    'amount': 1,
    'order': 'order-00001',
    'merchant_id': 13,
    'product_id': 15,
    'signature': ''
}

client = ClientPaymentSDK()
client.init()