
# 🧠 AI Appointment Booking Agent with LangGraph, FastAPI & Streamlit

A conversational AI assistant that helps users schedule appointments through natural language interaction. It integrates:

- 🧠 LangGraph + LLMs (OpenAI or Groq)  
- 📅 Google Calendar API  
- ⚡ FastAPI backend  
- 🎛️ Streamlit frontend  

---

## 🚀 Features

✅ Natural language appointment booking  
✅ Smart time slot parsing and understanding  
✅ Real-time Google Calendar availability checks  
✅ Automated meeting confirmations  
✅ Chat-style interaction with a conversational agent  

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

```
booking-agent/
├── agent/
│   └── langgraph_agent.py
├── backend/
│   ├── calendar_utils.py
│   └── main.py
├── frontend/
│   └── app.py
├── requirements.txt
├── .gitignore
├── README.md
```

---

## 🔑 Environment Setup

Create a `.streamlit/secrets.toml` file or export these as environment variables:

```toml
OPENAI_API_KEY = "your_openai_key"    # OR
GROQ_API_KEY = "your_groq_key"
```

Ensure `credentials.json` for Google Calendar is downloaded and stored securely.

---

## 🧪 Running Locally

**Clone the repository:**

```bash
git clone https://github.com/yourusername/booking-agent.git
cd booking-agent
```

**Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the backend:**

```bash
uvicorn backend.main:app --reload
```

**Run the frontend:**

```bash
streamlit run frontend/app.py
```

---

## 🌍 Deployment

You can deploy this app using **Streamlit Cloud**.  
Set `frontend/app.py` as the entry point in your configuration.

---

## 📧 Contact

Made with ❤️ by **Abdul Bari**  
Feel free to reach out for suggestions, improvements, or collaborations!

---

Let me know if you’d like to add:
- 🔀 Support for multi-user calendars  
- 🧩 LangChain agent integration  
- 🔒 OAuth flow for secure calendar access

Always happy to help sharpen it further or brainstorm new angles!
