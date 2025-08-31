# Hackathon Backend - Flask API

This is the backend API for the hackathon project, built with Flask and SQLite.

## Features

- ✅ **Demo Endpoint**: `/api/demo` - Returns status confirmation
- ✅ **Query Endpoint**: `/api/query/<user_query>` - Searches SQLite database for answers
- ✅ **AI Placeholder**: `/api/ai_query/<user_query>` - Ready for OpenAI/Gemini integration
- ✅ **Health Check**: `/api/health` - Database connection status
- ✅ **CORS Enabled**: Frontend integration ready
- ✅ **Auto Database Initialization**: Creates DB and sample data on first run

## Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python app.py
```

The server will start at `http://localhost:5000`

### 3. Test Endpoints
```bash
# Test demo endpoint
curl http://localhost:5000/api/demo

# Test query endpoint
curl http://localhost:5000/api/query/What%20is%20AI

# Test AI placeholder
curl http://localhost:5000/api/ai_query/Hello

# Health check
curl http://localhost:5000/api/health
```

## API Endpoints

### GET `/api/demo`
Returns backend status confirmation.
```json
{
  "status": "ok",
  "message": "Backend is running successfully!"
}
```

### GET `/api/query/<user_query>`
Searches the SQLite database for answers.
```json
{
  "answer": "Artificial Intelligence (AI) is technology...",
  "category": "Technology",
  "source": "database"
}
```

### GET `/api/ai_query/<user_query>`
AI integration placeholder (ready for OpenAI/Gemini).
```json
{
  "answer": "AI integration placeholder - This will be connected to OpenAI/Gemini API later!",
  "query": "Hello",
  "source": "ai_placeholder"
}
```

### GET `/api/health`
Database connection status.
```json
{
  "status": "healthy",
  "database": "connected"
}
```

## Database

- **File**: `../db/seed_data.db` (auto-created)
- **Schema**: FAQ table with question, answer, and category
- **Sample Data**: 10 pre-loaded Q&A pairs
- **Auto-initialization**: Database and sample data created on first run

## Deployment

### Render (Recommended)
1. Connect your GitHub repo to Render
2. Create new Web Service
3. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Python Version**: 3.9.16

### Railway
1. Connect your GitHub repo to Railway
2. Deploy automatically
3. Railway will detect Python and install dependencies

### Local Production
```bash
gunicorn app:app --bind 0.0.0.0:8000 --workers 4
```

## Project Structure
```
backend/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── render.yaml        # Render deployment config
└── README.md          # This file

db/
├── seed_data.sql      # Database schema and sample data
└── seed_data.db       # SQLite database (auto-created)
```

## Next Steps for AI Integration

1. **Add API Keys**: Create environment variables for OpenAI/Gemini
2. **Install AI SDKs**: Add `openai` or `google-generativeai` to requirements.txt
3. **Update AI Route**: Replace placeholder in `/api/ai_query` with actual API calls
4. **Error Handling**: Add rate limiting and error handling for AI APIs

## Troubleshooting

### Database Issues
- Check if `db/` directory exists
- Ensure write permissions in the project directory
- Database auto-creates on first run

### Port Issues
- Change port in `app.py` if 5000 is occupied
- Use `--port` flag with gunicorn

### CORS Issues
- CORS is enabled for all origins in development
- Configure specific origins for production

## Team Notes

- **Backend Developer**: Jiya
- **Frontend Team**: Kashish + Kevna
- **API Base URL**: Share with frontend team after deployment
- **Database**: SQLite with sample Q&A data ready
