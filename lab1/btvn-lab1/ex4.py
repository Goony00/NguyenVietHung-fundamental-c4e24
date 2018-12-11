from matplotlib import pyplot
from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)

db = client.get_database()

cus_coll= db['customers']

events = 0
ads = 0
wom = 0

for counts in cus_coll.find():
    if counts['ref'] == 'events':
        events += 1
    if counts['ref'] == 'ads':
        ads += 1
    if counts['ref'] == 'wom':
        wom += 1

print('Group event:', events)
print('Group ad: ', ads)
print('Group word of mouth: ', wom)

count = [events, ads, wom]
name = ['Events', 'Advs', 'WOM']

pyplot.pie(count,labels=name,autopct= '%0.1f%%',shadow = True,explode = [0,0.01,0.03])
pyplot.axis('equal')
pyplot.show()
client.close()
