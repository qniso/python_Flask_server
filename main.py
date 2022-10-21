import flask
from flask import Flask

from shared.components.documents.document import generate_document

app = Flask(__name__)


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


# app.run()