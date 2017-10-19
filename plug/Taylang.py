#-*-coding:utf8;-*-
#qpy:2

import sys,os

reload(sys)

sys.setdefaultencoding('utf8')

def lang(self):
        if self == "pt":
            return "português"
        elif self == "en":
            return "inglês"
        elif self == "ar":
            return "árabe"
        elif self == "af":
            return "africanês"
        elif self == "es":
            return "espanhol"
        elif self == "de":
            return "alemão"
        elif self == "ca":
            return "Catalão"
        elif self == "zn-CN":
            return "Chinês Simples"
        elif self == "zn-TW":
            return "Chinês Tradicional"
        elif self == "tl":
            return "Filipino"
        elif self == "fr":
            return "Francês"
        elif self == "haw":
            return "Havaiano"
        elif self == 'it':
            return "Italiano"
        elif self == "ja":
            return "Japonês"
        elif self == "kn":
            return "Canadense" 
        elif self == "la":
            return "Latin"
        elif self == "ne":
            return "Nepali"
        elif self == "fa":
            return "Persa"
        elif self == "ru":
            return "Russo"
        elif self == "sl":
            return "eslovaca"
        else:
            return "🙇"
