from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Flask is working!"

@app.route('/api/demo')
def demo():
    return jsonify({"status": "ok", "message": "Demo endpoint working!"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/query/<query>')
def query(query):
    return jsonify({"answer": f"You asked: {query}", "source": "test"})

if __name__ == '__main__':
    print("Starting simple test Flask app...")
    app.run(debug=True, host='0.0.0.0', port=5000)
