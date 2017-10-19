#coding:utf-8 -*-
import config, metodos
from mensagens import bemvindo
from pprint import *
from metodos import sendMessage

def welcome(msg):
    if 'new_chat_member' in msg:

        sendMessage(msg['chat']['id'], bemvindo['welcome'].format(msg['new_chat_member']['first_name']),reply_to_message_id=msg['message_id'])
        return

def byebye(msg):
    if 'left_chat_member' in msg:

        sendMessage(msg['chat']['id'],bemvindo['byebye'].format(msg['left_chat_member'][u'first_name']),reply_to_message_id=msg['message_id'])
        return

def shell(msg):
    welcome(msg)
