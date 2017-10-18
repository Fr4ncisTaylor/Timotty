# -*- coding: utf-8 -*-
from cybot.config import apis
from cybot.metodos import sendPhoto

def printar(msg):
    if msg['text'].startswith('/print'):
        texto = msg['text'].replace('/print','')
        sendPhoto(msg['chat']['id'], apis['print']+texto)
