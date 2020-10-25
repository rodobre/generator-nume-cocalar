from flask import Flask, render_template, jsonify
from secrets import randbelow
import json

app = Flask(__name__, template_folder='templates/')
json_name_file = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_name', methods=['GET'])
def get_name():
    global json_name_file

    first_name = json_name_file['first_name']
    middle_name = json_name_file['middle_name']
    third_name = json_name_file['third_name']

    a, b, c = first_name[randbelow(len(first_name))], middle_name[randbelow(len(middle_name))], \
                 third_name[randbelow(len(third_name))]

    return jsonify({'first_name': a, 'middle_name': b, 'third_name': c})

if __name__ == '__main__':
    with open('names.json', 'r') as json_file:
        json_name_file = json.loads(json_file.read())
    app.run(host='0.0.0.0', port=7979)