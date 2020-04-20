import skype as sk1
from skpy import Skype, SkypeChats

def Skype_send_to_common(text):
    sk = Skype(sk1.username, sk1.password) # connect to Skype
    ch = sk.chats[sk1.common] # групповой чат Челябинск ОП3
    ch.sendMsg(text) # отправка сообщения
