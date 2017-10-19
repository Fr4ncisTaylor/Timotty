# -*- coding: utf-8 -*-

import redis

from cybot import mensagens
from cybot.metodos import *

redis = redis.StrictRedis(host=config.redis['host'], port=config.redis['port'], db=config.redis['db'])
m = mensagens

def promover(msg):
    if 'text' in msg:
        texto = msg[u'text'].encode('utf-8')
        chat_id = msg['chat']['id']
        nome = msg['from'][u'first_name']
        from_id = msg['from']['id']

        if msg['chat']['type'] == 'group' or msg['chat']['type'] == 'supergroup':
            redis.hset('grupos', str(chat_id), 'OK')
            redis.hset('usuarios', str(from_id), 'OK')

        if msg['chat']['type'] == 'private':
            redis.hset('usuarios', str(from_id), 'OK')

        if texto.startswith('/promover'):
            if from_id == config.sudo:
                mensagem =texto.replace('/promover', '')
                mensagem = u'{}'.format(mensagem.decode('utf8'))
                r=redis.hgetall('grupos')

                if r:
                    Y = 0
                    N = 0

                    for (i,idd) in enumerate(r):

                        try:
                            sendMessage(idd,mensagem,parse_mode='Markdown')
                            Y += 1
                        except:
                            N += 1

                    sendMessage(chat_id,m.promover.format(Y,N,mensagem))

                else:
                    sendMessage(chat_id,m.redis['erro'])
