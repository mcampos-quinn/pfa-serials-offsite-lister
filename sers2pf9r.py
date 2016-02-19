import csv

milISSN = []
mil245a = []
mill130 = []
shelf245a = []
shelf130 = []
shelfISSN = []
null = ""
shelfDict = {}
milDict = {}

list022 = []
list130 = []
list245 = []

with open("SerItemsW130and245a.csv", "rb") as s, open("workList.csv", "rb") as w:
    milReader = csv.reader(s)
    shelfReader = csv.reader(w)

    for bit in shelfReader:
        shelfItems = bit
        shelfTuple = tuple(shelfItems[1:4])
        shelfDict[shelfItems[0]] = shelfTuple
        shelfISSN.append(bit[1])
        shelf130.append(bit[2])
        shelf245a.append(bit[3])

    for bop in milReader:
        milItems = bop
        milTuple = tuple(milItems[1:6])
        milDict[milItems[0]] = milTuple
        milISSN.append(bop[2])
        mil245a.append(bop[4])
        mill130.append(bop[5])

sISSN = set(shelfISSN)
mISSN = set(milISSN)
s245 = set(shelf245a)
s130 = set(shelf130)

m022 = [key for key, value in milDict.iteritems() if (value[1] is not null) and (value[1] in sISSN)]
for item in m022:
    list022.append(item+"|"+("|".join(milDict[item])))

m130 = [key for key, value in milDict.iteritems() if ((value[4] is not null) and (value[4] in s130))]
for item in m130:
    list130.append(item+"|"+("|".join(milDict[item])))

m245 = [key for key, value in milDict.iteritems() if value[3] in s245]
for item in m245:
    list245.append(item+"|"+("|".join(milDict[item])))

output = list022 + list130 + list245

with open("output.txt", "wb") as txt, open("output.csv", "wb") as out:
    for x in output:
        txt.write(x+"\n")
        writer = csv.writer(out)
        writer.writerow(x.split("|"))

with open("output.csv", "rb") as oot, open("cleanOut.csv", "wb") as clean:
    cleaner = set()
    for row in oot:
        if row in cleaner: continue
        cleaner.add(row)
        clean.write(row)

print m022
# print len(m245)
# print len(m130)
# print(output)
print(cleaner)