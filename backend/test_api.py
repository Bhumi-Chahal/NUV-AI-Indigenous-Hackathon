#!/usr/bin/env python3
"""
Simple test script to verify the Flask API endpoints
Run this after starting the Flask server
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, description):
    """Test a single endpoint and print results"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        print(f"✅ {description}")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
        print()
        return True
    except Exception as e:
        print(f"❌ {description}")
        print(f"   Error: {str(e)}")
        print()
        return False

def main():
    """Test all API endpoints"""
    print("🧪 Testing Hackathon Backend API")
    print("=" * 40)
    
    # Test all endpoints
    tests = [
        ("/api/demo", "Demo endpoint"),
        ("/api/health", "Health check"),
        ("/api/query/What%20is%20AI", "Query endpoint - AI question"),
        ("/api/query/random%20question", "Query endpoint - unknown question"),
        ("/api/ai_query/Hello%20world", "AI query placeholder")
    ]
    
    passed = 0
    total = len(tests)
    
    for endpoint, description in tests:
        if test_endpoint(endpoint, description):
            passed += 1
    
    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Backend is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the Flask server and try again.")

if __name__ == "__main__":
    main()
