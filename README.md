# 🤖 AutoStream Conversational AI Agent

## 📌 Project Overview

This project is a **Conversational AI Agent** built for a fictional SaaS company **AutoStream**, which provides automated video editing tools for content creators.

The agent is designed to simulate a real-world **Agentic Workflow** that can:

* Understand user intent
* Retrieve accurate information using a RAG pipeline
* Identify high-intent users
* Capture leads via tool execution

---

## 🚀 Features

### 🧠 Intent Detection

The agent classifies user input into:

* Greeting
* Pricing/Product Inquiry
* High-intent Lead
* Follow-up Queries
* Gratitude (Thanks)

---

### 📚 RAG (Retrieval-Augmented Generation)

* Uses a **local JSON knowledge base**
* Implements **similarity-based retrieval**
* Handles vague queries like:

  * “What do you offer?”
  * “Tell me about plans”
* Supports:

  * Pricing details
  * Plan features
  * Refund policy
  * Support information

---

### 🔄 Agentic Workflow (LangGraph)

* Built using **LangGraph**
* Modular node-based architecture:

  * Intent Node
  * RAG Node
  * Lead Capture Node
  * Tool Execution Node
* Uses conditional routing for dynamic flow

---

### 🛠️ Tool Execution (Lead Capture)

When high-intent is detected:

1. Agent asks for:

   * Name
   * Email
   * Platform
2. Executes mock tool:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

---

### 🧠 Context Awareness

* Maintains conversation state using LangGraph
* Supports follow-up queries like:

  * “Tell me more”
  * “Give me more details”

---

## 🏗️ Project Structure

```
autostream-agent/
│── app.py
│── requirements.txt
│── data/
│   └── knowledge_base.json
│── agent/
│   ├── graph.py
│   ├── intent_classifier.py
|   ├── memory.py
│   ├── rag_pipeline.py
│   ├── tools.py
|── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/somyasinghal0/autostream-agent.git
cd autostream-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

---

## 💬 Sample Interaction

```
You: Hi
Agent: Hello! Ask me anything about our plans 😊

You: Tell me about pricing
Agent: [Displays pricing plans]

You: I want to try Pro plan
Agent: Please provide details...

You: Somya, somya@gmail.com, YouTube
Agent: Lead captured successfully 🎉

You: What do you offer
Agent: [Displays pricing plans]
```

---

## 🧠 Architecture Explanation

This project uses **LangGraph** to implement an agentic workflow as a state machine. Each node represents a functional unit such as intent detection, retrieval, or tool execution. Conditional routing is used to dynamically decide the next step based on user intent.

State is maintained using a shared state object that persists information such as user input, detected intent, and conversation context (`last_topic`). This enables the agent to handle multi-turn conversations and follow-up queries effectively.

The RAG pipeline uses a structured JSON knowledge base combined with similarity-based retrieval to provide accurate and flexible responses.

---

## 📲 WhatsApp Integration (Concept)

To integrate this agent with WhatsApp:

1. Use **WhatsApp Business API** or services like Twilio
2. Set up a webhook endpoint (Flask/FastAPI)
3. Receive incoming messages via webhook
4. Pass message to the agent (`graph.invoke`)
5. Send agent response back to user

Flow:

```
User → WhatsApp → Webhook → Agent → Response → WhatsApp → User
```

---

## 📦 Tech Stack

* Python 3.9+
* LangGraph
* LangChain (optional)
* JSON (Knowledge Base)

---

## 🎯 Evaluation Highlights

* ✅ Correct intent classification
* ✅ RAG-based response generation
* ✅ Proper tool execution (no premature calls)
* ✅ Clean state management
* ✅ Real-world conversational flow

---

## 👩‍💻 Author

**Somya Singhal**

---

## ⭐ Final Note

This project demonstrates how to build a **production-style conversational AI agent** with modular design, context awareness, and tool integration — going beyond a simple chatbot.
