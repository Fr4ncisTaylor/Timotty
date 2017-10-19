# -*- coding:utf-8 -*-

adms = [000000,111111,22222] #digite os ids dos adms

sudo =  0000000 # Seu ID

idioma = 'pt-br'

bot = '' ## Token do bot gerado no @BotFather

grupo_url ='https://t.me/RoboTaylor' ## grupo do bot

#####  NÃO MEXA NOS VALORES ABAIXO

th = [] ## Não adicione nada aqui.
offset = 0 ## Valor do offset
update_id = 1 ## Não mude isso
timer = 999 ## Não mude isso
api = 'https://api.telegram.org/bot' # NÃO ALTERE ISSO

##### config REDIS_SERVER

redis = {    'host' : 'localhost',
             'port' : 6379,
               'db' : 5}
aiml = {'principal' : 'principal.xml',
        '':''}
###### KEYS  & CONFIGS

keys = {
       'print' : '', ## key api print
    'tradutor' : '',## key tradutor google

        }

#print


aprint = {
        'api' : "http://api.screenshotmachine.com/?key={}&dimension={}&format={}&url=",
        'key' : keys['print'],
   'dimensao' : '1024xfull',
     'format' : 'img'}

# tradutor
tradutor = {
           'api':"https://www.googleapis.com/language/translate/v2?key={}&target={}&format=html&q=",
           'key':keys['tradutor']}

# QR code
qr_code = {'api' : "http://chart.apis.google.com/chart?cht=qr&chl={}&chs=120x120"}

##### APIS

apis = {'print' :  aprint['api'].format(aprint['key'],aprint['dimensao'],aprint['format']),
        'tradutor' : tradutor['api'].format(tradutor['key'],idioma),
        'qr' : qr_code['api']
        }

##### diretorios

ia = {'mae' : 'plug/mae.xml',
      'cerebro' : 'responda'}