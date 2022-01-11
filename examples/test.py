from client_payment_sdk import ClientPaymentSDK
from client_payment_sdk import sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '100',
    'merchant_id': '13',
    'order': 'fb11ff6c-7145-11ec-9e37-0242ac130019',
    'product_id': '15'
}

params['signature'] = sign('/init', params, api_secret)

client = ClientPaymentSDK(None, api_secret)
print(params)
# html = client.init(params)

#https://example.com/?amount=100.0000&invoice_id=696&product_id=15&merchant_id=13&order=fb11ff6c-7145-11ec-9e37-0242ac130019&currency=RUB&signature=vj6yZajuKJXlYh9AUm8xvKO12KYsLt_UBfau1Q9JvME