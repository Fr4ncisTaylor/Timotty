# -*- coding: utf-8 -*-

import json
import os
import requests
import time
from threading import Thread
from pprint import pprint
import metodos
from comandos import comandos
import config
import sys
from mensagens import creditos

# definindo BOT
bot = metodos
# Classe Threads que manterá o bot on


class Th(Thread) :
    def __init__ (self, msgs):
        Thread.__init__(self)
        self.msgs = msgs

    def run(self) :

        if self.msgs.get('message', None) is not None :
            msg = self.msgs['message']
            content_type = 'text'

        else :
            return

        if (time.time() - msg['date']) > config.timer :
            return


        comandos(msg)## importando os comandos para dentro do bot

dados_bot = bot.getMe()
threads = config.th
offset = config.offset

if len(config.bot) > 10:
    print creditos['mensagem'].format(metodos.getMe()['first_name'],metodos.getMe()['username'])
    print creditos['creditos'].format(creditos['autor'],creditos['url'],creditos['user'])
else:
    print('Token inválida.')
    sys.exit()

while True :
    threads.append(bot.getUpdates(offset=offset))

    for (i, msgs) in enumerate(threads[-1]['result']) :
        t = Th(msgs)
        t.start()

        offset = int(msgs['update_id']) + config.update_id

    del threads[:]
