from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'

params = {'amount': '100',
          'merchant_id': '13',
          'order': 'fb11ff6c-7145-11ec-9e37-0242ac130021',
          'product_id': '15',
          'device_channel': 'BRW',
          'device_browser_ip': '0.0.0.0',
          'device_browser_accept_header': 'text/html',
          'device_browser_java_enabled': 'false',
          'device_browser_language': 'RU',
          'device_browser_color_depth': '32',
          'device_browser_screen_height': '800',
          'device_browser_screen_width': '480',
          'device_browser_tz': '60, 120, -180',
          'device_browser_user_agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
          'challenge_window_size': '02'
          }

params['signature'] = sign('/init', 'GET', params, api_secret)

client = ClientPaymentSDK()
result = client.init(params)

print(result)
