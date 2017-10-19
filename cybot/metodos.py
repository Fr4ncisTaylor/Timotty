import json
import requests
import config
import os

bot = config.bot
api = config.api
api_bot = api + bot

#### UPDATES ######
def getMe() :
    url = api_bot + '/getMe'
    r = requests.post(url)
    jsons = json.loads(r.content)['result']
    return jsons

def getUpdates( allowed_updates = None,limit = None,offset = None,timeout = None) :
    url = api_bot + '/getUpdates'
    payload = {'allowed_updates' : allowed_updates,
                         'limit' : limit,
                        'offset' : offset,
                       'timeout' : timeout}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### MESSAGE  #####
def sendMessage(chat_id, text,parse_mode=None,disable_web_page_preview=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendMessage'
    payload = {      'chat_id' : chat_id,
        'disable_notification' : disable_notification,
    'disable_web_page_preview' : disable_web_page_preview,
                  'parse_mode' : parse_mode,
                'reply_markup' : reply_markup,
         'reply_to_message_id' : reply_to_message_id,
                        'text' : text,}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def replyMessage(chat_id, text,disable_notification=None,disable_web_page_preview=None,parse_mode=None,reply_markup=None,reply_to_message_id=None) :
    url = api_bot + '/sendMessage'
    payload = {      'chat_id' : chat_id,
        'disable_notification' : disable_notification,
    'disable_web_page_preview' : disable_web_page_preview,
                  'parse_mode' : parse_mode,
                'reply_markup' : reply_markup,
         'reply_to_message_id' : reply_to_message_id,
                        'text' : text,}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def forwardMessage(chat_id, from_chat_id, message_id,disable_notification=None):
    url = api_bot + '/forwardMessage'
    payload = {    'chat_id' : chat_id,
               'from_chat_id': from_chat_id,
                'message_id' : message_id,
      'disable_notification' : disable_notification,}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### STICKER
def sendSticker(chat_id,sticker,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendMessage'
    payload = {'chat_id': chat_id,
               'disable_notification': disable_notification,
               'reply_markup': reply_markup,
               'reply_to_message_id': reply_to_message_id,
               'sticker': sticker, }
    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### PHOTO
def sendPhoto(chat_id,photo,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):

    url = api_bot + '/sendPhoto'
    payload = {    'chat_id' : chat_id,
                     'photo' : photo,
                   'caption' : caption,
       'disable_notification': disable_notification,
       'reply_to_message_id' : reply_to_message_id,
              'reply_markup' : reply_markup,}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### AUDIO
def sendAudio(chat_id, audio,caption=None,duration=None,performer=None,title=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendAudio'
    payload = {    'chat_id' : chat_id,
                     'audio' : audio,
                   'caption' : caption,
                  'duration' : duration,
                 'performer' : performer,
                     'title' : title,
      'disable_notification' : disable_notification,
       'reply_to_message_id' : reply_to_message_id,
              'reply_markup' : reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### DOCUMENT
def sendDocument(chat_id, document,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):

    url = api_bot + '/sendDocument'
    payload = {'chat_id': chat_id,
               'document': document,
               'caption': caption,
               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### VIDEO
def sendVideo(chat_id, video,duration=None,width=None,height=None,caption=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):

    url = api_bot + '/sendVideo'
    payload = {'chat_id': chat_id,
               'video': video,
               'caption': caption,
               'duration': duration,
               'width': width,

               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def sendVideoNote(chat_id, video_note,duration=None,length=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):

    url = api_bot + '/sendVideoNote'
    payload = {'chat_id': chat_id,
               'video_note': video_note,
               'duration': duration,
               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### VOICE
def sendVoice(chat_id, voice,caption=None,duration=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):

    url = api_bot + '/sendVoice'
    payload = {'chat_id': chat_id,
               'voice': voice,
               'caption': caption,
               'duration': duration,
               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### lOCATION
def sendLocation(chat_id, latitude, longitude,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendLocation'
    payload = {'chat_id': chat_id,
               'latitude': latitude,
               'longitude': longitude,
               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### VENUE
def sendVenue(chat_id, latitude, longitude,title,address,foursquare_id=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendLocation'
    payload = {    'chat_id': chat_id,
                  'latitude': latitude,
                   'adress' : address,
            'foursquare_id' : foursquare_id,
                 'longitude': longitude,
      'disable_notification': disable_notification,
       'reply_to_message_id': reply_to_message_id,
              'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### CONTACT
def sendContact(chat_id, phone_number, first_name,last_name=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendContact'
    payload = {'chat_id': chat_id,
               'phone_number': phone_number,
               'first_name': first_name,
               'last_name': last_name,
               'disable_notification': disable_notification,
               'reply_to_message_id': reply_to_message_id,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

######### CHAT ACTION
def sendChatAction(chat_id, action):
    url = api_bot + '/sendChatAction'
    payload = {'chat_id': chat_id,
               'action': action,
               }

    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### PIN/UNPIN ####
def pinChatMessage(chat_id, message_id,disable_notification=None):
    url = api_bot + '/pinChatMessage'
    payload = {'chat_id': chat_id,
               'message_id': message_id,
               'disable_notification':disable_notification
               }

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def unpinChatMessage(chat_id):
    url = api_bot + '/unpinChatMessage'
    payload = {'chat_id': chat_id}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### LEAVE
def leaveChat(chat_id):
    url = api_bot + '/leaveChat'
    payload = {'chat_id': chat_id, }

    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### GETS
def getChat(chat_id):
    url = api_bot + '/getChat'
    payload = {'chat_id': chat_id, }

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def getChatAdministrators(chat_id):
    url = api_bot + '/getChatAdministrators'
    payload = {'chat_id': chat_id, }
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def getChatMembersCount(chat_id):
    url = api_bot + '/getChatMembersCount'
    payload = {'chat_id': chat_id, }
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def getChatMember(chat_id, user_id):
    url = api_bot + '/getChatMember'
    payload = {'chat_id': chat_id,
               'user_id' : user_id}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

### BANHAMMER
def kickChatMember(chat_id,user_id):
    url = api_bot + '/kickChatMember'
    payload = {'chat_id': chat_id,
               'user_id': user_id}
    r = requests.post(url, data=payload)
    j = json.loads(r.content)

    return j

def unbanChatMember(chat_id,user_id):
    url = api_bot + '/unbanChatMember'
    payload = {'chat_id': chat_id,
               'user_id': user_id}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def restrictChatMember(chat_id,user_id,until_date=None,can_send_message=None,can_send_media_messages_=None,can_send_other_messages=None,can_add_web_page_previews=None):
    url = api_bot + '/restrictChatMember'
    payload = {'chat_id': chat_id,
               'user_id': user_id,
               'until_date': until_date,
               'can_send_message': can_send_message,
               'can_send_media_messages_': can_send_media_messages_,
               'can_send_other_messages': can_send_other_messages,
               'can_add_web_page_previews': can_add_web_page_previews}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def promoteChatMember(chat_id,user_id,can_change_info=None,can_post_message=None,can_edit_messages=None,can_delete_messages=None,can_invite_users=None,can_restrict_members=None,can_pin_messages=None,can_promote_members=None):
    url = api_bot + '/promoteChatMember'
    payload = {'chat_id': chat_id,
               'user_id': user_id,
               'can_change_info': can_change_info,
               'can_post_message': can_post_message,
               'can_edit_messages':can_edit_messages,
               'can_delete_messages':can_delete_messages,
               'can_invite_users': can_invite_users,
               'can_restrict_members': can_restrict_members,
               'can_pin_messages': can_pin_messages,
               'can_promote_members' : can_promote_members}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def exportChatInviteLink(chat_id):
    url = api_bot + '/exportChatInviteLink'
    payload = {'chat_id': chat_id, }

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def setChatPhoto(chat_id,photo):
    url = api_bot + '/setChatPhoto'
    payload = {'chat_id': chat_id,
               'photo' : photo}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def setChatTitle(chat_id,title):
    url = api_bot + '/setChatTitle'
    payload = {'chat_id': chat_id,
               'title' : title}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def setChatDescription(chat_id,description):
    url = api_bot + '/setChatDescripton'
    payload = {'chat_id': chat_id,
               'description' : description}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### EDITS
def editMessageText(text,chat_id=None,message_id=None,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
    url = api_bot + '/editMessageText'
    payload = {'chat_id': chat_id,
               'message_id': message_id,
               'inline_message_id': inline_message_id,
               'text': text,
               'parse_mode': parse_mode,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def editMessageCaption(caption,chat_id=None,message_id=None,inline_message_id=None,disable_web_page_preview=None,reply_markup=None):
    url = api_bot + '/editMessageCaption'
    payload = {'chat_id': chat_id,
               'message_id': message_id,
               'inline_message_id': inline_message_id,
               'caption': caption,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def editMessageReplyMarkup(text,chat_id=None,message_id=None,inline_message_id=None,parse_mode=None,disable_web_page_preview=None,reply_markup=None):
    url = api_bot + '/editMessageReplyMarkup'
    payload = {'chat_id': chat_id,
               'message_id': message_id,
               'inline_message_id': inline_message_id,
               'text': text,
               'parse_mode': parse_mode,
               'reply_markup': reply_markup}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### DELETE
def deleteMessage(chat_id,message_id):
    url = api_bot + '/deleteMessage'
    payload = {'chat_id': chat_id,
               'message_id': message_id}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

def deleteChatPhoto(chat_id):
    url = api_bot + '/deleteChatPhoto'
    payload = {'chat_id': chat_id}

    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### GAME

def sendGame(chat_id,game_short_name,disable_notification=None,reply_to_message_id=None,reply_markup=None):
    url = api_bot + '/sendGame'
    payload = {'chat_id': chat_id,
               'disable_notification': disable_notification,
               'game_short_name' : game_short_name,
               'reply_markup': reply_markup,
               'reply_to_message_id': reply_to_message_id,}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def setGameScore(user_id,score,force=None,disable_edit_message=None,chat_id=None,message_id=None,inline_message_id=None):
    url = api_bot + '/sendGame'
    payload = {        'chat_id' : chat_id,
                       'user_id' : user_id,
                          'score': score,
                         'force' : force,
          'disable_edit_message' : disable_edit_message,
                    'message_id' : message_id,
             'inline_message_id' : inline_message_id}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

def getGameHighScores(user_id,chat_id=None,message_id=None,inline_message_id=None):
    url = api_bot + '/sendGame'
    payload = {'chat_id': chat_id,
               'user_id': user_id,
               'message_id': message_id,
               'inline_message_id': inline_message_id}
    r = requests.post(url, data=payload)
    return json.loads(r.content)

#### EXTRAS
def run(self):
    os.system('{}'.format(self))
