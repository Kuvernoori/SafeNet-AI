📘 SafeNet

Text + Image Moderation System
Version: MVP Prototype

📌 Overview

SafeNet is an MVP prototype designed to detect cyberbullying, toxic language, and harmful content in both text and images.
The project demonstrates the core ideas of an automated moderation system:

✔ how a moderation API works
✔ how text and image analysis can be implemented
✔ how a dashboard for moderators may look
✔ how content flows through a backend + frontend system

SafeNet includes:

FastAPI backend

Text analysis module (rule-based)

Image analysis module (OCR + text detection)

Moderator Dashboard built with Streamlit

Dockerized architecture (Docker Compose)

This MVP focuses on demonstrating functionality, not fully accurate ML performance.

```
/safenet-api
    ├── main.py                 
    ├── text_analyzer.py        
    ├── ocr_analyzer.py         
    ├── requirements.txt
    └── Dockerfile

/safenet-dashboard
    ├── Dashboard_app.py        
    ├── requirements.txt
    └── Dockerfile

docker-compose.yml
README.md
```

🐳 Running via Docker

```
docker compose up --build
```

2. Access the running services:
Service	URL
Backend API (FastAPI)	http://localhost:8000
Moderation Dashboard http://localhost:8501
