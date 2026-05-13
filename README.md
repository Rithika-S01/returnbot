
# 🛒 ReturnBot — E-commerce Return Policy RAG Chatbot

> Ask any question about return & refund policies across Indian e-commerce platforms and get instant, cited answers powered by AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3.0-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

---

## 🎯 Problem It Solves
Finding return policies across platforms like Flipkart, Myntra, Meesho is confusing.
ReturnBot lets you ask plain English questions and get direct answers — no more reading walls of text.

---

## 💬 Example Questions
- *"Can I return a used product on Flipkart?"*
- *"What is Myntra's return window?"*
- *"How long does Amazon refund take?"*
- *"Does Nykaa accept opened cosmetics for return?"*

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| LangChain | RAG orchestration |
| ChromaDB | Vector database |
| Sentence Transformers | Text embeddings |
| Ollama (TinyLlama) | Local LLM (free) |
| Streamlit | Web UI |

---

## 📁 Project Structure
returnbot/
├── data/
│   └── raw_policies/       # Policy text files
├── ingest/
│   └── embedder.py         # Embeds policies into ChromaDB
├── rag/
│   └── chain.py            # RAG chain setup
├── app/
│   └── streamlit_app.py    # Streamlit UI
└── requirements.txt

---

## 🚀 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Rithika-S01/returnbot.git
cd returnbot
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install packages**
```bash
pip install -r requirements.txt
```

**4. Install Ollama and pull model**
- Download Ollama from https://ollama.com/download
```bash
ollama pull tinyllama
```

**5. Embed documents**
```bash
python ingest/embedder.py
```

**6. Run the app**
```bash
streamlit run app/streamlit_app.py
```

---

## 👩‍💻 Built By
Rithika — Fresher passionate about AI/ML and RAG systems.
=======
# returnbot
A RAG-based chatbot that answers questions about e-commerce return &amp; refund policies from Flipkart, Amazon, Myntra, Meesho and Nykaa using LangChain, ChromaDB and Ollama.

