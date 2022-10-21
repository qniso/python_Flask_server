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


