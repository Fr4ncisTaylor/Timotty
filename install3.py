# -*- coding: utf-8 -*-
import os,sys,time

if input(u'Deseja iniciar instalação do Timotty? [Y/N]\n\n>>> ').lower() == 'y':
    print(u'Iniciando...')

    try:
        import requests
    except:
        print(u'Instalando o Requests')
        os.system('pip3 install requests')
    try:
        import redis
    except:
        print(u'Instalando o Redis-Server')
        os.system('pip3 install redis')

    os.system('clear')
    print(u'Instalação concluída!')
    time.sleep(2)
    os.system('clear')

    if input('Deseja iniciar Timotty? [Y/N]\n\n> '):
        os.system('python3 bot.py')
    else:
        os.system('clear')
        sys.exit()

else:
    sys.exit()
