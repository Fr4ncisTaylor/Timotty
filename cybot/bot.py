# -*- coding: utf-8 -*-
import json
import os
import requests
import time
from threading import Thread, local
from pprint import pprint
import metodos
from comandos import comandos
import config
import sys
from mensagens import creditos
from diskcache import Cache

# Definindo BOT
bot = metodos
# Definindo cache para bot_is_on
cache = Cache('tmp/mycachedir')
cache['bot_is_on'] = True
# Classe Threads que manterá o bot on


class Th(Thread) :
    def __init__ (self, msgs):
        Thread.__init__(self)
        self.msgs = msgs

    def run(self) :

        if self.msgs.get('message', None) is not None :
            msg = self.msgs['message']
            content_type = 'text'
        elif self.msgs.get('edited_message', None) is not None :
            msg = self.msgs['edited_message']

        elif self.msgs.get('channel_post', None) is not None :
            msg = self.msgs['channel_post']

        elif self.msgs.get('edited_channel_post', None) is not None :
            msg = self.msgs['edited_channel_post']

        elif self.msgs.get('inline_query', None) is not None :
            msg = self.msgs['inline_query']

        elif self.msgs.get('chosen_inline_result', None) is not None :
            msg = self.msgs['chosen_inline_result']

        elif self.msgs.get('callback_query', None) is not None :
            msgs = self.msgs['callback_query']

        elif self.msgs.get('shipping_query', None) is not None :
            msg = self.msgs['shipping_query']

        elif self.msgs.get('pre_checkout_query', None) is not None :
            msg = self.msgs['pre_checkout_query']

        else :
            return

        if (time.time() - msg['date']) > config.timer :
            return

        comandos(msg, content_type) ## Importando os comandos para dentro do bot
        return


dados_bot = bot.getMe()
threads = config.th
offset = config.offset

if len(config.bot) > 10:
    print(creditos['mensagem'].format(metodos.getMe()['result']['first_name'],metodos.getMe()['result']['username']))
    print(creditos['creditos'].format(creditos['autor'],creditos['url'],creditos['user']))
else:
    print('Token inválido.')
    sys.exit()

while True :
    threads.append(bot.getUpdates(offset=offset))

    for (i, msgs) in enumerate(threads[-1]['result']) :
        t = Th(msgs)
        print('th', i)
        t.start()

        offset = int(msgs['update_id']) + config.update_id

    del threads[:]