#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vrMensa import createMenuDict, cleanMenu, makeRequest
import datetime

txt = makeRequest()

menuRaw = createMenuDict(txt)

menu = cleanMenu(menuRaw)

print menu[datetime.datetime.today().weekday()]
