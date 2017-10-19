# -*- coding:utf-8 -*-

from cybot.aiml import Kernel
from cybot import config
from cybot.metodos import sendMessage,getMe,sendChatAction
from cybot.config import sudo
import sys,time,os
kernel = Kernel()
kernel.learn(config.ia['mae'])
kernel.respond(config.ia['cerebro'])

 		
		
def cmd(msg):
    if msg['text'].startswith('/add'):
        if msg['from']['id'] == sudo:
            text = msg['text'].replace('/add ', '')
            pergunta = text.split('|', 1)[0]
            resposta = text.split('|', 1)[1]
            sendMessage(msg['chat']['id'], escreva(pergunta, resposta))
            time.sleep(2)
            os.execl(sys.executable, sys.executable, *sys.argv)

def leia(arquivo):
    ### PEGA A ULTIMA LINHA
    aiml = open(arquivo, 'r')  # abre o aquivo para leitura

    line = aiml.readlines()  # le as linhas do arquivo
    line = '{}'.format(line[-1])  # pega a ultima linha e formata como string caso nao seja

    print 'line: ' + line  ## printa a linha no terminal
    aiml.close()  # fecha o arquivo

    ### LÊ O ARQUIVO INTEIRO
    aiml = open(arquivo, 'r')  # abre o arquivo para leitura
    read = aiml.read()  # le o arquivo completo

    ### REMOVE A ULTIMA LINHA
    read = '{}'.format(read)  # formata como string
    read = read.replace('{}'.format(line), '')  # apaga da leitura a ultima linha
    aiml.close()  # fecha o arquivo
    return read

def escreva(pergunta, resposta):
    arquivo = "/home/francis/Área de Trabalho/cybot/aiml/cerebro/manual.aiml"
    read = leia(arquivo)  # importa os resultados da funçao leia

    print pergunta
    print resposta
    msg = '''{}
    <category>
        <pattern>{}</pattern>
        <template>
           {}
        </template>
    </category>
</aiml>'''  # define a mensagem que sera escrita
    msg = msg.format(read, pergunta.upper(),
                     resposta)  # coloca no 1 o conteudo antigo, e adiciona a pergunta e a resposta

    aiml = open(arquivo, 'w')  # abre o arquivo para escrita
    aiml.write(msg)  # escreve a mensagem formatada
    aiml.close()  # fecha o arquivo
    return 'concluído.'

def conversa(msg):
    cmd(msg)
    if '/' not in msg['text']:
        if msg['chat']['type'] == 'supergroup' or msg['chat']['type'] == 'group':

            try:
                reply = msg['reply_to_message']['from']['id'] == getMe()['id']

            except:
                reply = 0

                if reply == getMe()['id']:
                    sendChatAction(msg['chat']['id'],'typing') ## envia o 'escrevendo...'

                    resposta = kernel.respond(msg['text']) ## resposta

                    sendMessage(msg['chat']['id'], resposta,reply_to_message_id=msg['message_id'])
        else:
            sendChatAction(msg['chat']['id'], 'typing')  ## envia o 'escrevendo...'

            resposta = kernel.respond(msg['text'])  ## resposta

            sendMessage(msg['chat']['id'], resposta, reply_to_message_id=msg['message_id'])

        return

