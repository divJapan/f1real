from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🏎️ F1 Live Server attivo!"

@app.route('/aggiorna', methods=['POST'])
def aggiorna():
    data = request.json

    if not data or 'type' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    event_type = data['type']

    if event_type == 'track_update':
        print(f"\n📢 TRACK UPDATE: {data['track']}")

    elif event_type == 'fastest_lap':
        mins = data.get('time_minutes', 0)
        secs = data.get('time_seconds', 0)
        print(f"\n🏎️ FASTEST LAP: {data['vehicle']} ha fatto {mins}:{secs:.3f} s su {data['track']}")

    elif event_type == 'race_winner':
        print(f"\n🏆🏁 VINCITORE DELLA GARA: {data['vehicle']} su {data['track']}")

    # TEMPLATE per eventuali futuri eventi (esempio):
    elif event_type == 'safety_car':
        print(f"\n🚨 SAFETY CAR STATUS: {data.get('status', 'unknown')} su {data['track']}")

    else:
        print(f"\n[DEBUG] Ricevuto evento sconosciuto: {event_type} | Payload: {data}")

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
