# Client payment SDK Python
[![Build Status](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![License](https://img.shields.io/pypi/l/yookassa-payout.svg)](https://github.com/yoomoney/yookassa-payout-sdk-python)

Русский | [Английский]((https://github.com/Space-Around/client-payment-sdk-python/blob/main/README.md))

Client payment SDK обеспечивает удобный доступ к [API](https://sbank.gogo.vc/docs/) из приложений, написанных на Python. Включает в себя предопределенный набор классов для ресурсов API, которые инициализируются динамически из ответов API.
## Установка

### через `pip`
1. Установить pip.
2. В консоле выполнить следующие комманды:
```bash
pip install client-payment-sdk
```

### через `easy_install`
1. Установить easy_install.
2. В консоле выполнить следующие комманды:
```bash
easy_install --upgrade client-payment-sdk
```

### через `setuptools`
1. В консоле выполнить следующие комманды:
```bash
wget https://github.com/Space-Around/client-payment-sdk-python/archive/refs/heads/main.zip
tar zxf client-payment-sdk-python-main.tar.gz
cd client-payment-sdk-python-main
python setup.py install
```

### Требования
* Python 3.10+

## Использование
```Python
from client_payment_sdk import ClientPaymentSDK, sign

client = ClientPaymentSDK()
```


## Документация

Посмотрите [документацию для API](https://sbank.gogo.vc/docs/).

Все примеры [здесь](https://github.com/Space-Around/client-payment-sdk-python/tree/main/examples).

### `.init()`
**Описание:** 
Инициация платежа.

**Аргументы**

Название | Описание                                                                 | Пример              | Обязательность
--------------------|--------------------------------------------------------------------------|---------------------|---
**amount**          | сумма платежа                                                            | 10                  | +
**order**           | номер заказа в вашей системе                                             | order-00001         | +
**merchant_id**     | ваш id в системе                                                         | 1                   | +
**product_id**      | id продукта в системе                                                    | 1                   | +
**to_card**         | номер карты для выплаты                                                  | 4111111111111111    | -
**signature**       | подпись                                                                  | quahJ5th...         | +
**description**     | описание заказа                                                          | Заказ товара        | -
**language**        | язык: ru или en                                                          | ru                  | -
**finish_url**      | url на который перенаправить пользователя после оплаты 	                 | https://exemple.com | - 
**notification_url**| url на который отправить нотификацию об оплате                           | https://exemple.com | - 
**lifetime**        | время действия ссылки в секундах (по умолчанию - 3600) 	                 | 3600                | -

### host2host

**Аргументы**

Название | Описание                 | Пример           | Обязательность
--------------------|--------------------------|------------------|---
**pan**          | номер карты              | 4111111111111111 | +
**expire_month**           | срок действия карты (месяц) | 01               | +
**expire_year**     | срок действия карты (год)  | 25               | +
**cvc**     | cvc-код                 | 1                | +

### 3DS 2.0

**Аргументы**

Название | Описание                               | Пример                                                                        | Обязательность
--------------------|----------------------------------------|-------------------------------------------------------------------------------|---
**device_channel**          | канал аутентификации                   | BRW                                                                           | +
**device_browser_ip**           | ip адрес браузера                      | 0.0.0.0                                                                       | +
**device_browser_accept_header**     | принимаемый контент                    | text/html                                                                     | +
**device_browser_java_enabled**     | признак работы с Java                  | false                                                                         | +
**device_browser_language**     | язык браузера                          | RU                                                                            | +
**device_browser_color_depth**     | глубина цвета браузера                 | 32                                                                            | +
**device_browser_screen_height**     | высота экрана браузера                 | 800                                                                           | +
**device_browser_screen_width**     | ширина экрана браузера                 | 480                                                                           | +
**device_browser_tz**     | часовой пояс браузера в минутах от UTC | 60, 120, -180                                                                 | +
**device_browser_user_agent**     | пользовательский агент браузера        | Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 | +
**challenge_window_size**     | размер окна для challenge              | 02                                                                            | +

**Возвращает:**
`InitPaymentResponse`

Название поля | По умолчанию                
--------------------|------------------------
**status**          | None
**payment_redirect_url**           | None     
**url**           | None
**form_data**           | None


**Пример:**
```Python
result = client.init(params)
```

</br>

### `.status()`
**Описание:** 
Получить статус платежа.

**Аргументы**

Название | Описание                     | Пример      | Обязательность
--------------------|------------------------------|-------------|---
**merchant_id**          | ваш id в системе             | 1           | +
**product_id**           | id продукта в системе        | 1           | +
**order**     | номер заказа в вашей системе | order-00001 | +
**signature**      | подпись                      | quahJ5th... | +

**Возвращает:**
`StatusPaymentResponse`

Название поля | По умолчанию                
--------------------|------------------------
**status**          | None
**payment_status**           | None     
**refund_status**           | None
**last_payment_error_code**           | None
**last_payment_error**           | None

**Пример:**
```Python
result = client.status(params)
```

</br>

### `.balace()`
**Описание:** 
Получение баланса.

**Аргументы**

Название | Описание                          | Пример      | Обязательность
--------------------|-----------------------------------|-------------|---
**merchant_id**          | ваш id в системе             | 1           | +
**currency**           | валюта счета (RUB по умолчанию) | RUB         | -
**signature**      | подпись                         | quahJ5th... | +

**Возвращает:**
`BalanceResponse`

Название поля | По умолчанию                
--------------------|------------------------
**status**          | None
**balance**           | None

**Пример:**
```Python
result = client.balance(params)
```

</br>

### `.withdrawal()`
**Описание:** 
Запрос на вывод средств.

**Аргументы**

Название | Описание                                       | Пример              | Обязательность
--------------------|------------------------------------------------|---------------------|---
**merchant_id**          | ваш id в системе                          | 1                   | +
**order**           | номер вывода средств в вашей системе                    | order-00001         | +
**currency**           | валюта счета (RUB по умолчанию)              | RUB                 | -
**pan**          | номер карты для вывода средств                                    | 4242424242424242    | +
**amount**          | сумма платежа                                 | 10                  | +
**signature**      | подпись                                      | quahJ5th...         | +
**notification_url**| url на который отправить нотификацию об платеже | https://exemple.com | -

**Возвращает:**
`WithdrawalResponse`

Название поля | По умолчанию                
--------------------|------------------------
**status**          | None
**withdrawal_request**           | None

**Пример:**
```Python
result = client.withdrawal(params)
```

</br>

### `.withdrawal_status()`
**Описание:** 
Статус запроса на вывод средств.

**Аргументы**

Название | Описание              | Пример      | Обязательность
--------------------|-----------------------|-------------|---
**merchant_id**          | ваш id в системе | 1           | +
**id**           | id-запроса на вывод средств | 1523        | +
**signature**      | подпись             | quahJ5th... | +

или

Название | Описание                         | Пример      | Обязательность
--------------------|----------------------------------|-------------|---
**merchant_id**          | ваш id в системе            | 1           | +
**order**           | номер вывода средств в вашей системе | order-00001 | +
**signature**      | подпись                        | quahJ5th... | +

**Возвращает:**
`StatusWithdrawalResponse`

Название поля | По умолчанию                
--------------------|------------------------
**status**          | None
**withdrawal_request**           | None

**Пример:**
```Python
result = client.withdrawal_status(params)
```

</br>


### `Webhook.verify_signature()`
**Описание:** 
Верификация подписи.

**Аргументы**

Название | Описание          | Пример                            | Обязательность
--------------------|-------------------|-----------------------------------|---
**endpoint**          | путь из url       | `/webhooks`                       | +
**method**           | HTTP метод        | POST                              | +
**params**      | данные из запроса | `WebhookData(data_from_response)` | +
**secret**      | секрет            | 1234fwes                          | +

**Возвращает:**
`True` или вызывает ошибку `SignatureVerificationError`.

**Пример:**
```Python
data = WebhookData(data_from_response)
Webhook.verify_signature('/webhooks', 'POST', data, api_secret)
```

</br>

### `WebhookData()`
**Описание:** 
Класс нотификации, необходим для метода `Webhook.verify_signature()` и более удобного получения данных из запроса.

**Аргументы:** `dict`

**Возвращает:**
`WebhookData`

Название | Описание                                     | Пример
--------------------|----------------------------------------------|--------
**webhook_type**          | тип вебхука                                 | invoice
**amount**           | сумма платежа                               | amount   
**product_id**      | id продукта в системе                     | 1
**merchant_id**      | ваш id в системе                        | 1
**order**      | номер заказа в вашей системе                  | order-00001
**currency**      | валюта платежа                             | RUB
**status**      | статус оплаты complete/failed               | complete
**webhook_id**      | id вебхука, одинаковый при повторах               | 1
**payment_error_code**      | код ошибки(если status='failed')              | common
**payment_error**      | текст ошибки(если status='failed')              | insufficient funds
**signature**      | подпись                                    | quahJ5th...
**withdrawal_request_id**      | id траназакции в системе                 | 1
**requested_amount**      | сумма которую запросили на вывод              | 100
**invoice_id**      | id траназакции в системе                 | 1
**customer_fee**      | комиссия, которая удерживается с покупателя | 2
**masked_pan**      | маскированный номер карты получателя               | RUB

**Пример:**
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
**Описание:** 
Создание jws подписи

**Аргументы**

Название | Описание          | Пример   | Обязательность
--------------------|-------------------|----------|---
**endpoint**          | путь из url       | `/init`  | +
**method**           | HTTP метод        | POST     | +
**params**      | данные (тип dict) | {}       | +
**secret**      | секрет            | 1234fwes | +

**Возвращает:**
`str`

**Пример:**
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

## Лицензия
Этот проект под [лицензией MIT](https://github.com/eth-brownie/brownie/blob/master/LICENSE).
