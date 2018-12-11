from pymongo import MongoClient

uri= 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client=MongoClient(uri)
db=client.get_database()
post_coll = db['posts']
add={
    'title':'Không làm gì',
    'author': 'V.Hùng',
    'content': 'Ôi mấy năm nay tôi vui chơi nhiều. Ôi mấy năm nay xung quanh toàn tình yêu. Ôi mấy năm nay gặp may gặp may. Tôi thấy như tôi thật hay thật hay',
}

post_coll.insert_one(add)
client.close