import jws
from jwcrypto import jwk
from jwcrypto import jws as jwsc
from jwcrypto.common import json_encode, json_decode
import json

header = {'alg': 'HS256'}
payload = {
    "PATH": "/init",
    "GET": {
        "amount": "10",
        "merchant_id": "13",
        "order": "order-00001",
        "product_id": "15"
    }
}

# header = {"alg":"HS256"}
# payload = '{"PATH":"/init","GET":{"amount":"10","merchant_id":"13","order":"order-00001","product_id":"15"}}'

# payload['GET'] = dict(sorted(payload['GET'].items(), key=lambda x: x[0]))

# print(payload)

# signature = jws.sign(header, payload, 'aa21444f3f71').decode('utf-8')
# print(signature)


key = jwk.JWK.from_password('aa21444f3f71')
payload_etalon = '{"PATH":"/init","GET":{"amount":"10","merchant_id":"13","order":"order-00001","product_id":"15"}}'
payload = str(payload).replace('\'', '"').replace(' ', '')

print(payload)
# print(payload_etalon)
# print(f'\'{payload}\'' == payload_etalon)
jwst = jwsc.JWS(payload.encode('utf-8'))

jwst.add_signature(key, None, json_encode({"alg": "HS256"}), json_encode({"kid": key.thumbprint()}))
sig = json_decode(jwst.serialize())
print(sig['signature'] == 'SK0TkoeNslHBhKp4EI3_oCVfCJ1gBENQbgNf7YGfQWo')
# SK0TkoeNslHBhKp4EI3_oCVfCJ1gBENQbgNf7YGfQWo