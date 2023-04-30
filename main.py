import json

import flask
import jwt
from flask import Flask, jsonify
from flask_cors import CORS

from shared.components.documents.document import generate_document
from shared.components.main_page.main_page import main_page_data
from shared.components.mongo.mongo import get_data, auth,get_car_numbers, get_car_fuel_data

app = Flask(__name__)
CORS(app)
key = 'secret'


@app.route('/')
def resp():
    return {"response": True}


@app.route('/login', methods=['POST'])
def login():
    data = flask.request.get_json()
    login = data['login']
    password = data['password']

    auth(login, password)

    print(login, password)
    encode = jwt.encode({"pass": password}, key, algorithm="HS256")

    return {
        "access_tokken": encode,
        "refresh_token": '123',
        "error": {
            "code": 0,
            "description": None
        },
        "expDate": '12.12.2020'
    }


@app.route('/document_gen', methods=['GET'])
def test_documents():
    date_start = flask.request.args['date_start']
    date_end = flask.request.args['date_end']
    full_name = flask.request.args['full_name']
    generate_document(date_start, date_end, full_name)

    return {"response": {"date_start": date_start, "date_end": date_end, "full_name": full_name}}

@app.route('/test', methods=['GET'])
def test_request():
    a = get_data()
    b = []
    for i in a:
        i['_id'] = 'null'
        b.append(i)
        print(i)
    data = {
        "response": b
    }
    return data


@app.route('/api/mainPageCardData', methods=["GET"])
def cardData():
    data = main_page_data()
    return {"response": data}

@app.route('/getCarFuel', methods=['GET'])
def carFuel():
    car_numbers = get_car_numbers()
    car_fuel = get_car_fuel_data()

    data = {
            "car_info_list": car_fuel,
            "car_numbers": car_numbers
        }


    return data

