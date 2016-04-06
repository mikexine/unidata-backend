#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vrMensa import createMenuDict, cleanMenu, makeRequest
import datetime
import pickledb
import arrow

txt = makeRequest()

menuRaw = createMenuDict(txt)

menu = cleanMenu(menuRaw)

today = menu[datetime.datetime.today().weekday()]
print today
db = pickledb.load('uni.db', False)

univr = db.get('univr')
univr['mensa']['sanfrancesco']['menu'] = today
univr['mensa']['legrazie']['menu'] = today
univr['mensa']['last_update'] = arrow.now('CET').format('HH:mm - DD-MM-YYYY')

db.set('univr', univr)
db.dump()
