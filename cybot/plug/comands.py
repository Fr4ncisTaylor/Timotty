from mensagens import *
from metodos import *


def comands(msg):
    if 'text' in msg:
        texto = msg[u'text'].encode('utf-8')
        chat_id = msg['chat']['id']
        nome = msg['from'][u'first_name']
        from_id = msg['from']['id']

        if texto == '/comandos':
            sendMessage(chat_id, comands['mensagem'].format(nome), parse_mode='Markdown')

