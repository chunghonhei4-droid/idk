from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

dictionary = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/addword', methods=['POST'])
def handle_json_data():
    data = request.get_json()
    dictionary[word] = data

@app.route('/words')
def getwords():
    return jsonify(dictionary)