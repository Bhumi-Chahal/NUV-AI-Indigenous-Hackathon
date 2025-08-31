#!/usr/bin/env python3
"""
Development startup script for the Hackathon Backend
This script sets up the environment and runs the Flask development server
"""

import os
import sys
import subprocess
import sqlite3

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_cors
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Requirements installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements")
            return False

def setup_database():
    """Ensure database directory exists"""
    db_dir = os.path.join(os.path.dirname(__file__), '..', 'db')
    os.makedirs(db_dir, exist_ok=True)
    print(f"✅ Database directory ready: {db_dir}")

def main():
    """Main startup function"""
    print("🚀 Starting Hackathon Backend Development Server")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Cannot start server due to missing dependencies")
        return
    
    # Setup database
    setup_database()
    
    print("\n📋 Server Configuration:")
    print("   Host: http://localhost:5000")
    print("   Database: ../db/seed_data.db (auto-created)")
    print("   Endpoints: /api/demo, /api/query, /api/ai_query, /api/health")
    
    print("\n🌐 Starting Flask development server...")
    print("   Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
