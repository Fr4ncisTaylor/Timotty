# -*- coding: utf-8 -*-
import requests,json,sys
from config import apis,idioma
from metodos import sendMessage

def traduzir(msg):

    if msg['text'].startswith('/traduza'):

        texto = msg['text'].replace('/traduza ','')
        url = apis['tradutor']

        a = requests.get(url+texto)
        b = a.text
        c = json.loads(b)
        print(c)
        lang = c['data']['translations'][0][u'detectedSourceLanguage']
        text = c['data']['translations'][0]['translatedText'].replace(";", "")

        sendMessage(msg['chat']['id'],"Tradução:<br/><br/><b>{}</b><br/><br/> Idioma detectado: <b>{}</b>".format(text,lang).replace("[", "").replace("39", "").replace("&", "").replace("#", "").replace("]", "").encode("utf-8"),parse_mode='HTML')
