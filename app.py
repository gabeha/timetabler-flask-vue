from flask import Flask, jsonify
from flask_cors import CORS

import json
from entry_point import create_schedule

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
    f = open('optimal_schedule.json')
    data = json.load(f)
    return jsonify({
        'status': 'success',
        'schedule': data
    })

@app.route('/invoke', methods=['GET'])
def invoke_solver():
    create_schedule()
    return jsonify({
        'status': 'success'
    })


if __name__ == '__main__':
    app.run()