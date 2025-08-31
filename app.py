from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/demo', methods=['GET'])
def demo():
    return jsonify({"status": "ok"})

@app.route('/api/query/<user_query>', methods=['GET'])
def query(user_query):
    conn = sqlite3.connect("db/faq.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", (f"%{user_query}%",))
    result = cursor.fetchone()
    conn.close()
    if result:
        return jsonify({"answer": result[0]})
    return jsonify({"answer": "Sorry, I don't know that yet."})

if __name__ == '__main__':
    app.run(debug=True)
