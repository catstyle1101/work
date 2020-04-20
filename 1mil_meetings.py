import requests
from managers import *
import csv
import datetime
import time

def row_to_list(row):
    # переводит ряды в список 
    big_row = []
    for row in reader:
        row = str(row)
        row = row[1:-2]
        row = row.split(';')
        big_row.append(row)
    #print(big_row)
    return big_row

def client_num(row):
    # возвращает список номеров клиентов в формате str(1 колонка таблицы)
    client_num = []
    for i in row:
        val = i[0].rindex('(') + 1
        val1 = i[0].rindex(')')
        client_num.append(str(i[0][val: val1]))
    #print(client_num)
    return(client_num)

def manager_num(row):
    # подбирает код менеджера по фамилии
    manager_num = []
    for i in row:
        val = i[2].strip()
        for j in managers_list:
                if val == j.get('fullname'):
                    manager_num.append(str(j.get('code')))
    return manager_num

def date():
    #приводит текущую дату к виду 00/00/00
    d = datetime.date.today()
    year = str(d.year)
    year = int(year[:-2])
    day = d.day 
    month = d.month
    return '{:02}'.format(day)+ '/' + '{:02}'.format(month) + '/' + '{:02}'.format(year)

def push(client, manager, date, list):
    #отправляет данные для добавления сделок в ежедневник
    for i in range(0, len(client)):
        str1 = 'https://ipro.etm.ru/cat/runprog.html?man=39004296&login=08mas&syf_prog=pr_meeting-rsp&withoutArchive=yes&RSPAction=A&idLabel=id&id=0x0000000005c25b0c&pme_comdoc=&pme_persons=pmp_class37^УЧел3$man-code^'
        str2 = '$cli-code^'
        str3 = '&pme_datep='
        str4 = '&RO_theme=Развитие продаж&pme_theme=ВТ10&RO_subtheme=Развитие клиентов S и A&pme_subtheme=ВТ10А5&RO_type=Встреча с партнёром&pme_type=ВМ10&RO_territory=По всем&pme_territory=&pme_task='
        str5 = 'ОС по счету №' + list[i][1] + ' получить спецусловия и договориться о поставке.'
        str6 =  '&RO_state=Назначено&pme_state=appoint&pme_datef=&RO_comment=&pme_comment=&pme_result=&pme_anket=&creNext=false&RO_attachList=[]&dataType=jsonp&callback=jQuery18207678261347394104_1586169441800&_=1586169726209'
        str_send = str1 + str(manager[i]) + str2 + str(client[i]) + str3 + str(date) + str4 + str5 + str6
        requests.post(str_send)
    report = 'Встречи на 1 млн залил в ежедневник, на этой неделе их: '
    print(report, len(client))
        

if __name__ == "__main__":
    csv_path = "c:/Users/masyuk_as/projects/work/1mill.csv"
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        list_of_sales = row_to_list(reader)

        client = client_num(list_of_sales)
        manager = manager_num(list_of_sales)
        date = date() 
        push(client, manager, date, list_of_sales) 
    



