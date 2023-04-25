import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
from shared.components.documents.document import generate_document
from shared.components.main_page.main_page import main_page_data
from shared.components.mongo.mongo import get_data, get_user

app = Flask(__name__)
CORS(app)

@app.route('/')
def resp():
    return {"response": True}


@app.route('/login', methods=["POST"])
def auth():
    data = flask.request.get_json()
    login = data['login']
    password = data['password']

    payload = {
        "login": login,
        "password": password
    }
    data = get_user(login, jwt.encode({"password": password}, 'secret', algorithm="HS256"))

    return jsonify(data)


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
