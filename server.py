from flask import Flask, request, jsonify

app = Flask(__name__)

last_clicked_coords = {
    'latitude': 0,
    'longitude': 0
}

@app.route('/save_coords', methods=['POST'])
def save_coords():
    print("save_coords on the server called!")
    data = request.json
    last_clicked_coords['latitude'] = data['latitude']
    last_clicked_coords['longitude'] = data['longitude']
    return jsonify({'message': 'Coordinates saved successfully'})

@app.route('/get_coords', methods=['GET'])
def get_coords():
    print("get_coords on the server called!")
    print(last_clicked_coords)
    return jsonify(last_clicked_coords)

# Adding CORS headers for allowing browser to process requests from another domain
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(debug=True)
