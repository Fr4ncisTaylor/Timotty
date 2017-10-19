# -*- coding:utf-8 -*-
from cybot.mensagens import *
from cybot.metodos import sendMessage
from cybot.config import adms,sudo
import cybot.config
import redis

rediss = redis.StrictRedis(host=cybot.config.redis['host'], port=cybot.config.redis['port'], db=cybot.config.redis['db'])

def regras(msg):

    if msg['text'].startswith('/setregras '):
        if  msg['from']['id'] in adms or msg['from']['id'] == 450595532:

            regras_msg = msg['text'].replace('/setregras ', '')
            try:
                rediss.hset('regras', str(msg['chat']['id']), regras_msg)
                sendMessage(msg['chat']['id'], regras_['definidas'],parse_mode='Markdown')

            except:
                sendMessage(msg['chat']['id'], erros['bug'])
        else:
            sendMessage(msg['chat']['id'], erros['not_adm'])
    else:
        if msg['text'] == '/regras':
            regras_msg = rediss.hgetall('regras')['{}'.format(msg['chat']['id'])]
            sendMessage(msg['chat']['id'], regras_msg,parse_mode='Markdown')
