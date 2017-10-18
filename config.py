# -*- coding:utf-8 -*-

adms = [1111111,222222,333333] #digite os ids dos adms

sudo = [0000000] # Seu ID


bot = '' ## Token do bot gerado no @BotFather

grupo_url ='https://t.me/RoboTaylor' ## grupo do bot

#####  NÃO MEXA NOS VALORES ABAIXO

th = [] ## Não adicione nada aqui.
offset = 0 ## Valor do offset
update_id = 1 ## Não mude isso
timer = 60 ## Não mude isso
api = 'https://api.telegram.org/bot' # NÃO ALTERE ISSO

##### config REDIS_SERVER

redis = {    'host' : 'localhost',
             'port' : 6379,
               'db' : 5}

###### KEYS  & CONFIGS

#print
key_print = '' ### key da api
dim_print = '1024xfull'
format_print = 'img'

##### APIS

apis = {'print' :  "http://api.screenshotmachine.com/?key={}&dimension={}&format={}&url=".format(key_print,dim_print,format_print),
        }