# 🧠 AI Appointment Booking Agent with LangGraph, FastAPI & Streamlit

This is a conversational AI booking assistant that helps users schedule appointments via natural language. It integrates:
- 🧠 LangGraph + LLM (OpenAI or Groq)
- 📅 Google Calendar API
- ⚡ FastAPI backend
- 🎛️ Streamlit frontend

---

## 🚀 Features
✅ Accepts natural language input  
✅ Parses and understands time slots  
✅ Checks Google Calendar for availability  
✅ Books confirmed meetings  
✅ Chat-style interaction with a smart agent  

---

## 🧱 Tech Stack
- Python 3.11+
- FastAPI
- Streamlit
- LangGraph
- Google Calendar API
- OpenAI / Groq API
- dateparser

---

## 📁 Folder Structure

booking-agent/
├── agent/
│ └── langgraph_agent.py
├── backend/
│ ├── calendar_utils.py
│ └── main.py
├── frontend/
│ └── app.py
├── requirements.txt
├── .gitignore
├── README.md

yaml
Copy
Edit

---

## 🔑 Environment Setup

Create a `.streamlit/secrets.toml` or export these in your terminal:

```toml
OPENAI_API_KEY = "your_openai_key"   # OR
GROQ_API_KEY = "your_groq_key"
Also ensure credentials.json for Google Calendar is downloaded and stored securely.

🧪 Running Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/booking-agent.git
cd booking-agent
Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run backend:

bash
Copy
Edit
uvicorn backend.main:app --reload
Run frontend:

bash
Copy
Edit
streamlit run frontend/app.py
🌍 Deployment
Deploy via Streamlit Cloud. Set frontend/app.py as the entry file.

📧 Contact
Made with ❤️ by Abdul Bari
Feel free to reach out for suggestions, improvements, or collaborations!

yaml
Copy
Edit

---

Let me know if you'd like me to tailor it further — for example, using `LangChain` agents or multi-user calendar support!







