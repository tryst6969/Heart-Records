from flask import Flask, jsonify, request
app = Flask(__name__)

info = [
    {
        "heart_id": 1011,
        "heart_date":"21/09/22",
        "heart_rate": "81"
    },
    {
        "heart_id": 2022,
        "heart_date":"21/09/22",
        "heart_rate": "72"
    }
    
]

@app.route('/info', methods=['GET'])
def getHeartData():
    return jsonify(info)

@app.route('/info/<int:heart_id>', methods=['GET'])
def getHeartInfo(heart_id):
    info = [ info for info in info if info['heart_id'] == heart_id]
    return jsonify({"info":info})

@app.route('/info', methods=['POST'])
def addHeartData():
    data = request.get_json()
    info.append(data)
    return {'heart_id': len(info)},200

if __name__ == '__main__':
    app.run()