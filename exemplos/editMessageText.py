from inline import inline_keyboard ## Gerador de botões inline
from inline import identifier ## Identificador para a edição da mensagem
from inline import data ## Retorno dos botões (callback_data)
from metodos import editMessageText ## Metodo que edita mensagem

def infos(msg):
    idf = identifier(msg) ## Identificador
    
    keyboard = [[{'text': '☕️Github', 'url': 'https://github.com/francis-taylor/Timotty-Master'}] + 
    [{'text': '👤Dev', 'url': 'https://t.me/francistaylor'}]] ## Sintaxe do teclado
    
    markup = inline_keyboard(keyboard) ## Gera o botão
    
    if data == 'info':
        editMessageText(idf,'Versão: 1.3', parse_mode='Markdown', reply_markup=markup) ## Edita a mensagem