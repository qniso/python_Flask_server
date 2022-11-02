import flask
from flask import Flask
from flask_cors import CORS

from shared.components.documents.document import generate_document
from shared.components.mongo.mongo import get_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def resp():
    return {"response": True}


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
    # data = {
    #     "response": bson.BSON(a[0]['_id'])
    # }
    for i in a:
        i['_id'] = 'null'
        b.append(i)
        print(i)

    data = {
        "response": b
    }
    return data



# app.run()