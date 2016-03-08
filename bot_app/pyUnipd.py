# -*- coding: utf-8 -*-
import pickledb

# connect to DB


class pyUnipd:

    def __init__(self):
        pass

    def allUni(self):
        db = pickledb.load('uni.db', False)
        uniList = db.getall()
        info = {}
        for u in uniList:
            thisUni = db.get(u)
            infoUni = []
            for key in thisUni:
                infoUni.append(key)
            info[u] = infoUni
        return info

    def oneUni(self, uniID):
        db = pickledb.load('uni.db', False)
        thisUni = db.get(uniID)
        infoUni = []
        for key in thisUni:
            infoUni.append(key)
        return {"data": infoUni}

    def mensa(self, uniID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['mensa']
        except:
            return {'error': 'wrong id'}

    def singleMensa(self, uniID, mensaID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['mensa'][mensaID]
        except:
            return {'error': 'wrong id'}

    def aulastudio(self, uniID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['aulastudio']
        except:
            return {'error': 'wrong id'}

    def singleAula(self, uniID, aulaID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['aulastudio'][aulaID]
        except:
            return {'error': 'wrong id'}

    def biblioteca(self, uniID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['biblioteca']
        except:
            return {'error': 'wrong id'}

    def singleBiblio(self, uniID, biblioID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['biblioteca'][biblioID]
        except:
            return {'error': 'wrong id'}

    def udupadova(self, uniID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['udupadova']
        except:
            return {'error': 'wrong id'}

    def dirittostudio(self, uniID):
        db = pickledb.load('uni.db', False)
        try:
            return db.get(uniID)['dirittostudio']
        except:
            return {'error': 'wrong id'}
