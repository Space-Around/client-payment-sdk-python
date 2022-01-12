from jwcrypto import jws, jwk
from jwcrypto.common import json_encode, json_decode
from .utils import dict_to_str


def sign(endpoint, method, payload, secret):
    header = {'alg': 'HS256'}

    key = jwk.JWK.from_password(secret)

    sorted_param = dict(sorted(payload.items(), key=lambda x: x[0]))

    for key in sorted_param:
        sorted_param[key] = str(sorted_param[key])

    payload_dict = {'PATH': endpoint, method.upper(): sorted_param}

    payload_str = dict_to_str(payload_dict)

    jwstoken = jws.JWS(payload_str.encode('utf-8'))
    jwstoken.add_signature(key, None, json_encode(header), json_encode({"kid": key.thumbprint()}))
    jws_data = json_decode(jwstoken.serialize())

    return jws_data['signature']