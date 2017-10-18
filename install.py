# -*- coding: utf-8 -*-
import os,sys,time

if raw_input(u'Deseja iniciar instalação do Timotty? [Y/N]\n\n>>> ').lower() == 'y':
    print(u'Iniciando...')

    try:
        import requests
    except:
        print(u'instalando Requests')
        os.system('pip install requests')
    try:
        import redis
    except:
        print(u'instalando Redis-Server')
        os.system('pip install redis')

    os.system('clear')
    print(u'Instalação concluída!')
    time.sleep(2)
    os.system('clear')
    print('abra o arquivo config.py e edite-o conforme os exemplos.')
    time.sleep(5)

    os.system('clear')
    sys.exit()

else:
    sys.exit()
