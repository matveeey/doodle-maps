from flask import Flask, request, jsonify

app = Flask(__name__)

last_clicked_coords = {
    'latitude': 0,
    'longitude': 0
}

@app.route('/save_coords', methods=['POST'])
def save_coords():
    data = request.json
    last_clicked_coords['latitude'] = data['latitude']
    last_clicked_coords['longitude'] = data['longitude']
    return jsonify({'message': 'Coordinates saved successfully'})

@app.route('/get_coords', methods=['GET'])
def get_coords():
    return jsonify(last_clicked_coords)

if __name__ == '__main__':
    app.run(debug=True)
