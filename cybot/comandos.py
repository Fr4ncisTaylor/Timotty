# -*- coding:utf-8 -*-
import sys
import redis
from metodos import sendMessage
import config
from plug.ia import conversa
from plug import banhammer, comands, myid, newmember, printar, promover, start, tradutor, regras, qr#, info
from diskcache import Cache

### Redis server
redis = redis.StrictRedis(host=config.redis['host'], port=config.redis['port'], db=config.redis['db'])

### Definindo cache para bot_is_on
cache = Cache('tmp/mycachedir')

### Plugins
def comandos(msg, content_type):

    if content_type == 'text':

        if msg['text'].startswith('/run'):
            if msg['from']['id'] == config.sudo:
                cmd = msg['text'].replace('/run ','')
                if cmd == 'on':
                    cache['bot_is_on'] = True
                elif cmd == 'off':
                    cache['bot_is_on'] = False
                sendMessage(msg['chat']['id'], 'Alterando as configurações para *{}*'.format(cmd),"markdown")
                return
            
        status = cache['bot_is_on']
        if status:
            print("ok")
            regras.regras(msg) # Modulo de regras

            myid.my_id(msg) # Modulo do comando /id

            newmember.welcome(msg) # Modulo de boas vindas

            promover.promover(msg) # mudulo de divulgação

            start.start(msg) # Modulo de inicialização

            banhammer.banhammer(msg) # Modulo de administração

            printar.printar(msg) # Modulo do comando /print

            comands.comands(msg) # Modulo do comando /comandos

            conversa(msg) # Modulo de inteligencia artificial

            tradutor.traduzir(msg) #modulo de tradução

            qr.make_qr(msg) #  Modulo do comando /qr
    
    if content_type == 'callback':
        info.infos(msg)
