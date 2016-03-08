import pickledb

db = pickledb.load('uni.db', False)

uniList = db.getall()
info = {}
for u in uniList:
    thisUni = db.get(u)
    infoUni = []
    for key in thisUni:
        infoUni.append(key)
    info[u] = infoUni
print info
