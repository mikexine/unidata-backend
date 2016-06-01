#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import requests
import json
import arrow
import ConfigParser
import pickledb
from telegram import Bot


db = pickledb.load('uni.db', True)



mensaList = ['sanfrancesco', 'piovego', 'agripolis', 'acli',
             'belzoni', 'forcellini', 'murialdo']
rep = '<span style="visibility:hidden">:</span>'
nomenu = 'Menu non pubblicato su www.esupd.gov.it/'
errmenu = ['Niente menu, errore su www.esupd.gov.it/']


def getcal():
    soup = BeautifulSoup(urllib2.urlopen("http://www.esupd.gov.it/it").read())
    listFull = []
    listPart = []
    listCal = []
    p = 0
    for i in soup.find_all("td"):
        listFull.append(str(i))
    for x in range(7):
        listPart.append(listFull[p])
        listPart.append(listFull[p + 1])
        p += 4
    for x in range(len(listPart)):
        if 'open' in listPart[x]:
            listCal.append(1)
        else:
            listCal.append(0)
    return listCal


def getmenu(mid):
    mensaid = '0' + str(mid)
    completo = {"primo": [], "secondo": [], "contorno": [], "dessert": []}
    try:
        url = "http://www.esupd.gov.it/it/Pagine/Menu.aspx?idmenu=ME_"
        soup = BeautifulSoup(urllib2.urlopen(url + mensaid).read())
        menu = []
        for i in soup.find_all("h2"):
            portata = i.text.split()[0].lower()
            for j in i.next_siblings:
                if j.name == "h2":
                    break
                if j.name == "ul":
                    a = str(j)
                    menu += (a.split("<li>"))
                    for piatto in range(len(menu)):
                        if "h3" in menu[piatto]:
                            menu[piatto] = menu[piatto].replace(rep, ' ')
                            txt = menu[piatto][4:].split("<")[0]
                            completo[portata].append(txt.replace('*',''))
                menu = []
        for key in completo:
            if completo[key] == []:
                completo[key] = [nomenu]
    except:
        for key in completo:
            completo[key] = errmenu
    return completo


unipdDict = db.get('unipd')
mensaDict = unipdDict['mensa']

try:
    cal = getcal()
except:
    cal = None
a = 0

if cal is not None:
    for x in range(7):
        mensaDict[mensaList[x]]['calendario']['pranzo'] = cal[a]
        mensaDict[mensaList[x]]['calendario']['cena'] = cal[a + 1]
        a += 2
else:
    for x in range(7):
        mensaDict[mensaList[x]]['calendario']['pranzo'] = "errore su www.esupd.gov.it/"
        mensaDict[mensaList[x]]['calendario']['cena'] = "errore su www.esupd.gov.it/"
        a += 2

for x in range(7):
    mensaDict[mensaList[x]]['menu'] = getmenu(x + 1)
    print x


mensaDict['last_update'] = arrow.now('CET').format('HH:mm - DD-MM-YYYY')

unipdDict['mensa'] = mensaDict

db.set('unipd', unipdDict)
db.dump()


config = ConfigParser.ConfigParser()
config.read('settings.ini')
token = str(config.get('main', 'token'))
ch_id = "27002116"
starter = Bot(token=token)
txt = "bot_app unipd database updated"
starter.sendMessage(ch_id, text=txt)


# data[1]['mensa'] = mensaDict
# r = requests.put("http://unipd.xyz/mensa/" + mensaID,
#                  data=json.dumps(data[1]), headers=headers, timeout=30)


# updateID = data[0]['id']
# now = arrow.now('CET').format('HH:mm - DD-MM-YYYY')
# data[0]['mensa']['last_update'] = now
# r = requests.put("http://unipd.xyz/mensa/" + updateID,
#                  data=json.dumps(data[0]), headers=headers, timeout=30)