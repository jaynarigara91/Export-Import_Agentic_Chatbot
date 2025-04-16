# DAHFOOD Export-Import Customer Service Chatbot 🤖🌍

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama4-9cf)](https://groq.com/)
[![RAG](https://img.shields.io/badge/Architecture-RAG-yellow)](https://python.langchain.com/)

**An AI-powered chatbot** designed to revolutionize customer support for DAHFOOD, a global export-import company. Built with LangGraph, RAG architecture, and real-time NLP to streamline logistics inquiries and enhance user experience.

https://github.com/user-attachments/assets/eb7231e0-9c1c-458a-a9ff-bd5add9ece69

---

## 🚨 Problem Statement
DAHFOOD’s customers faced **delays in resolving critical export-import queries** such as:
- Categories inqueries
- Logistics pricing and compliance FAQs
- Time-zone barriers for 24/7 support
- Repetitive manual responses from human agents

Traditional chatbots lacked **context-aware responses** and couldn’t scale with DAHFOOD’s growing global operations.

---

## 🛠️ Solution
This **AI-driven chatbot** solves these challenges by:
- Providing **instant, accurate responses** using DAHFOOD’s website data and RAG (Retrieval-Augmented Generation)
- Maintaining **multi-turn conversation context** with LangGraph
- Storing chat history in MySQL for compliance and personalized follow-ups
- Reducing response time by **70%** with Groq’s ultra-fast Llama4 inference

---

## ✨ Key Features
- **Real-Time Q&A**: Resolves logistics, pricing, and shipment queries instantly.
- **Conversational Memory**: Tracks chat history using MySQL and LangGraph.
- **RAG Pipeline**: Combines Google’s Gemini Embeddings with Chroma DB for precise data retrieval.
- **Multilingual Support**: Handles diverse languages for global customers.
- **Scalable Backend**: Flask API for seamless integration with DAHFOOD’s systems.

---

## 🧰 Tech Stack
| Category          | Tools                                                                 |
|-------------------|-----------------------------------------------------------------------|
| **AI/ML Models**  | Groq Llama4, GoogleGenerativeAIEmbeddings                             |
| **Frameworks**    | LangChain, LangGraph                                                  |
| **Database**      | MySQL (Chat History), Chroma DB (Vector Storage)                      |
| **Backend**       | Flask (Python), REST APIs                                             |
| **Languages**     | Python 3.9+                                                           |

---

## 🚀 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/dahfood-chatbot.git
   cd dahfood-chatbot

2. **Open Comand prompt on this folder and run this to connect with conda environment**:
  ```bash
  venv\Scripts\activate   


3. **Run this to install requirements for this project**:
  ```bash
  python install -r requirements.txt


4. **run chatbot with this command**
  ```bash
   python -m src.main


5. **Now run UI of Chatbot and Talk with it**
  ```bash
   start index.html

## run "start index.html" in other terminal command while running main.py
