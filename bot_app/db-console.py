# -*- coding: utf-8 -*-
import pickledb
import json
db = pickledb.load('uni.db', False)

universities = db.getall()

print "opzioni disponibili: "

for uni in universities:
    print uni
    unidata = db.get(uni)
    for data in unidata:
        print "|- " + data
        for d in unidata[data]:
            print "   |- " + d

#print db.get('unipd')


uni = raw_input("uni da modificare: ")
cat = raw_input("categoria da modificare: ")
campo = raw_input("campo da modificare: ")

unidata = db.get(uni)
current_dict = unidata[cat][campo]

#print(json.dumps(current_dict, indent=2))
print current_dict
new = raw_input("nuovo valore: ")

unidata[cat][campo] = json.loads(new)

db.set(uni, unidata)

print db.get(uni)[cat][campo]
db.dump()

print "--"
print uni
print cat
print campo