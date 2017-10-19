# -*- coding: utf-8 -*-

from cybot import mensagens
from cybot.inline import make_url
from cybot.metodos import *

m = mensagens

def start(msg):
    if 'text' in msg:
        texto = msg[u'text'].encode('utf-8')
        chat_id = msg['chat']['id']
        nome = msg['from'][u'first_name']
        from_id = msg['from']['id']

        if texto == '/start':

            keyboard = [[{'text': m.start['bot1'], 'url': config.grupo_url}] +
                        [{'text':m.start['bot2'], 'url': mensagens.creditos['url']}]]

            markup = make_url(keyboard)
            sendMessage(chat_id, m.start['mensagem'].format(nome), reply_markup=markup)
