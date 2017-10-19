# -*- coding: utf-8 -*-
import os,sys,time

if raw_input(u'Deseja iniciar instalação do Timotty para Python 2+ ? [Y/N]\n\n>>> ').lower() == 'y':
    print(u'Iniciando...')

    try:
        import requests
    except:
        print(u'Instalando Requests')
        os.system('pip install requests')
    try:
        import redis
    except:
        print(u'Instalando Redis-Server')
        os.system('pip install redis')

    os.system('clear')
    print(u'Instalação concluída!')
    time.sleep(2)
    os.system('clear')

    if raw_input('Deseja iniciar Timotty? [Y/N]\n\n> '):
        os.system('python bot.py')
    else:
        os.system('clear')
        sys.exit()

else:
    sys.exit()
