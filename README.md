# 🤖 AI Email Agent

An intelligent Email Agent built using:

- FastAPI (Backend API)
- Streamlit (Frontend UI)
- LangGraph (Agent workflow)
- OpenAI / Groq LLM
- Gmail API with OAuth2

---

## 🚀 Features

- 📩 Reads latest email from Gmail
- 🧠 Classifies email (Spam / Complaint / General)
- ✍️ Generates smart reply using LLM
- 👀 Allows user to edit before sending
- 📤 Sends email automatically via Gmail API

---

## 🏗️ Architecture

Frontend (Streamlit)  
⬇  
FastAPI Backend  
⬇  
LangGraph Agent  
⬇  
LLM (Groq/OpenAI)  
⬇  
Gmail API  

---

## 🔐 Setup Instructions

1. Clone the repository:
```
git clone https://github.com/U1503/ai-email-agent.git
```

2. Create virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Add:
- `.env` file with API key
- `backend/credentials.json` (Google OAuth)

5. Run backend:
```
uvicorn backend.main:app --reload
```

6. Run frontend:
```
cd frontend
streamlit run app.py
```

---

## 📸 Screenshots

(Add your screenshots here)

---

## 📌 Author

Udit Narayan Sah  
B.Tech IT | AI Developer
