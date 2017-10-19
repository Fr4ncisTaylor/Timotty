# -*- coding:utf-8 -*-

from cybot.config import apis
from cybot.metodos import sendPhoto

def make_qr(msg):
    if msg['text'].startswith('/qr'):
        texto = msg['text'].replace('/qr ', '')
        print sendPhoto(msg['chat']['id'], photo=apis['qr'].format(texto))