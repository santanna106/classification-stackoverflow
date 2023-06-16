from flask import Flask,jsonify,request
from joblib import load

app = flask(__file__)

@app.route("/")

def index():
    if 'query' not in request.args:
        return jsonify({"prediction":None,"message":"sendme a text"})

    query = request.args.get("query")
    model = load("model.joblib")
    labels = ['Linguagens e Frameworks','Plataformas','Ferramentas']

    predict - model.predict([query])
    prediction = labels[predict[0]]

    return jsonify({"prediction":prediction})