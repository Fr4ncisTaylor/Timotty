from metodos import sendMessage ## Importa a função de enviar mensagem

def exemplo(msg):
  chat_id = msg['chat']['id'] ## Pega o ID do chat
  
  sendMessage(chat,id, 'Hello World') ## Envia a mensagem