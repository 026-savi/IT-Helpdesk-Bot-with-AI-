# 🚀 AI-Powered IT Helpdesk Bot

An intelligent IT Helpdesk Support System built using FastAPI, Python, SQLite, and AI integration.  
The system automates IT support responses, ticket generation, priority detection, and issue management.

---

## ✨ Features

- 🤖 AI-powered IT support assistant
- 🎫 Automatic ticket generation
- 📊 Ticket dashboard & analytics
- ⚡ Priority detection system
- 🔍 RAG-based support responses
- 🗄️ SQLite database integration
- 🌐 FastAPI backend APIs
- 💻 Modern frontend UI

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### AI / ML
- Groq API
- LLM Integration
- RAG (Retrieval-Augmented Generation)

---

## 📂 Project Structure

```bash
backend/
frontend/
rag_db/
vector_db/
requirements.txt
README.md
```

---

## ▶️ Run Backend

### 1️⃣ Open terminal

```bash
cd D:\it-helpdesk-bot
```

### 2️⃣ Activate virtual environment

```bash
venv\Scripts\activate
```

### 3️⃣ Start backend server

```bash
uvicorn backend.main:app --reload --port 8001
```

Backend will run on:

```bash
http://127.0.0.1:8001
```

---

## ▶️ Run Frontend

Open another terminal:

```bash
cd D:\it-helpdesk-bot
```

Run:

```bash
python -m http.server 5500
```

Frontend will run on:

```bash
http://127.0.0.1:5500/index.html
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat` | AI Chat Support |
| GET | `/tickets` | Get All Tickets |
| GET | `/stats` | Dashboard Stats |
| PATCH | `/tickets/{id}` | Update Ticket |

---

## 👨‍💻 Developed By

### Savi Sethi

---

## 📜 License

This project is for educational and learning purposes.
