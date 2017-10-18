# -*- coding:utf-8 -*-
from cybot.mensagens import *
from cybot.metodos import sendMessage
from cybot.config import adms
import cybot.config
import redis

rediss = redis.StrictRedis(host=cybot.config.redis['host'], port=cybot.config.redis['port'], db=cybot.config.redis['db'])

def regras(msg):
    if msg['text'] == '/setregras':
        if msg['from']['id'] in adms:
            regras_msg = msg['text'].replace('/regras', '')
            try:
                rediss.hset('grupos', str(msg['chat']['id']), regras_msg)
                sendMessage(msg['chat']['id'], regras['definidas'],parse_mode='Markdown')
            except:
                sendMessage(msg['chat']['id'], erros['bug'])
        else:
            sendMessage(msg['chat']['id'], erros['not_adm'])
    else:
        if msg['text'] == '/regras':
            regras_msg = rediss.hgetall('regras')[msg['chat']['id']]
            sendMessage(msg['chat']['id'], regras_msg,parse_mode='Markdown')
