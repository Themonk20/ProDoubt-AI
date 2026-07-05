# ProDoubt AI 🚀

ProDoubt AI is an AI-powered Chrome Extension that allows users to ask natural language questions about products directly on any e-commerce website. It extracts product information from the current webpage, processes it using a Retrieval-Augmented Generation (RAG) pipeline, and generates accurate, context-aware answers using Groq LLM.

---

## ✨ Features

- 🤖 Ask questions about any product in natural language
- 🌐 Works directly on product pages
- 📄 Extracts webpage content automatically
- 🔍 Semantic search using FAISS Vector Store
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast responses using Groq Llama 3.3 70B
- 🎨 Clean and minimal Chrome Extension UI

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension (Manifest V3)

### Backend
- FastAPI
- Python

### AI Stack
- LangChain
- Groq LLM (Llama 3.3 70B Versatile)
- HuggingFace Embeddings
- FAISS Vector Store

---

## 🏗️ Architecture

```text
Chrome Extension
        │
        ▼
Extract Webpage Text
        │
        ▼
FastAPI Backend
        │
        ▼
Create LangChain Document
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
Retrieve Top Relevant Chunks
        │
        ▼
Groq LLM
        │
        ▼
Answer Returned to Extension
```

---

## 📂 Project Structure

```
ProDoubt-AI
│
├── backend
│   ├── app.py
│   ├── rag.py
│   ├── models.py
│   ├── requirements.txt
│   └── .env
│
├── extension
│   ├── manifest.json
│   ├── content.js
│   ├── popup.html
│   ├── popup.css
│   ├── popup.js
│   └── logo.png
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Themonk20/ProDoubt-AI.git
cd ProDoubt-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

### Configure environment variables

Create a `.env` file inside the `backend` folder.

```env
GROQ_API_KEY=your_groq_api_key
```

---

### Start the backend

```bash
cd backend
python -m uvicorn app:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧩 Load the Chrome Extension

1. Open Chrome
2. Go to `chrome://extensions`
3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the `extension` folder

---

## 📸 Demo

> Add screenshots or a GIF here showing the extension answering product-related questions.

Example:

- Extension Popup
- Product Page
- AI Response

---

## 💡 Example Questions

- What is the battery life?
- Is this product waterproof?
- Does it support voice calling?
- What is included in the box?
- What is the warranty period?
- Does it support Bluetooth 5.2?

---

## 🚀 Future Improvements

- Persistent vector database
- Multi-page product understanding
- Product comparison across websites
- Chat history
- Conversation memory
- Streaming responses
- Better webpage content cleaning
- Product specification extraction
- Deployment on Render or Railway

---

## 👨‍💻 Author

**Parth Shandilya**

B.Tech, IIT Roorkee

GitHub: https://github.com/Themonk20


