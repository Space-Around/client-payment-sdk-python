# Client payment SDK Python
[![Build Status](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![License](https://img.shields.io/pypi/l/yookassa-payout.svg)](https://github.com/yoomoney/yookassa-payout-sdk-python)

[Russian](https://github.com/Space-Around/client-payment-sdk-python/blob/main/README.ru.md) | English

Client payment SDK provides convenient access to the [API](https://sbank.gogo.vc/docs/) from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses.
## Installation

### via `pip`
1. Install pip.
2. In the console, run the following command:
```bash
pip install client-payment-sdk
```

### via `easy_install`
1. Install easy_install.
2. In the console, run the following command:
```bash
easy_install --upgrade client-payment-sdk
```

### via `setuptools`
1. In the console, run the following command:
```bash
wget https://github.com/Space-Around/client-payment-sdk-python/archive/refs/heads/main.zip
tar zxf client-payment-sdk-python-main.tar.gz
cd client-payment-sdk-python-main
python setup.py install
```

### Requirements
* Python 3.10+

## Usage
```Python
from client_payment_sdk import ClientPaymentSDK, sign

client = ClientPaymentSDK()
```


## Documentation
See [API docs](https://sbank.gogo.vc/docs/).

All examples [here](https://github.com/Space-Around/client-payment-sdk-python/tree/main/examples).

### `.init()`
**Description:** 
Payment initiation.

**Arguments**

Name | Description                                     | Example             | Required
--------------------|-------------------------------------------------|---------------------|---
**amount**          | payment amount                                  | 10                  | +
**order**           | order number in your system                     | order-00001         | +
**merchant_id**     | your id in the system                           | 1                   | +
**product_id**      | product id in the system                        | 1                   | +
**to_card**         | payment card number                             | 4111111111111111    | -
**signature**       | signature                                   | quahJ5th...         | +
**description**     | order description                               | Ordering a product  | -
**language**        | language: ru or en                              | en                  | -
**finish_url**      | url to which to redirect the user after payment | https://exemple.com | - 
2**notification_url**| url to which to send a notification of payment  | https://exemple.com | - 
**lifetime**        | link time in seconds (default 3600)             | 3600                | -

### host2host
**Arguments**

Name | Description              | Example          | Required
--------------------|--------------------------|------------------|---
**pan**          | card number              | 4111111111111111 | +
**expire_month**           | card expiry date (month) | 01               | +
**expire_year**     | card expiry date (year)  | 25               | +
**cvc**     | cvc-code                 | 1                | +

### 3DS 2.0
**Arguments**

Name | Description                           | Example                                                                       | Required
--------------------|---------------------------------------|-------------------------------------------------------------------------------|---
**device_channel**          | authentication channel                | BRW                                                                           | +
**device_browser_ip**           | browser IP address                    | 0.0.0.0                                                                       | +
**device_browser_accept_header**     | accepted content                      | text/html                                                                     | +
**device_browser_java_enabled**     | indication of work with Java          | false                                                                         | +
**device_browser_language**     | browser language                      | RU                                                                            | +
**device_browser_color_depth**     | browser colour depth                  | 32                                                                            | +
**device_browser_screen_height**     | browser screen height                 | 800                                                                           | +
**device_browser_screen_width**     | browser screen width                  | 480                                                                           | +
**device_browser_tz**     | browser time zone in minutes from UTC | 60, 120, -180                                                                 | +
**device_browser_user_agent**     | browser user agent                    | Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 | +
**challenge_window_size**     | size of challenge window              | 02                                                                            | +

**Return:**
`InitPaymentResponse`

Field name | Default                
--------------------|------------------------
**status**          | None
**payment_redirect_url**           | None     
**url**           | None
**form_data**           | None


**Example:**
```Python
result = client.init(params)
```

</br>

### `.status()`
**Description:** 
Get payment status.

**Arguments**

Name | Description              | Example | Required
--------------------|--------------------------|------|---
**merchant_id**          | your id in the system    | 1    | +
**product_id**           | product id in the system | 1    | +
**order**     | your id in the system    | order-00001     | +
**signature**      | signature                | quahJ5th...     | +

**Return:**
`StatusPaymentResponse`

Field name | Default                
--------------------|------------------------
**status**          | None
**payment_status**           | None     
**refund_status**           | None
**last_payment_error_code**           | None
**last_payment_error**           | None

**Example:**
```Python
result = client.status(params)
```

</br>

### `.balace()`
**Description:** 
Get balance.

**Arguments**

Name | Description              | Example    | Required
--------------------|--------------------------|------------|---
**merchant_id**          | your id in the system    | 1          | +
**currency**           | account currency (RUB by default) | RUB        | -
**signature**      | signature                | quahJ5th... | +

**Return:**
`BalanceResponse`

Field name | Default                
--------------------|------------------------
**status**          | None
**balance**           | None

**Example:**
```Python
result = client.balance(params)
```

</br>

### `.withdrawal()`
**Description:** 
Withdrawal request.

**Arguments**

Name | Description              | Example    | Required
--------------------|--------------------------|------------|---
**merchant_id**          | your id in the system    | 1          | +
**order**           | order number in your system                     | order-00001        | +
**currency**           | account currency (RUB by default) | RUB        | -
**pan**          | card number              | 4242424242424242 | +
**amount**          | payment amount                                  | 10                 | +
**signature**      | signature                | quahJ5th... | +
**notification_url**| url to which to send a notification of payment  | https://exemple.com | -

**Return:**
`WithdrawalResponse`

Field name | Default                
--------------------|------------------------
**status**          | None
**withdrawal_request**           | None

**Example:**
```Python
result = client.withdrawal(params)
```

</br>

### `.withdrawal_status()`
**Description:** 
Withdrawal status.

**Arguments**

Name | Description              | Example    | Required
--------------------|--------------------------|------------|---
**merchant_id**          | your id in the system    | 1          | +
**id**           | withdrawal request id                     | 1523       | +
**signature**      | signature                | quahJ5th... | +

or

Name | Description              | Example    | Required
--------------------|--------------------------|------------|---
**merchant_id**          | your id in the system    | 1          | +
**order**           | withdrawal number in your system                     | order-00001       | +
**signature**      | signature                | quahJ5th... | +

**Return:**
`StatusWithdrawalResponse`

Field name | Default                
--------------------|------------------------
**status**          | None
**withdrawal_request**           | None

**Example:**
```Python
result = client.withdrawal_status(params)
```

</br>


### `Webhook.verify_signature()`
**Description:** 
Signature verification.

**Arguments**

Name | Description           | Example | Required
--------------------|-----------------------|--------|---
**endpoint**          | path from url         | `/webhooks` | +
**method**           | HTTP method           | POST   | +
**params**      | payload from response | `WebhookData(data_from_response)`       | +
**secret**      | secret                | 1234fwes | +

**Return:**
`True` or raise error `SignatureVerificationError`.

**Example:**
```Python
data = WebhookData(data_from_response)
Webhook.verify_signature('/webhooks', 'POST', data, api_secret)
```

</br>

### `WebhookData()`
**Description:** 
Notification class, is needed for the `Webhook.verify_signature()` method and to more easily get data from the request.

**Arguments:**
`dict`

**Return:**
`WebhookData`

Name | Description                                  | Example
--------------------|----------------------------------------------|--------
**webhook_type**          | webhook type                                 | invoice
**amount**           | payment amount                               | amount   
**product_id**      | product id in the system                     | 1
**merchant_id**      | your id in the system                        | 1
**order**      | order number in your system                  | order-00001
**currency**      | payment currency                             | RUB
**status**      | payment status complete/failed               | complete
**webhook_id**      | webhook id, same on repetition               | 1
**payment_error_code**      | error code (if status='failed')              | common
**payment_error**      | error text (if status='failed')              | insufficient funds
**signature**      | signature                                    | quahJ5th...
**withdrawal_request_id**      | transaction id in the system                                       | 1
**requested_amount**      | amount requested for withdrawal                                       | 100
**invoice_id**      | transaction id in the system                 | 1
**customer_fee**      | commission to be deducted from the purchaser | 2
**masked_pan**      | masked beneficiary card number                                       | RUB

**Example:**
```Python
# using Flask
@app.route("/webhooks", methods=["POST"])
def webhooks():
    payload = request.form.to_dict()
    try:
        data = WebhookData(payload)

        print(Webhook.verify_signature('/webhooks', 'POST', data, api_secret))
        # usage data
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    return "", 200
```

</br>


### `.sign()`
**Description:** 
Create jws signature

**Arguments**

Name | Description    | Example  | Required
--------------------|----------------|----------|---
**endpoint**          | path from url  | `/init`  | +
**method**           | HTTP method         | POST     | +
**params**      | payload (dict) | {}       | +
**secret**      | secret         | 1234fwes | +

**Return:**
`str`

**Example:**
```Python
api_secret = 'aa21444f3f71'
payload = {
    'amount': 10,
    'merchant_id': 15,
    'order': '241eeda4-7491-11ec-9c7f-0242ac130021',
    'product_id': 15,
    'notification_url': 'http://25ab-91-241-13-31.ngrok.io/webhooks'
}

payload['signature'] = sign('/init', 'POST', payload, api_secret)
```

## License
This project is licensed under the [MIT license](https://github.com/eth-brownie/brownie/blob/master/LICENSE).
