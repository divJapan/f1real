from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

latest_data = {
    'type': '',
    'vehicle': '',
    'time_minutes': 0,
    'time_seconds': 0.0
}

@app.route('/aggiorna', methods=['POST'])
def aggiorna_dati():
    global latest_data
    data = request.json
    print(f"Ricevuto update: {data}")
    latest_data = data
    return jsonify({'status': 'ok'})

@app.route('/dati', methods=['GET'])
def get_dati():
    return jsonify(latest_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # <-- AGGIUNTA questa parte
    app.run(host='0.0.0.0', port=port)
