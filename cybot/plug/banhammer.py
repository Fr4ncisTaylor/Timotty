# -*- coding:utf-8 -*-

import cybot.config
from cybot.metodos import *
from cybot.mensagens import *


adms = config.adms
def ban(msg):
    if msg['text'] == '/ban':
        from_id = msg['from']['id']
        chat_id = msg['chat']['id']

        if from_id in adms:
            try:
                reply_id = msg['reply_to_message']['from']['id']
                reply = True
            except:
                reply = False

            if reply == True:
                if 'error_code' not in  kickChatMember(chat_id, reply_id):
                    sendMessage(chat_id, ban['banido'].format(msg['from']['first_name']))
                else:
                    sendMessage(chat_id,ban['404'])

            else:
                sendMessage(chat_id, erros['reply'])
        else:
            sendMessage(chat_id,erros['admin'])

def unban(msg):
    if msg['text'] == '/desban':
        from_id = msg['from']['id']
        chat_id = msg['chat']['id']

        if from_id in adms:
            try:
                reply_id = msg['reply_to_message']['from']['id']
                reply = True
            except:
                reply = False

            if reply == True:
                if 'error_code' not in  unbanChatMember(chat_id, reply_id):
                    sendMessage(chat_id, ban['desbanido'].format(msg['from']['first_name']))
                else:
                    sendMessage(chat_id,ban['404'])

            else:
                sendMessage(chat_id, erros['reply'])
        else:
            sendMessage(chat_id,erros['admin'])


def kick(msg):
    if msg['text'] == '/kick':
        from_id = msg['from']['id']
        chat_id = msg['chat']['id']

        if from_id in adms:
            try:
                reply_id = msg['reply_to_message']['from']['id']
                reply = True
            except:
                reply = False

            if reply == True:
                if 'error_code' not in  kickChatMember(chat_id, reply_id) and 'error_code' not in  unbanChatMember(chat_id, reply_id):
                    sendMessage(chat_id, ban['kickado'].format(msg['from']['first_name']))
                else:
                    sendMessage(chat_id,ban['404'])

            else:
                sendMessage(chat_id, erros['reply'])
        else:
            sendMessage(chat_id,erros['admin'])


def banhammer(msg):
    ban(msg)
    kick(msg)
    unban(msg)
