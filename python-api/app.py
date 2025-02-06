# python-api/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    # Aquí puedes extender la lógica de procesamiento
    response = {
        "status": "success",
        "data_received": data,
        "message": "Procesado correctamente"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
