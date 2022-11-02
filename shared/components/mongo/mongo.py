import datetime
import pymongo

import certifi
from bson.binary import Binary

ca = certifi.where()

myclient = pymongo.MongoClient(
    "mongodb+srv://Admin_qniso:BUOorKChVrdWTWVu@telegrambot.n1ebp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca
)


def send_doc(file, date, name):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['HOLIDAY_DOCS']  # PYTHON_TEST
    i = ''
    with open(f'{file}', 'rb') as f:
        encoded = Binary(f.read())

    collection.insert_one({"Operation" : f'Заява на выідпустку {name} {date}', "filename": file, "file": encoded, "description": f'Звява від {date}'})



def get_plan_data():
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['WORKING_PLAN']  # PYTHON_TEST

    cur = collection.find()
    data = []
    res = list(cur)

    for i in res:
        i['_id'] = 'null'
        data.append(i)
        print(i)
    return data

def get_data():
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['PYTHON_TEST']  # PYTHON_TEST

    cur = collection.find()
    res = list(cur)


    # print(res)
    return res


