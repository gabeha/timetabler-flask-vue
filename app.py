from flask import Flask, jsonify
from flask_cors import CORS

import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# retrive schedule
@app.route('/schedule', methods=['GET'])
def schedule():
    f = open('schedules.json')
    data = json.load(f)
    return jsonify({
        'status': 'success',
        'schedule': data
    })


if __name__ == '__main__':
    app.run()