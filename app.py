print("🚀 Starting Flask server...")



from flask import Flask, request, jsonify, render_template
from database import insert_event, get_all_events
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    events = get_all_events()
    return render_template('index.html', events=events)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    payload = {}

    if event_type == 'push':
        payload = {
            'type': 'push',
            'author': data['pusher']['name'],
            'to_branch': data['ref'].split('/')[-1],
            'timestamp': datetime.utcnow().isoformat()
        }

    elif event_type == 'pull_request':
        payload = {
            'type': 'pull_request',
            'author': data['pull_request']['user']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': data['pull_request']['created_at']
        }

    if payload:
        insert_event(payload)
        return jsonify({"status": "received"}), 200
    return jsonify({"status": "ignored"}), 200

@app.route('/api/events')
def api_events():
    return jsonify(get_all_events())

if __name__ == '__main__':
    app.run(debug=True)