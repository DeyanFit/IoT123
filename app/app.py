from flask import Flask, request, jsonify
from pysondb import db

app = Flask(__name__)

db_pool = db.getDb("my_database.json")

@app.route('/', methods=['GET'])
def get_home():
    return "Welcome to the Home Page"

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json
    if data:
        db_pool.add(data)
        db_pool.dump()
        return "Data added to the database"
    else:
        return "Invalid data format", 400

@app.route('/get_data', methods=['GET'])
def get_data():
    data = db_pool.all()
    return jsonify(data)

@app.route('/get_device_data/<device_id>', methods=['GET'])
def get_device_data(device_id):
    data = db_pool.where({"device_id": device_id})
    if data:
        return jsonify(data)
    else:
        return "No data found for the specified device", 404

@app.route('/graph/<thermometer_id>', methods=['GET'])
def get_graph(thermometer_id):
    data = db_pool.where({"device_id": thermometer_id})

    if data:
        values = [entry['value'] for entry in data]
        avg_temp = sum(values) / len(values)
        max_temp = max(values)
        min_temp = min(values)

        graph_data = {
            "data": values,
            "statistics": {
                "average": avg_temp,
                "max": max_temp,
                "min": min_temp
            }
        }

        return jsonify(graph_data)
    else:
        return "No data found for the specified device", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
