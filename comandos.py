# -*- coding:utf-8 -*-
import redis,sys,config, metodos
from cybot import mensagens
from plug.newmember import welcome
from plug.promover import promover
from plug.start import start
from plug.myid import my_id
from plug.banhammer import banhammer
from plug.printar import printar
from plug.comands import comands
from plug.regras import regras






''' caso você use linux, mantenha o sisteminha encode abaixo...'''

## default encoding
reload(sys)
sys.setdefaultencoding('utf8')

### redis server
redis = redis.StrictRedis(host=config.redis['host'], port=config.redis['port'], db=config.redis['db'])

### plugins
def comandos(msg):
    if 'text' in msg:
        my_id(msg)
        welcome(msg)
        promover(msg)
        start(msg)
        banhammer(msg)
        printar(msg)
        comands(msg)

