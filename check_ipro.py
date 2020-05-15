import requests
from managers import *
import datetime
import time
import skype_send_message as ssm
import json
import sys

def check_ipro():
    d = datetime.date.today()
    year = str(d.year)
    year = int(year[:-2])
    day = d.day + -1 #изменить на -1!!!
    month = d.month
    date_end = '{:02}'.format(day) + '/' + '{:02}'.format(month) + '/' + '{:02}'.format(year)
    date_begin = '01' + '/' + '{:02}'.format(month) + '/' + '{:02}'.format(year)

    site = 'https://ipro.etm.ru/cat/buildbrowser.html'
    payload = {
        'dataType': 'jsonp',
        'man' : '39004296',
        'login' : '08mas',
        'syf_prog' : 'pr_meeting-rsp',
        'RSPAction' : 'B',
        'body' : 'pr_meeting',
        'whichTableRowid' : 'pr_meeting',
        #'fieldlist' : 'RO_subtheme,whencre,pme_datep,pme_datef,RO_client^all,RO_person_etm^class37Inc,pme_task,RO_state,pme_comdoc,pme_result,pme_subtheme',
        'fieldlist' : 'pme_datep,RO_client^all,RO_person_etm^class37Inc',
        'd1' : date_begin,
        'd2' : date_end,
        #'filterpme_comment' : None,
        'filterpme_state' : 'appoint',
        'showSubTheme' : 'notArchive',
        'filterpme_subtheme' : 'ВТ1040',
        #'filterexm_mancode' : None,
        'mycli' : 'false',
        'onlyMy' : 'false',
        #'taskSearch' : None,
        'codeRC63' : 'УП04',
        'codeOP' : 'УЧел3',
        #'callback' : 'jQuery18207107582847141982_1589433817024',
        #'_search' : 'false',
        #'nd' : '1589434017821',
        #'rows' : '20',
        #'page' : '1',
        #'sidx' : 'pme_datep',
        #'sord' : 'desc',
        #'_' : '1589434017821',

    }
    
    
    val = requests.get(site, params=payload, )
    

    spam = val.url
    print(spam)
    #тестируем варианты
    #server_message = r'{ "page":"0","rows":[ ],"total":0,"records": 0,"userdata":{"error":"","limit":"no " )'
    #server_message = r'{ "page":"1","rows":[ {"id": "0x0000000006462901", "cell":["20/05/20","160022026 - МАВР (Москалев) Москалев Артем Александрович Главный бухгалтер (!)","ОП3 Челябинск : Патракова Елена Сергеевна"]},{"id": "0x00000000064628a4", "cell":["20/05/20","36119713 - Курлыкова В.В. ИП Курлыкова Владислава Викторовна Начальник отдела логистики","ОП3 Челябинск : Патракова Елена Сергеевна"]},{"id": "0x0000000006462193", "cell":["20/05/20","1505294 - ОПТИМАПРАЙС Куратова Ирина Николаевна Продавец","ОП3 Челябинск : Патракова Елена Сергеевна"]},{"id": "0x0000000006461f04", "cell":["18/05/20","160146121 - Савченко И.О. ИП","ОП3 Челябинск : Акимова Вера Михайловна"]},{"id": "0x0000000006445b04", "cell":["18/05/20","160045765 - Аргунов Е.С. ИП","ОП3 Челябинск : Никитина Екатерина Сергеевна"]},{"id": "0x0000000006445a87", "cell":["18/05/20","36123101 - Сергеева А.С.","ОП3 Челябинск : Никитина Екатерина Сергеевна"]},{"id": "0x0000000006445a10", "cell":["18/05/20","160048916 - Батурбаева Г.Р. ИП","ОП3 Челябинск : Никитина Екатерина Сергеевна"]},{"id": "0x000000000642a581", "cell":["20/05/20","70017203 - Электроплюс Терещенко Илья Анатольевич Владелец/Собственник","ОП3 Челябинск : Мельникова Алена Александровна"]},{"id": "0x000000000642a10e", "cell":["21/05/20","600000106 - Антарес ООО Маг. Неповинный Захар Специалист по снабжению","ОП3 Челябинск : Дружинина Светлана Владиславовна"]},{"id": "0x000000000625f008", "cell":["19/05/20","70018520 - ОЗЭМИ ТД ООО Евгений . Генеральный директор (!)","ОП3 Челябинск : Котлярова Наталья Владимировна"]},{"id": "0x000000000613e50a", "cell":["22/05/20","70014699 - Сигма ООО Копейск Маслов Валентин Витальевич Главный энергетик (!)","ОП3 Челябинск : Михайлова Елена Михайловна"]},{"id": "0x0000000006131086", "cell":["22/05/20","36124825 - Снежинский ЗСЭМ ООО Смолина Ольга Евгеньевна Начальник отдела снабжения (ОМТС, УМТО) (!)","ОП3 Челябинск : Прохоров Александр Георгиевич"]},{"id": "0x0000000006105e85", "cell":["13/05/20","36139504 - АРГАЯШАГРОПРОМЭНЕРГО ООО Василенко Валерий Владимирович Владелец/Собственник","ОП3 Челябинск : Харламов Егор Александрович"]},{"id": "0x00000000060a0b85", "cell":["20/05/20","36120991 - Рускомплект ООО Чел.","ОП3 Челябинск : Котлярова Наталья Владимировна"]},{"id": "0x00000000060a0a14", "cell":["20/05/20","36116610 - Росэнерго-Чел","ОП3 Челябинск : Котлярова Наталья Владимировна"]},{"id": "0x00000000060a0988", "cell":["20/05/20","36123070 - Энергет.технологии2","ОП3 Челябинск : Харламов Егор Александрович"]},{"id": "0x00000000060a091b", "cell":["20/05/20","36150029 - Климат-Тех","ОП3 Челябинск : Низамов Роман Фаридович"]},{"id": "0x00000000060a0807", "cell":["20/05/20","36116645 - 220 Вольт","ОП3 Челябинск : Котлярова Наталья Владимировна"]},{"id": "0x00000000060a0684", "cell":["20/05/20","70016882 - Менщиков Г.В. ИП Чел","ОП3 Челябинск : Мельникова Алена Александровна"]},{"id": "0x0000000005f49314", "cell":["20/05/20","70000384 - ЮЖУРАЛЭЛЕКТР-КА ООО","ОП3 Челябинск : Котлярова Наталья Владимировна"]}],"total":2,"records": 22,"userdata":{"error":"","limit":"no "}} )'
    server_message = input('Скопируй, что появилось в браузере: ')
    if '"page":"0",' in server_message:
        print('Нет пропущенных айпро на сегодня!') 
    else:        
        val = server_message.find('"id"')
        server_message = server_message[val-1:]

        server_message = server_message.split('"id": ')



        answer = []
        for line in server_message:
            #if '"total":' not in line:
            line = line.replace('ОП3 Челябинск : ', '')
            begin = line.find(' - ') + 3
            end = line.find('"]},', begin + 3)
            
            line = line[begin:end]
            line = line.replace('","', ' - ')
            if ']}],' in line:
                end = line.find(']}],')
                line = line[:end]
            answer.append(line)

        if answer[0] == '':
            answer = answer[1:]
        # формируем сообщение в чат        
        message = '(pointdownindex)' * 8 + '\n'
        if len(answer) == 0:
            return print('Нет пропущенных встреч по айпро на сегодня!')       
        else:
            message += 'Сегодня пропущенных встреч по айпро: ' + str(len(answer)) + '!\n'
            if day > 24:
                message += 'Срочно закрыть!!!!\n'
            else:
                message += 'Срочно закрыть или перенести!\n'
            message += 'Пропустившие: \n'
            for line in answer:
                message += line + '\n'
        message += '(pointupindex)' * 8 + '\n'
        # отправляем сообщение в скайп
        ssm.Skype_send_to_common(message)


if __name__ == "__main__":

    check_ipro()