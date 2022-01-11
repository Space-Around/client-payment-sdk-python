import jws

header = {"alg":"HS256"}
payload = '{"PATH":"/init","GET":{"amount":"10","merchant_id":"13","order":"order-00001","product_id":"15"}}'

signature = jws.sign(header, payload, 'aa21444f3f71').decode('utf-8')
print(signature)