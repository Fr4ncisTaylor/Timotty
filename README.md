# Timotty-Master

![Timotty](images.png)

[TimottyBot](https://t.me/TimottyBot)

[Suporte](https://t.me/RoboTaylor)

⚜️**Versão 1.1 | Python 2 ou 3+**

* * *
## Informações
Timotty foi desenvolvido com as Threads nativa da linguagem Python.
Ele ultiliza os métodos da API Telegram, que você pode encontar no arquivo `/cybot/metodos.py`.

* * *
Comandos Normais
------------
<table>
  <thead>
    <tr>
      <td><strong>Comando</strong></td>
      <td><strong>Uso</strong></td>
      <td><strong>Descrição</strong></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Id</td>
      <td>/id (Reply)</td>
      <td>Exibe informações sobre o perfil do usuário.</td>
    </tr>
    <tr>
      <td>Print</td>
      <td>/print [url]</td>
      <td>Envia um print do site informado.</td>
    </tr>
    <tr>
      <td>Traduza</td>
      <td>/traduza [texto]</td>
      <td>Traduz um texto de qualquer idioma para o portugês.</td>
    </tr>
    <tr>
     <td>Qr</td>
     <td>/qr [url/texto]</td>
     <td>Envia um Qr Code do site ou texto informado.</td>
   </tr>
    <tr>
      <td>Ban</td>
   <td>/ban (reply)</td>
      <td>Bane o membro do chat.</td>
    </tr>
    <tr>
      <td>Desban</td>
      <td>/desban (reply)</td>
     <td>Desbane o membro do chat.</td>
    </tr>
    <tr>
      <td>Kick</td>
      <td>/kick (reply)</td>
      <td>Remove o membro do chat.</td>
    </tr>
  </tbody>
</table>

Comando Sudo
------------
<table>
  <thead>
    <tr>
      <td><strong>Comando</strong></td>
      <td><strong>Uso</strong></td>
      <td><strong>Descrição</strong></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Promover</td>
      <td>/promover [texto]</td>
      <td>Promove uma divulgação nos chats privados.</td>
    </tr>
    <tr>
      <td>Run</td>
      <td>/run (on/off)</td>
      <td>Liga ou desliga o bot.</td>
    </tr>
    <tr>
      <td>Add</td>
      <td>/add [pergunta|resposta]</td>
      <td>Adiciona a pergunta e a resposta na I.A do bot.</td>
    </tr>
  </tbody>
</table>

* * *
## Instalação

Clone o repositório:
`git clone https://github.com/francis-taylor/Timotty-Master`

Entre no diretório:
`cd Timotty-Master`

Execute a instalação:

* python 2: `python install2.py`

* python 3: `python3 install3.py`

* * *
## Configuração
* Abra o arquivo `cybot/config.py` e insira o ID dos Administradores do bot em `adms = [000000,111111,22222]`.

* Insira o seu ID no espaço `sudo =  0000000`.

* Coloque o token do seu bot que foi gerado pelo [Bot Father](https://t.me/BotFather) no `bot = '110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw'`

* * *
## Iniciando o bot

* python 2: `python bot.py`

* python 3: `python3 bot.py`

### ou

* python 2: `nohup python bot.py`

* python 3: `nohup python3 bot.py`

* * *
## Exemplos

### Editar mensagens

```from inline import inline_keyboard, identifier, data
from metodos import editMessageText

def info(msg):
    idf = identifier(msg) #identifica a mensagem
    
    #define o teclado
    keyboard = [[{'text': '☕️Github', 'url': 'https://github.com/francis-taylor/Timotty-Master'}] + 
               [{'text': '👤Dev', 'url': 'https://t.me/francistaylor'}]]
    
    #formata o teclado
    markup = inline_keyboard(keyboard)
    
    #identifica o retorno do botão
    if data == 'info':
        editMessageText(idf,'Versão: 1.3\n', parse_mode='Markdown', reply_markup=markup) #edita a mensagem
        ```
        
* * *
## Agradecimentos

Agradeço ao [Murkiriel](https://t.me/Mkriel) por ter me ajudado com o projeto.
