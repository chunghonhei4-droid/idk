from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

dictionary = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/addword', methods=['POST'])
def handle_json_data():
    data = request.get_json()
    if data and 'word' in data:
        word = data['word'].lower()
        dictionary[word] = {
            'definition': data.get('definition', ''),
            'category': data.get('category', 'General'),
            'example': data.get('example', '')
        }
        return jsonify({'success': True, 'message': f'Word "{word}" added successfully'})
    return jsonify({'success': False, 'message': 'Invalid data'}), 400

@app.route('/words')
def getwords():
    return jsonify(dictionary)