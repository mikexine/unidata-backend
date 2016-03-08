#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import arrow

def createMenuDict(txt):
    start = '<p class="lead">ALTERNATIVE FISSE:</p>'
    end = '<!-- row -->'

    s1 = txt.find(start)
    s2 = txt.find(end)

    pranzo = txt[:s1]
    cena = txt[s2:]

    pranzoDict = {}
    cenaDict = {}

    for i in range(6):
        # print i
        pranzoDict[i] = {}
        giorno = '<td data-giorno="%s" data-tipo-piatto="1">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="1">' % (i+2)
        giornoIndex = pranzo.find(giorno)
        fineIndex = pranzo.find(fine)
        currentPranzo = str(pranzo[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        pranzoDict[i]['primo'] = tmp.text
        pranzoDict[i]['primo'] = pranzoDict[i]['primo'].replace('\n\n\n\n', '!')
        pranzoDict[i]['primo'] = pranzoDict[i]['primo'].replace('\n\n', '')
        pranzoDict[i]['primo'] = pranzoDict[i]['primo'].split('!')

        giorno = '<td data-giorno="%s" data-tipo-piatto="2">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="2">' % (i+2)
        giornoIndex = pranzo.find(giorno)
        fineIndex = pranzo.find(fine)
        currentPranzo = str(pranzo[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        pranzoDict[i]['secondo'] = tmp.text
        pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].replace('\n\n\n\n', '!')
        pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].replace('\n\n', '')
        pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].split('!')

        giorno = '<td data-giorno="%s" data-tipo-piatto="4">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="4">' % (i+2)
        giornoIndex = pranzo.find(giorno)
        fineIndex = pranzo.find(fine)
        currentPranzo = str(pranzo[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        pranzoDict[i]['contorno'] = tmp.text
        pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].replace('\n\n\n\n', '!')
        pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].replace('\n\n', '')
        pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].split('!')

    i = 6
    pranzoDict[i] = {}

    giorno = '<td data-giorno="7" data-tipo-piatto="1">'
    fine = '<th>Secondi Piatti</th>'
    giornoIndex = pranzo.find(giorno)
    fineIndex = pranzo.find(fine)
    currentPranzo = str(pranzo[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    pranzoDict[i]['primo'] = tmp.text
    pranzoDict[i]['primo'] = pranzoDict[i]['primo'].replace('\n\n\n\n', '!')
    pranzoDict[i]['primo'] = pranzoDict[i]['primo'].replace('\n\n', '')
    pranzoDict[i]['primo'] = pranzoDict[i]['primo'].split('!')

    giorno = '<td data-giorno="7" data-tipo-piatto="2">'
    fine = '<th>Contorni</th>'
    giornoIndex = pranzo.find(giorno)
    fineIndex = pranzo.find(fine)
    currentPranzo = str(pranzo[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    pranzoDict[i]['secondo'] = tmp.text
    pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].replace('\n\n\n\n', '!')
    pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].replace('\n\n', '')
    pranzoDict[i]['secondo'] = pranzoDict[i]['secondo'].split('!')

    giorno = '<td data-giorno="7" data-tipo-piatto="4">'
    fine = ' </div><!-- .table-responsive -->'
    giornoIndex = pranzo.find(giorno)
    fineIndex = pranzo.find(fine)
    currentPranzo = str(pranzo[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    pranzoDict[i]['contorno'] = tmp.text
    pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].replace('\n\n\n\n', '!')
    pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].replace('\n\n', '')
    pranzoDict[i]['contorno'] = pranzoDict[i]['contorno'].split('!')


    for i in range(6):
        # print i
        cenaDict[i] = {}
        giorno = '<td data-giorno="%s" data-tipo-piatto="1">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="1">' % (i+2)
        giornoIndex = cena.find(giorno)
        fineIndex = cena.find(fine)
        currentPranzo = str(cena[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        cenaDict[i]['primo'] = tmp.text
        cenaDict[i]['primo'] = cenaDict[i]['primo'].replace('\n\n\n\n', '!')
        cenaDict[i]['primo'] = cenaDict[i]['primo'].replace('\n\n', '')
        cenaDict[i]['primo'] = cenaDict[i]['primo'].split('!')

        giorno = '<td data-giorno="%s" data-tipo-piatto="2">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="2">' % (i+2)
        giornoIndex = cena.find(giorno)
        fineIndex = cena.find(fine)
        currentPranzo = str(cena[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        cenaDict[i]['secondo'] = tmp.text
        cenaDict[i]['secondo'] = cenaDict[i]['secondo'].replace('\n\n\n\n', '!')
        cenaDict[i]['secondo'] = cenaDict[i]['secondo'].replace('\n\n', '')
        cenaDict[i]['secondo'] = cenaDict[i]['secondo'].split('!')

        giorno = '<td data-giorno="%s" data-tipo-piatto="4">' % (i+1)
        fine = '<td data-giorno="%s" data-tipo-piatto="4">' % (i+2)
        giornoIndex = cena.find(giorno)
        fineIndex = cena.find(fine)
        currentPranzo = str(cena[giornoIndex:fineIndex])
        tmp = BeautifulSoup(currentPranzo, "lxml")
        cenaDict[i]['contorno'] = tmp.text
        cenaDict[i]['contorno'] = cenaDict[i]['contorno'].replace('\n\n\n\n', '!')
        cenaDict[i]['contorno'] = cenaDict[i]['contorno'].replace('\n\n', '')
        cenaDict[i]['contorno'] = cenaDict[i]['contorno'].split('!')

    i = 6
    cenaDict[i] = {}

    giorno = '<td data-giorno="7" data-tipo-piatto="1">'
    fine = '<th>Secondi Piatti</th>'
    giornoIndex = cena.find(giorno)
    fineIndex = cena.find(fine)
    currentPranzo = str(cena[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    cenaDict[i]['primo'] = tmp.text
    cenaDict[i]['primo'] = cenaDict[i]['primo'].replace('\n\n\n\n', '!')
    cenaDict[i]['primo'] = cenaDict[i]['primo'].replace('\n\n', '')
    cenaDict[i]['primo'] = cenaDict[i]['primo'].split('!')

    giorno = '<td data-giorno="7" data-tipo-piatto="2">'
    fine = '<th>Contorni</th>'
    giornoIndex = cena.find(giorno)
    fineIndex = cena.find(fine)
    currentPranzo = str(cena[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    cenaDict[i]['secondo'] = tmp.text
    cenaDict[i]['secondo'] = cenaDict[i]['secondo'].replace('\n\n\n\n', '!')
    cenaDict[i]['secondo'] = cenaDict[i]['secondo'].replace('\n\n', '')
    cenaDict[i]['secondo'] = cenaDict[i]['secondo'].split('!')

    giorno = '<td data-giorno="7" data-tipo-piatto="4">'
    fine = '<p class="lead">ALTERNATIVE FISSE:</p>'
    giornoIndex = cena.find(giorno)
    fineIndex = cena.find(fine)
    currentPranzo = str(cena[giornoIndex:fineIndex])
    tmp = BeautifulSoup(currentPranzo, "lxml")
    cenaDict[i]['contorno'] = tmp.text
    cenaDict[i]['contorno'] = cenaDict[i]['contorno'].replace('\n\n\n\n', '!')
    cenaDict[i]['contorno'] = cenaDict[i]['contorno'].replace('\n\n', '')
    cenaDict[i]['contorno'] = cenaDict[i]['contorno'].split('!')


    menu = {
        'pranzo': pranzoDict,
        'cena' : cenaDict
    }

    return menu


def cleanMenu(menuRaw):
    for a in menuRaw:
        for b in menuRaw[a]:
            for c in menuRaw[a][b]:
                del menuRaw[a][b][c][0]

    # print menuRaw
    menu = {}
    for i in range(7):
        menu[i] = {}

        menu[i]['pranzo'] = menuRaw['pranzo'][i]
        menu[i]['cena'] = menuRaw['cena'][i]


    for i in range(7):
        for j in menu[i]['pranzo']:
            for k in range(len(menu[i]['pranzo'][j])):
                menu[i]['pranzo'][j][k] = menu[i]['pranzo'][j][k].replace('\n', '')

    for i in range(7):
        for j in menu[i]['cena']:
            for k in range(len(menu[i]['cena'][j])):
                menu[i]['cena'][j][k] = menu[i]['cena'][j][k].replace('\n', '')

    return menu


def makeRequest():
    ts = arrow.utcnow().timestamp

    url = "https://esu.markas.info/ajax_tools/get_week"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"actual_week\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamp_selezionato\"\r\n\r\n"+ str(ts) + "\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tipo_menu_id\"\r\n\r\n10\r\n-----011000010111000001101001--"

    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'accept': "application/json",
        'x-requested-with': "XMLHttpRequest",
        'host': "esu.markas.info",
        'origin': "https//esu.markas.info",
        'referer': "https//esu.markas.info/menu",
        'cache-control': "no-cache",
        }

    session = requests.Session()
    response = session.post(url, data=payload, headers=headers).json()
    txt = response['visualizzazione_settimanale'].encode('ascii', 'ignore')
    return txt
