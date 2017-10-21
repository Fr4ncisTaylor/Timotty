# -*- coding: utf-8 -*-
import os,sys,time

if raw_input(u'Deseja iniciar instalação do Timotty para Python 2+ ? [Y/N]\n\n>>> ').lower() == 'y':
    print(u'Iniciando...')

    try:
        import requests
    except:
        print(u'Instalando o Requests')
        os.system('pip2 install requests')
    try:
        import redis
    except:
        print(u'Instalando o Redis-Server')
        os.system('pip2 install redis')
    try:
        import diskcache
    except:
        print(u'Instalando o DiskCache')
        os.system('pip2 install diskcache')

    os.system('clear')
    print(u'Instalação concluída!')
    time.sleep(2)
    os.system('clear')

    if raw_input('Deseja iniciar Timotty? [Y/N]\n\n> '):
        os.system('python2 cybot/bot.py')
    else:
        os.system('clear')
        sys.exit()

else:
    sys.exit()
