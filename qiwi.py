from telegram_api import bot

import requests
import json
import time

print('res')

s = requests.Session()
s.headers = {'content-type': 'application/json'}
s.headers['authorization'] = 'Bearer ' + api_access_token
s.headers['User-Agent'] = 'Android v3.2.0 MKT'
s.headers['Accept'] = 'application/json'
print('res4')

postjson = json.loads(
    '{"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"},"comment":"' + 'crypto' + '","fields":{"account":""}}')
postjson['id'] = str(int(time.time() * 1000))
postjson['sum']['amount'] = 1
postjson['sum']['currency'] = '643'
postjson['fields']['account'] = '+79055377771'
print('res2')

res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments', json=postjson)
print('res3')

bot.send_message(message.chat.id, ' wtf ')

try:
    bot.send_message(message.chat.id, res.text.transaction.state.code)  # не кошер, еще подумаю где лучше делать
    if (res.text.transaction.state.code == 'Accepted'):
        status = 'ok'
    else:
        status = 'false'

except:
    # bot.send_message(message.chat.id, res.text.message)
    status = 'false'
    bot.send_message(message.chat.id, "Qiwi failed")

print("finish him")
