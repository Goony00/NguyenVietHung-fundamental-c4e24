from pymongo import MongoClient

#1 kết nối vào dtb server
uri= 'mongodb://admin:b7355608@ds127604.mlab.com:27604/c4e24-lab111'
client= MongoClient(uri)

#2 chọn dtb
db= client.get_database()

# #3 chọn collection
# post_collection =db["posts"]

acc_coll = db['acc']

# #4 tạo document
# new_doc={   
#     'title': 'hom nay troi nang',
#     'post': 'minh van o nha code',
# }

acc=[
    {
        "username": "boi1",
        "email": "boi1@gg.com",
        "phone": 233,
        "password": 'ggnoob',
        "yob": 1997
    },

    {
        "username": "boi2",
        "email": "boi2@gg.com",
        "phone": 666,
        "password": 'ggez',
        "yob": 1998
    },

    {
        "username": "boi3",
        "email": "boi3@gg.com",
        "phone": 555,
        "password": 'ggwp',
        "yob": 1999
    },
]
# #5 đưa document vào collection
# post_collection.insert_one(new_doc)

for i in acc:
    acc_coll.insert_one(i)

# for post in post_collection.find():
#     print(post)

for i in acc_coll.find():
    print(i)

#6 ngắt kết nối
client.close()












