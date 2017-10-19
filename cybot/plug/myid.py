# -*- coding: utf-8 -*-

import config
from metodos import *
from mensagens import myid

def my_id(msg):
    chat_id = msg['chat']['id']
    try: user = '@' + msg['from']['username']
    except:user = " "

    if msg['text'] == '/id':
        if msg['chat']['type'] == 'private':
            sendMessage(chat_id, myid['private'].decode('utf8').format(msg['from']['first_name'].encode('utf-8'),msg['from']['id'],user))


        if msg['chat']['type'] == 'supergroup' or msg['chat']['type'] == 'group':
            sendMessage(chat_id, myid['private'].decode('utf8').format(msg['from']['first_name'],msg['from']['id'],user))

