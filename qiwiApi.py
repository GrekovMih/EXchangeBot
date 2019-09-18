from telegramApi import bot

import requests
import json
import time


# Перевод на QIWI Кошелек
def send_p2p(my_login, api_access_token, to_qw, comment, sum_p2p, message):
    s = requests.Session()
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['User-Agent'] = 'Android v3.2.0 MKT'
    s.headers['Accept'] = 'application/json'
    postjson = json.loads(
        '{"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"},"comment":"' + comment + '","fields":{"account":""}}')
    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = sum_p2p
    postjson['sum']['currency'] = '643'
    postjson['fields']['account'] = to_qw
    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments', json=postjson)
    #print(res)

    bot.send_message(message.chat.id, res.text)

    try:
        bot.send_message(message.chat.id, res.text.transaction.state.code)  #не кошер, еще подумаю где лучше делать
        if (res.text.transaction.state.code=='Accepted'):
            status='ok'
        else:
            status='false'

    except:
        bot.send_message(message.chat.id, res.text.message)
        status = 'false'

    print(json.loads(res.text))

    return status
