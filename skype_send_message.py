import skype as sk1
from skpy import Skype, SkypeChats

def Skype_send_to_common(text):
    #Функция отправляет в общий чат Челябинск ОП3 заготовленный текст
    sk = Skype(sk1.username, sk1.password) # connect to Skype
    ch = sk.chats[sk1.common] # групповой чат Челябинск ОП3
    ch.sendMsg(text) # отправка сообщения
def Skype_send_to_territory(text):
    #Функция отправляет в общий чат Челябинск ОП3 заготовленный текст
    sk = Skype(sk1.username, sk1.password) # connect to Skype
    ch = sk.chats[sk1.territory] # групповой чат Территориалы 2.0
    ch.sendMsg(text) # отправка сообщения

def Skype_send_to_test(text):
    #Функция отправляет в общий чат Челябинск ОП3 заготовленный текст
    sk = Skype(sk1.username, sk1.password) # connect to Skype
    ch = sk.chats[sk1.test] # групповой чат Тест
    ch.sendMsg(text) # отправка сообщения