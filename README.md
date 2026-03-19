## 🎨 Ultra - AI Image Generator

A lightweight FastAPI demonstration for generating AI images using the Pollinations AI API. This project features a clean web interface, a modular backend service, and local image caching.

### 🚀 Features
* FastAPI Backend: High-performance Python API.
* AI-Powered: Integration with the Pollinations AI engine.
* Local Storage: Saves generated images to static/images for quick access.
* Modern UI: Simple HTML/JS interface with loading states.
* Modular Design: Clear separation between API routes and image services.

### 📂 Project Structure
├── main.py              # FastAPI application & routing
├── .env                 # API Keys (Hidden)
├── requirements.txt     # Python dependencies
├── services/
│   └── image_services.py # Logic for fetching images
├── static/
│   └── images/          # Generated images storage
└── templates/
    └── index.html       # Frontend UI

### 🛠️ Setup Instructions

1. Clone the repository

2. Create a Virtual Environment
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the root directory and add your API key:
KEY=your_pollinations_api_key_here

5. Run the Application
uvicorn main:app --reload

The app will be available at http://127.0.0.1:8000.

### 📡 API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | / | Serves the web interface. |
| POST | /generate | Accepts prompt and model to generate an image. |

This is a demo application. Most cloud hosting providers (Render, Heroku) use ephemeral file systems, meaning images saved to static/images will be deleted when the server restarts. For production, consider using AWS S3 or Cloudinary.