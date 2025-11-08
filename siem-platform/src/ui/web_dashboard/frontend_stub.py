from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    # Stub data for the dashboard
    data = {
        "title": "SIEM Dashboard",
        "description": "This is a stub for the SIEM dashboard.",
        "metrics": {
            "total_logs": 1000,
            "alerts": 5,
            "active_incidents": 2
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)