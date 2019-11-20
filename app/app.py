# app/app.py
from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np


# Initialize the app and set a secret_key.
app = Flask(__name__)
app.secret_key = 'something_secret'

# Load the pickled model.
# MODEL = pickle.load(open('model.pkl', 'rb'))

@app.route('/api', methods=['GET'])
def api():
    """Handle request and output model score in json format."""
    # Handle empty requests.
    if not request.json:
        return jsonify({'error': 'no request received'})
    # Parse request args into feature array for prediction.
    x_list, missing_data = parse_args(request.json)
    print(x_list, missing_data)
    x_array = np.array([x_list])
    # Predict on x_array and return JSON response.
    # estimate = int(MODEL.predict(x_array)[0])
    # response = dict(ESTIMATE=estimate, MISSING_DATA=missing_data)
    response =''
    return jsonify(response)


FEATURES = ['AGE']
def parse_args(request_dict):
    """Parse model features from incoming requests formatted in    
    JSON."""
    # Initialize missing_data as False.
    missing_data = False
# Parse out the features from the request_dict.
    x_list = []
    for feature in FEATURES:
        value = request_dict.get(feature, None)
        print(value)
        if value:
            x_list.append(value)
        else:
            # Handle missing features.
            x_list.append(0)
            missing_data = True
    return x_list, missing_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)