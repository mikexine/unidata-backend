#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import ConfigParser
import pickledb
from telegram import Bot

url = "http://zaphod.cab.unipd.it/psico/disponibilita"
soup = BeautifulSoup(urllib2.urlopen(url).read()) 


db = pickledb.load('uni.db', True)


unipdDict = db.get('unipd')
metelli = unipdDict['biblioteca']['metelli']

metelli['posti'] = soup.text.replace("\n", "")
print metelli

unipdDict['biblioteca']['metelli'] = metelli

db.set('unipd', unipdDict)
db.dump()




url = "http://zaphod.cab.unipd.it/pinali/PostiLiberiPinali.txt"
soup = BeautifulSoup(urllib2.urlopen(url).read()) 
db = pickledb.load('uni.db', True)

unipdDict = db.get('unipd')
pinali = unipdDict['biblioteca']['pinali']

pinali['posti'] = soup.text.replace("\n", "")
print pinali

unipdDict['biblioteca']['pinali'] = pinali

db.set('unipd', unipdDict)
db.dump()


url = "https://docs.google.com/spreadsheets/d/11-xeHgyl9GWc5vZ8cdLUT3MNqFBvtCkSLwUcISO8toI/pubhtml"
soup = BeautifulSoup(urllib2.urlopen(url).read()) 
data = []
table = soup.find('table', attrs={'class':'waffle'})
table_body = table.find('tbody')

print "-----------"
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

posti = data[0][1]
notebook = data[1][1]
print posti
print notebook

db = pickledb.load('uni.db', True)

unipdDict = db.get('unipd')
bibliogeo = unipdDict['biblioteca']['bibliogeo']

bibliogeo['posti'] = posti
bibliogeo['notebook'] = notebook
print bibliogeo

unipdDict['biblioteca']['bibliogeo'] = bibliogeo

db.set('unipd', unipdDict)
db.dump()


config = ConfigParser.ConfigParser()
config.read('settings.ini')
token = str(config.get('main', 'token'))
ch_id = "27002116"
starter = Bot(token=token)
txt = "posti metelli aggiornati"
starter.sendMessage(ch_id, text=txt)