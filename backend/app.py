from flask import Flask, jsonify, request
import sqlite3
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Database configuration
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db', 'seed_data.db')

def init_db():
    """Initialize the database if it doesn't exist"""
    if not os.path.exists(DB_PATH):
        # Create the db directory if it doesn't exist
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        
        # Create a simple table structure
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Create FAQ table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS faq (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                category TEXT
            )
        ''')
        
        # Insert sample data
        sample_data = [
            ("What is AI?", "Artificial Intelligence (AI) is technology that enables computers to perform tasks that typically require human intelligence.", "Technology"),
            ("How does machine learning work?", "Machine learning uses algorithms to identify patterns in data and make predictions or decisions without explicit programming.", "Technology"),
            ("What is the hackathon about?", "This hackathon focuses on building innovative solutions using AI and modern web technologies.", "Event"),
            ("How do I get started with coding?", "Start with basic programming concepts, choose a beginner-friendly language like Python, and practice with small projects.", "Education"),
            ("What is Flask?", "Flask is a lightweight web framework for Python that makes it easy to build web applications.", "Technology")
        ]
        
        cursor.executemany('INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)', sample_data)
        conn.commit()
        conn.close()
        print(f"Database initialized at {DB_PATH}")

@app.route('/api/demo', methods=['GET'])
def demo():
    """Demo endpoint to test if backend is running"""
    return jsonify({"status": "ok", "message": "Backend is running successfully!"})

@app.route('/api/query/<user_query>', methods=['GET'])
def query(user_query):
    """Query the SQLite database for answers"""
    try:
        # Initialize DB if it doesn't exist
        init_db()
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Search for questions that contain the user query (case-insensitive)
        cursor.execute("""
            SELECT answer, category 
            FROM faq 
            WHERE LOWER(question) LIKE LOWER(?) 
            OR LOWER(answer) LIKE LOWER(?)
        """, (f"%{user_query}%", f"%{user_query}%"))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return jsonify({
                "answer": result[0],
                "category": result[1],
                "source": "database"
            })
        else:
            return jsonify({
                "answer": "Sorry, I don't know that yet.",
                "source": "fallback"
            })
            
    except Exception as e:
        return jsonify({
            "error": "Database error occurred",
            "message": str(e)
        }), 500

@app.route('/api/ai_query/<user_query>', methods=['GET'])
def ai_query(user_query):
    """Placeholder for AI integration - will be replaced with actual API calls later"""
    return jsonify({
        "answer": "AI integration placeholder - This will be connected to OpenAI/Gemini API later!",
        "query": user_query,
        "source": "ai_placeholder"
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment monitoring"""
    return jsonify({
        "status": "healthy",
        "database": "connected" if os.path.exists(DB_PATH) else "not_found"
    })

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    print("Starting Flask backend...")
    print(f"Database path: {DB_PATH}")
    app.run(debug=True, host='0.0.0.0', port=5000)
