from jwcrypto import jws, jwk
from jwcrypto.common import json_encode, json_decode
from .utils import dict_to_str


def sign(endpoint, method, payload, secret):
    header = {'alg': 'HS256'}

    key = jwk.JWK.from_password(secret)

    sorted_param = dict(sorted(payload.items(), key=lambda x: x[0]))

    if method == 'POST':
        payload_dict = {'PATH': endpoint, 'POST': sorted_param}
    else:
        # TODO: add raise if not method get
        payload_dict = {'PATH': endpoint, 'GET': sorted_param}

    payload_str = dict_to_str(payload_dict)

    jwstoken = jws.JWS(payload_str.encode('utf-8'))
    jwstoken.add_signature(key, None, json_encode(header), json_encode({"kid": key.thumbprint()}))
    jws_data = json_decode(jwstoken.serialize())

    return jws_data['signature']